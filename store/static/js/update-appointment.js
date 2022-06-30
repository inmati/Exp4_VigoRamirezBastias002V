document.addEventListener('DOMContentLoaded', function () {

    const btnActualizarHora = document.getElementById('update-appointment-btn');

    btnActualizarHora.addEventListener('click', function () {
        let email = document.getElementById('email2').value;
        let date = document.getElementById('date1').value;

        fetch('http://127.0.0.1:8000/appointment/'+email+'/update',{
            method: 'PUT',
            headers: {
                'content-type': 'application/json'
            },
            body: JSON.stringify({
                    newDate: date
                })        
        })
        .then(response => response.json())
        .then(data => alert(JSON.stringify(data)))
        .catch(err => alert('Algo salió mal'))

    });
    
});