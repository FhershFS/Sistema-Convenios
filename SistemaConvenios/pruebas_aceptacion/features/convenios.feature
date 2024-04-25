@Crear_Convenio
Característica: Crear Convenios
    Yo como administrador 
    quiero registrar un convenio al sistema 
    para su posterior consulta y seguimiento de este mismo


    Escenario: Agregar exitosamente
        Dado ingreso al login
        Y Escribo el usuario "fherfelixs" y la contraseña "DarkRay8"
        Cuando cliqueo el botón identificarse
        Y puedo ver la página de inicio
        Cuando Presiono alguna de las categoria de los convenios
        Y presiono el boton + persona
        Y ingreso el nombre "pruebas89"
        Y presiono save en la persona
        Y presiono nuevamente la categoria del convenio
        Y presiono en el boton + unidad academica
        Y ingresooo el nombre "Electricas"
        Y presiono save en la categoria
        Y presiono por ultima vez la categoria del convenio
        Y presiono el botón +Convenio
        Y ingreso el número "28" 
        Y ingreso el tipo diversas instituciones
        Y ingreso la persona Prueba89
        Y ingreso la unidad Electrica
        Y presiono save
        Entonces obtengo el mensaje "Convenio agregado"

        Escenario: Agregar exitosamente
        Dado ingreso al login
        Y Escribo el usuario "fherfelixs" y la contraseña "DarkRay8"
        Cuando cliqueo el botón identificarse
        Y puedo ver la página de inicio
        Cuando Presiono alguna de las categoria de los convenios
        Y presiono el botón +Convenio
        Y ingreso el número "28" 
        Y ingreso el tipo diversas instituciones
        Y ingreso la persona Prueba89
        Y ingreso la unidad Electrica
        Y presiono save
        Entonces obtengo el mensajee "La clave ya existe"

    


