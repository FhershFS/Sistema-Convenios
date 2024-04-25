@Persona
Característica: Filtro de convenio por persona
    Como administrador
    quiero filtrar un convenio por su persona
    para poder ver qué convenio tiene esa persona

    Escenario: Filtro de convenio por persona exitosa
        Dado el inicio en el sistema
        Y pongo el nombre "fherfelixs" y contraseña "DarkRay8"
        Y oprimo identificarse btn
        Y estoy en el inicio
        Y presiono alguna categoria
        Y puedo ver en la pantalla de convenios seleccionada
        Y presiono en el boton agregar + persona 
        Y ingreso el nombre de persona: "Slayyter"
        Y presiono el save de la persona
        Y presiono nuevamente en la categoria del convenio que estoy probando
        Y presiono el boton de nueva + unidad academica
        Y ingresoooo el nombre de unidad "Uaz"
        Y presiono boton save en la categoria que estoy probando
        Y presiono una vez mas en la categoria del convenio que estoy probando
        Y presiono en el botón + Convenio para crearlo
        Y ingreso el número del convenio: "69" 
        Y ingreso en el tipo convenio diversas instituciones
        Y ingreso la persona Slayyter
        Y ingreso la unidad Uaz
        Y presiono en el btn de save
        Y obtengo el siguiente mensaje: "Convenio agregado"
        Y presiono una ultima vez en la categoria del convenio creado
        Y presiono en filtros
        Y selecciono la persona "Slayyter"
        Cuando presiono btn Buscar
        Entonces puedo ver el convenio con su persona "Slayyter" en la tabla de convenios
