const express = require('express');
const path = require('path');

const app = express();
const PORT = 7000; // frontend en 5000

// Servir archivos estáticos de /public
app.use(express.static(path.join(__dirname, 'public')));

app.listen(PORT, () => {
    console.log(`Frontend corriendo en http://localhost:${PORT}`);
});