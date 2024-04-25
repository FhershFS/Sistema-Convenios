Característica: Inicio de sesión
    Como usuario del sistema
    quiero iniciar sesión
    para realizar mis actividades dentro del sistema.


        Escenario: Usuario y/o contraseña inválida
            Dado Ingreso al sistema en su apartado de login
              Y escribo el nombre de usuario "azulito" y la contraseña "098122"
             Cuando presiono el botón Identificarse
             Entonces puedo ver el mensaje de error "Please enter a correct username and password. Note that both fields may be case-sensitive."

        Escenario: Usuario y/o contraseña válidas
            Dado Ingreso al sistema en su apartado de login
              Y escribo el nombre de usuario "fherfelixs" y la contraseña "DarkRay8"
             Cuando presiono el botón Identificarse
             Entonces puedo verla pantalla de inicio.