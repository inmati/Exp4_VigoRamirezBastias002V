$(document).ready(function () {

    $("#contact").validate({
        rules: {
            nombre: "required",
            apellidos: "required",
            fono: "required",
            email: {
                required: true,
                email: true
            }
        }, //rules
        messages: {
            nombre:{required: 'Campo requerido'},
            apellidos:{requird: 'Campo requerido'},
            email: {
                required: 'Ingresa tu correo electrónico',
                email: 'Formato de correo no válido'
            },
            fono: {
                required: 'Ingrese un número de celular',
                minlength: 'Cantidad de digitos insuficiente'
            }
        }
    });
});