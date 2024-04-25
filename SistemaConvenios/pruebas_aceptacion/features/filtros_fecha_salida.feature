@fecha_salida
Característica: Filtro de convenio por fecha de salida
    Como administrador
    quiero filtrar un convenio por su fecha de salida
    para poder ver qué convenio tiene esa fecha de salida

    Escenario: Filtro de convenio por fecha de salida exitosa
        Dado que inicio sesión en el sistema 
        Y pongo el nombre de usuario: "fherfelixs" y la contraseña: "DarkRay8"
        Y oprimo el botón para iniciar sesion 
        Y veo la pantalla de inicio del sistema
        Y presiono una categoria de la lista de convenios
        Y puedo ver la pantalla de convenios de esa categoria que se eligió
        Y presiono el botón de filtrar convenios
        Y escribo la fecha de salida del convenio "03/12/2023"
        Cuando presiono el botón para buscar el convenio
        Entonces puedo ver el convenio con fecha de salida 3/12/2023 y el número de convenio "5" en la tabla de convenios

    Escenario: Filtro de convenio por fecha de salida no encontrada
        Dado que inicio sesión en el sistema 
        Y pongo el nombre de usuario: "fherfelixs" y la contraseña: "DarkRay8"
        Y oprimo el botón para iniciar sesion 
        Y veo la pantalla de inicio del sistema
        Y presiono una categoria de la lista de convenios
        Y puedo ver la pantalla de convenios de esa categoria que se eligió
        Y presiono el botón de filtrar convenios
        Y escribo la fecha de salida del convenio "28/12/2023"
        Cuando presiono el botón para buscar el convenio
        Entonces puedo observar el mensaje siguiente: "No se encontraron resultados."