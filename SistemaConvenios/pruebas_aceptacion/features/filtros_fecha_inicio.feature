@fecha_inicio
Característica: Filtro de convenio por fecha de inicio
    Como administrador
    quiero filtrar un convenio por su fecha de inicio
    para poder ver qué convenio tiene esa fecha de inicio

    Escenario: Filtro de convenio por fecha de inicio exitosa
        Dado que inicio en el sistema en login
        Y pongo los datos nombre de usuario: "fherfelixs" y la contraseña "DarkRay8"
        Y oprimo el botón para iniciar sesión
        Y veo la pantalla de inicio de sesión
        Y presiono una de las categorias de la lista del menú 
        Y puedo ver la pantalla de convenios de esa categoria presionada
        Y oprimo en el boton + persona 
        Y pongo en el nombre de persona: "Slayyter"
        Y oprimo el save 
        Y oprimo nuevamente en la categoria 
        Y oprimo el boton + unidad academica
        Y pongo el nombre de unidad: "Uaz"
        Y oprimo boton save 
        Y oprimo una vez mas en la categoria 
        Y oprimo en el botón + 
        Y pongo el num de convenio: "5" 
        Y pongo en el tipo convenio la diversas instituciones
        Y ingreso la fecha de inicio del convenio: "03/12/2023"
        Y ingreso la fecha de ingreso del convenio: "03/12/2023"
        Y ingreso la fecha de salida del convenio: "03/12/2023"
        Y ingreso la fecha de termino del convenio: "03/12/2023"
        Y pongo la persona: Slayyter
        Y pongo la unidad: Uaz
        Y oprimo en el boton de guardar el convenio
        Y obtengo: "Convenio agregado"
        Y oprimo una ultima vez en la categoria








        Y presiono el botón de los filtros
        Y escribo la fecha de inicio del convenio "03/12/2023"
        Cuando presiono el botón buscar y filtrar
        Entonces puedo ver el convenio con fecha de inicio "Dec. 3, 2023" en la tabla de convenios

    Escenario: Filtro de convenio por fecha de inicio no encontrada
       Dado que inicio en el sistema en login
        Y pongo los datos nombre de usuario: "fherfelixs" y la contraseña "DarkRay8"
        Y oprimo el botón para iniciar sesión
        Y veo la pantalla de inicio de sesión
        Y presiono una de las categorias de la lista del menú 
        Y puedo ver la pantalla de convenios de esa categoria presionada
        Y presiono el botón de los filtros
        Y escribo la fecha de inicio del convenio "28/12/2023"
        Cuando presiono el botón buscar y filtrar
        Entonces puedo ver lo siguiente: "No se encontraron resultados."