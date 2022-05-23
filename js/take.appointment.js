$(document).ready(function(){

    let btnAgendarHora = document.getElementById('take-appointment');
    let card = document.getElementById('card');
    let fecha = document.getElementById('datetimepicker1Input');
    let nombre = document.getElementById('name');
    let apellidos = document.getElementById('last-name');
    let fono = document.getElementById('phone');
    let email = document.getElementById('email');

    console.log(fecha.value);
    console.log(nombre.value);
    consoe.log(apellidos.value);
    console.log(fono.value);
    console.log(email.value);

    btnAgendarHora.addEventListener('click', function () {

        if (fecha.value === '' || nombre.value === '' || apellidos.value === '' || fono.value === '' || email.value === '') {

            alert('Debes completar todos los campos');

            fecha.value = '';
            nombre.value = '';
            apellidos.value = '';
            fono.value = '';
            email.value = '';

        } else {
            
            card.innerHTML = `
            <div class="col-5 purple-card" id="card">
                <h3 class="nav-font">Cita agendada</h3>
                <br>
                <h6 class="nav-font">${nombre.value}</h6>
                <h6 class="nav-font">${email.value}</h6>
                <h6 class="nav-font">${fecha.value}</h6>
                <br>
                <p class="nav-font"><strong>Te llamaremos un día antes para confirmar hora.</strong></p>
            </div>
            `;

            fecha.value = '';
            nombre.value = '';
            apellidos.value = '';
            fono.value = '';
            email.value = '';

        }
    });
});