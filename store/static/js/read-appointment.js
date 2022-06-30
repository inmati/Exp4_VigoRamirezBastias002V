document.addEventListener('DOMContentLoaded', function () {

    const btnConsultarHora = document.getElementById('get-appointment-btn');    

    btnConsultarHora.addEventListener('click', function () {

        let email = document.getElementById('email1').value;
        fetch('http://127.0.0.1:8000/appointment/'+email+'/read',{
            method: 'GET',
            headers: {
                'content-type': 'application/json'
            }      
        })
        .then(response => response.json())
        .then(data => alert(JSON.stringify(data)))
        .catch(err => alert('Algo salió mal'))

    });

});