document.addEventListener('DOMContentLoaded', function () {

    const btnAgendarHora = document.getElementById('appointment-btn');  
    btnAgendarHora.addEventListener('click', function () {

        let nombre = document.getElementById('nombre').value;
        let apellido = document.getElementById('apellido').value;
        let correo = document.getElementById('email').value;
        let fecha = document.getElementById('datetimepicker1Input').value;
        let direccion = document.getElementById('direccion').value;
        let celular = document.getElementById('cel').value;
        let cardName = document.getElementById('card-name');
        let cardEmail = document.getElementById('card-email');
        let cardDate = document.getElementById('card-date');

        if (nombre === '' || apellido === '' || correo === '' || fecha === '' || direccion === '' || celular === '') {
            alert('Debes completar todos los datos');
            let nombre = '';
            apellido = '';
            correo = '';
            fecha = '';
            direccion =''; 
            celular = '';
        } else {

            let nombreCompleto = nombre+' '+apellido;
            cardName.innerText = nombreCompleto;
            cardEmail.innerText = correo;
            cardDate.innerText = fecha;

            apellido = '';
            correo = '';
            fecha = '';
            direccion =''; 
            celular = '';
        }

    });

});