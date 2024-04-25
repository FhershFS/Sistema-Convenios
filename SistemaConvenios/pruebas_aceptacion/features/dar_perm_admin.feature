@Admin
Característica: Dar permisos de administrador a un usuario
    Yo como administrador
    quiero dar permisos de administrador a un usuario registrado 
    para que el usuario pueda tener acceso completo a la plataforma


    Escenario: Cambio correcto
        Dado ingreso al login
        Y Escribo el usuario "fherfelixs" y la contraseña "DarkRay8"
        Cuando cliqueo el botón identificarse
        Y puedo ver la página de inicio
        Cuando Presiono en administrar usuarios
        y presiono el botón de cambiar permisos al primer usuario
        y selecciono el grupo de admin
        y presiono guardar
        y cierro sesión
        y ingreso al login
        Y Escribo el usuario "ErickSan01" y la contraseña "Contra123"
        Cuando cliqueo el botón identificarse
        Y puedo ver la página de inicio
        Entonces puedo ver la seccion "Admin. Usuarios"