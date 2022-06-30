document.addEventListener('DOMContentLoaded', function () {

    const btnAgendarHora = document.getElementById('appointment-btn');    

    btnAgendarHora.addEventListener('click', function () {

        let name = document.getElementById('nombre').value;
        let last_name = document.getElementById('apellido').value;
        let email = document.getElementById('email').value;
        let date = document.getElementById('date').value;
        let address = document.getElementById('direccion').value;
        let cel = document.getElementById('cel').value;

        fetch('http://127.0.0.1:8000/appointment/create',{
            method: 'POST',
            headers: {
                'content-type': 'application/json'
            },
            body: JSON.stringify({
                    nombre: name,
                    apellido: last_name,
                    email: email,
                    direccion: address,
                    fono: cel,
                    fecha: date
                })        
        })
        .then(response => response.json())
        .then(data => alert(JSON.stringify(data)))
        .catch(err => alert('Algo salió mal'))

    });
});