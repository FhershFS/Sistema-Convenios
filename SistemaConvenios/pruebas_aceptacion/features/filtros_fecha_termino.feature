@fecha_termino
Característica: Filtro de convenio por fecha de término
    Como administrador
    quiero filtrar un convenio por su fecha de término
    para poder ver qué convenio tiene esa fecha de término

    Escenario: Filtro de convenio por fecha de término exitosa
        Dado el inicio sesión en el sistema 
        Y ingreso nombre de usuario: "fherfelixs" y la contraseña: "DarkRay8"
        Y oprimo el botón para iniciar en el sistema 
        Y veo la pantalla inicial del sistema
        Y presiono una categoria de la lista en el menú
        Y puedo ver la pantalla de convenios de esa categoria que se eligió en el menú
        Y presiono el botón de filtrar los convenios
        Y escribo la fecha de término del convenio "03/12/2023"
        Cuando presiono el botón para buscar algún convenio
        Entonces puedo ver el convenio con fecha de término 3/12/2023 y el número de convenio "5" en la tabla de convenios

    Escenario: Filtro de convenio por fecha de término no encontrada
        Dado el inicio sesión en el sistema 
        Y ingreso nombre de usuario: "fherfelixs" y la contraseña: "DarkRay8"
        Y oprimo el botón para iniciar en el sistema 
        Y veo la pantalla inicial del sistema
        Y presiono una categoria de la lista en el menú
        Y puedo ver la pantalla de convenios de esa categoria que se eligió en el menú
        Y presiono el botón de filtrar los convenios
        Y escribo la fecha de término del convenio "28/12/2023"
        Cuando presiono el botón para buscar algún convenio
        Entonces se muestra el mensaje siguiente: "No se encontraron resultados."