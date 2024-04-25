@Status
Característica: Filtro de convenio por status
    Como administrador
    quiero filtrar un convenio por su status
    para poder ver qué convenio tiene esa status

    Escenario: Filtro de convenio por status terminado
        Dado que inicio en el sistema 
        Y pongo el nombre "fherfelixs" y su contraseña: "DarkRay8"
        Y oprimo para dentificarme
        Y veo el inicio del sistema
        Y presiono alguna de las categoria de convenios 
        Y puedo ver en la pantalla de convenios los de esa categoria
        Y presiono el botón para los filtros
        Y selecciono la status "Terminado"
        Cuando presiono en Buscar
        Entonces puedo ver el convenio con su status "TERMINADO" en la tabla de convenios

    Escenario: Filtro de convenio por status no empezado
        Dado que inicio en el sistema 
        Y pongo el nombre "fherfelixs" y su contraseña: "DarkRay8"
        Y oprimo para dentificarme
        Y veo el inicio del sistema
        Y presiono alguna de las categoria de convenios 
        Y puedo ver en la pantalla de convenios los de esa categoria
        Y presiono el botón para los filtros
        Y selecciono la status "No empezado"
        Cuando presiono en Buscar
        Entonces puedo ver el convenio con su status "NO EMPEZADO" en la tabla de convenios

    Escenario: Filtro de convenio por status en espera
        Dado que inicio en el sistema 
        Y pongo el nombre "fherfelixs" y su contraseña: "DarkRay8"
        Y oprimo para dentificarme
        Y veo el inicio del sistema
        Y presiono alguna de las categoria de convenios 
        Y puedo ver en la pantalla de convenios los de esa categoria
        Y presiono el botón para los filtros
        Y selecciono la status "En espera"
        Cuando presiono en Buscar
        Entonces puedo ver el convenio con su status "ESPERA" en la tabla de convenios

    Escenario: Filtro de convenio por status en espera no encontrado
        Dado que inicio en el sistema 
        Y pongo el nombre "fherfelixs" y su contraseña: "DarkRay8"
        Y oprimo para dentificarme
        Y veo el inicio del sistema
        Y presiono alguna de las categoria de convenios 
        Y puedo ver en la pantalla de convenios los de esa categoria
        Y presiono el botón para los filtros
        Y selecciono la status "En espera"
        Cuando presiono en Buscar
        Entonces Veo: "No se encontraron resultados."

    Escenario: Filtro de convenio por status no encontrado
        Dado que inicio en el sistema 
        Y pongo el nombre "fherfelixs" y su contraseña: "DarkRay8"
        Y oprimo para dentificarme
        Y veo el inicio del sistema
        Y presiono alguna de las categoria de convenios 
        Y puedo ver en la pantalla de convenios los de esa categoria
        Y presiono el botón para los filtros
        Y selecciono la status "No empezado"
        Cuando presiono en Buscar
        Entonces Veo: "No se encontraron resultados."


    Escenario: Filtro de convenio por status terminado no encontrado
        Dado que inicio en el sistema 
        Y pongo el nombre "fherfelixs" y su contraseña: "DarkRay8"
        Y oprimo para dentificarme
        Y veo el inicio del sistema
        Y presiono alguna de las categoria de convenios 
        Y puedo ver en la pantalla de convenios los de esa categoria
        Y presiono el botón para los filtros
        Y selecciono la status "Terminado"
        Cuando presiono en Buscar
        Entonces Veo: "No se encontraron resultados."

   

    
 

