@Editar_Convenio
Característica: Eliminar Convenio

    Yo como administrador 
    quiero eliminar un convenio 
    cuando ya no sea requerido.

    Escenario:
        Dado que visualizo el login
        Y anoto el usuario "fherfelixs" y la contraseña "DarkRay8"
        Cuando pincho el botón identificarse
        Y puedo apreciar la página de inicio
        Cuando pincho alguna de las categoria de los convenios
        y pincho el boton + persona
        y anoto el nombre "prueba89123123"
        y pincho save en la persona
        y pincho nuevamente la categoria del convenio
        y pincho en el boton + unidad academica
        y anotoo el nombre "Químicas"
        y pincho save en la categoria
        y pincho otra vez la categoria del convenio
        y pincho el botón +Convenio
        y anoto el número "12/123" 
        y anoto el tipo diversas instituciones
        y anoto la persona
        y anoto la unidad
        y pincho save
        y pincho por ultima vez la categoria del convenio
        y pincho el boton con el icono de basura a la derecha del convenio
        Entonces observo el mensaje "¿Esta seguro de que quiere borrar el siguiente Convenio?"
        y cuando pulso borrar
        Entonces visualizo el mensaje "Convenio eliminado"