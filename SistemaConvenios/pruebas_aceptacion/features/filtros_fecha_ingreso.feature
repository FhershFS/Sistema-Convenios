@fecha_ingreso
Característica: Filtro de convenio por fecha de ingreso
    Como administrador
    quiero filtrar un convenio por su fecha de ingreso
    para poder ver qué convenio tiene esa fecha de ingreso

    Escenario: Filtro de convenio por fecha de ingreso exitosa
        Dado inicio en el sistema login
        Y pongo el nombre de usuario: "fherfelixs" y la contraseña "DarkRay8"
        Y oprimo el botón para iniciar
        Y veo la pantalla de inicio
        Y presiono una categoria de la lista
        Y puedo ver la pantalla de convenios de esa categoria elegida.
        Y presiono el botón de filtrado
        Y escribo la fecha de ingreso del convenio "03/12/2023"
        Cuando presiono el botón para Buscar
        Entonces puedo ver el convenio con fecha de ingreso 3/12/2023 y el número de convenio "5" en la tabla de convenios

    Escenario: Filtro de convenio por fecha de ingreso no encontrada
        Dado inicio en el sistema login
        Y pongo el nombre de usuario: "fherfelixs" y la contraseña "DarkRay8"
        Y oprimo el botón para iniciar
        Y veo la pantalla de inicio
        Y presiono una categoria de la lista
        Y puedo ver la pantalla de convenios de esa categoria elegida.
        Y presiono el botón de filtrado
        Y escribo la fecha de ingreso del convenio "28/12/2023"
        Cuando presiono el botón para Buscar
        Entonces puedo ver el mensaje siguiente: "No se encontraron resultados."