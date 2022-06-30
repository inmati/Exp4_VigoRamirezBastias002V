document.addEventListener('DOMContentLoaded', function () {

    const btnCancelarHora = document.getElementById('delete-appointment-btn');
    
    btnCancelarHora.addEventListener('click', function () {
        let email = document.getElementById('email3').value;

        fetch('http://127.0.0.1:8000/appointment/'+email+'/delete',{
            method: 'DELETE',
            headers: {
                'content-type': 'application/json'
            }       
        })
        .then(response => response.json())
        .then(data => alert(JSON.stringify(data)))
        .catch(err => alert('Algo salió mal'))

    });

});