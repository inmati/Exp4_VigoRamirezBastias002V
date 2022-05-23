$(document).ready(

    $(function () {
        $("#pide-tu-hora").validate({
            rules: {
                email: {
                    required: true,
                    email: true
                },
                nombre: "required",
                apellido: "required",
                fono: "required",
                direccion: "required",
            },
            messages: {
                email: {
                    required: 'Ingresa tu correo electrónico',
                    email: 'Formato de correo no válido'
                },
                nombre: {
                    required: 'Ingrese un nombre',
                },
                apellido: {
                    required: 'Ingrese un apellido',
                },
                fono: {
                    required: 'Ingrese un número de celular',
                    minlength: 'Cantidad de digitos insuficiente'
                },
                direccion: {
                    required: 'Ingrese una dirección',
                }
            }//messages
        }); //$('#mi-formulario').validate
    })
);
