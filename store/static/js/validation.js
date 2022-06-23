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
            }
        }); $('#registrate').validate({
            rules: {
                email: {
                    required: true,
                    email: true
                },
                nombre: "required",
                apellido: "required",
                fono: "required",
                direccion: "required",
                username: "required",
                password: {
                    required: true
                },
                password2: {
                    required: true,
                    equalTo: '#pass'
                }
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
                },
                username: {
                    required: 'Ingrese un apellido',
                },
                password: {
                    required: 'Ingresa una contraseña',
                    minlength: 'Caracteres insuficientes'
                },
                password2:{
                    required: 'Ingresa una contraseña',
                    equalTo: 'Las contraseñas no coinciden',
                    minlength: 'Caracteres insuficientes'
                }
            }

        });
    })
);
