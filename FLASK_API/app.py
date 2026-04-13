from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
db = SQLAlchemy(app)
CORS(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    phone = db.Column(db.String(11))
    
    def serialize(self):
        return {
            'id':self.id,
            'name':self.name,
            'email':self.email,
            'phone': self.phone
        }
        
with app.app_context():
    db.create_all()
    

@app.route('/contacts', methods = ['GET'])
def get_contacts():
    contacts = Contact.query.all()
    return jsonify({'contacts': [c.serialize() for c in contacts]})

@app.route('/contacts', methods = ['POST'])
def add_contacts():
    data = request.get_json()
    c = Contact(name = data['name'], email = data['email'], phone = data['phone'])
    db.session.add(c)
    db.session.commit()
    return jsonify({'message':'Contacto Creado con exito'})

@app.route('/contacts/<int:id>', methods = ['GET'])
def get_contactsid(id):
    c = Contact.query.get(id)
    if not c:
        return jsonify({'message':'No existe el contacto'}), 404
    return jsonify(c.serialize())

@app.route('/contacts/<int:id>', methods = ['PUT', 'PATCH'])
def edit_contact(id):
    c = Contact.query.get_or_404(id)
    data = request.get_json()
    
    if 'name' in data:
        c.name = data['name']
    if 'email' in data:
        c.email = data['email']
    if 'phone' in data:
        c.phone = data['phone']
        
    db.session.commit()
    return jsonify({'message':'Datos actualizados', 'c': c.serialize() })

@app.route('/contacts/<int:id>', methods = ['DELETE'])
def delete_contact(id):
    c = Contact.query.get(id)
    if not c:
        return jsonify({'message':'Contacto no encontrado'}), 404
    
    db.session.delete(c)
    db.session.commit()
    return jsonify({'message':'Contacto borrado'})


        
    

    
    
if __name__ == '__main__':
    app.run(port=3000, debug=True)
    
    
    
    