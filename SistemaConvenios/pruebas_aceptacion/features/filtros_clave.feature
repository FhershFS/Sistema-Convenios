@Clave
Característica: Filtro de convenio por clave
    Como administrador
    quiero filtrar un convenio por su clave
    para poder ver qué convenio tiene esa clave

    Escenario: Filtro de convenio por clave exitosa
        Dado inicio en el sistema en su apartado de login
        Y pongo el nombre de usuario "fherfelixs" y la contraseña "DarkRay8"
        Y oprimo el botón Identificarse
        Y veo el inicio
        Y presiono la categoria de convenios Diversas Instituciones
        Y puedo verla pantalla de convenios Diversas Instituciones.
        Y presiono en el boton + persona
        Y ingreso el nombre de persona "puset"
        Y presiono el save en la persona
        Y presiono nuevamente en la categoria del convenio
        Y presiono el boton + unidad academica
        Y ingresooo el nombre de unidad "Nutricion"
        Y presiono boton save en la categoria
        Y presiono una vez mas en la categoria del convenio
        Y presiono en el botón + Convenio
        Y ingreso el número de convenio "123" 
        Y ingreso en el tipo diversas instituciones
        Y ingreso la persona puset
        Y ingreso la unidad Nutricion
        Y presiono en save
        Y obtengo el mensaje: "Convenio agregado"
        Y presiono por ultima vez en la categoria del convenio creado
        Y presiono el botón de filtros
        Y escribo la clave del convenio "15"
        Cuando presiono el botón Buscar
        Entonces puedo ver el convenio con clave 15 y el número de convenio "123" en la tabla de convenios

    Escenario: Filtro de convenio por clave no encontrada
        Dado inicio en el sistema en su apartado de login
        Y pongo el nombre de usuario "fherfelixs" y la contraseña "DarkRay8"
        Y oprimo el botón Identificarse
        Y veo el inicio
        Y presiono la categoria de convenios Diversas Instituciones
        Y puedo verla pantalla de convenios Diversas Instituciones.
        Y presiono el botón de filtros
        Y escribo la clave del convenio "666"
        Cuando presiono Buscar
        Entonces puedo ver el mensaje "No se encontraron resultados."