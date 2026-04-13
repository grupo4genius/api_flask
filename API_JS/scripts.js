const API_URL = "http://localhost:3000/contacts"; // tu endpoint Flask

async function cargarContactos() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) throw new Error("Error al conectar con la API");

        const contactos = await response.json();

        const tbody = document.getElementById("tabla-body");
        tbody.innerHTML = ""; // limpiar tabla

        contactos.forEach(c => {
            const tr = document.createElement("tr");
            tr.innerHTML = `
                <td>${c.name}</td>
                <td>${c.email}</td>
                <td>${c.phone}</td>
            `;
            tbody.appendChild(tr);
        });
    } catch (err) {
        console.error(err);
    }
}

cargarContactos();