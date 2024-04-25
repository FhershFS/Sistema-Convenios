@Unidad
Característica: Filtro de convenio por unidad
    Como administrador
    quiero filtrar un convenio por su unidad
    para poder ver qué convenio tiene esa unidad

    Escenario: Filtro de convenio por unidad exitosa
        Dado inicio en el sistema
        Y pongo el nombre  "fherfelixs" y la contraseña "DarkRay8"
        Y oprimo Identificarse
        Y veo  el inicio
        Y presiono la categoria de convenios Diversas Instituciones.
        Y puedo ver en la pantalla de convenios Diversas Instituciones.
        Y oprimo en el boton agregar + persona 
        Y ingreso en el nombre de persona: "Slayyter"
        Y oprimo el save de la persona ingresada
        Y oprimo nuevamente en la categoria del convenio de prueba
        Y oprimo el boton de nueva + unidad academica
        Y ingreso el nombre de unidad: "Uaz"
        Y oprimo boton save en la unidad ingresada
        Y oprimo una vez mas en la categoria del convenio de prueba
        Y oprimo en el botón + Convenio para crearlo
        Y ingreso el num de convenio: "99" 
        Y ingreso en el tipo convenio la diversas instituciones
        Y ingreso la persona: Slayyter
        Y ingreso la unidad: Uaz
        Y oprimo en el boton de guardar
        Y obtengo el mensaje siguiente de: "Convenio agregado"
        Y oprimo una ultima vez en la categoria del convenio de prueba
        Y presiono el botón filtros
        Y selecciono la unidad "Uaz"
        Cuando presiono Buscar
        Entonces puedo ver el convenio con su unidad "Uaz" en la tabla de convenios
