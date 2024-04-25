import time
from time import sleep
from behave import when, then, given
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


@given(u'que inicio en el sistema en login')
def step_impl(context):
    driver = webdriver.Chrome()
    driver.get('http://127.0.0.1:8000/usuarios/login/')
    context.driver = driver


@given(u'pongo los datos nombre de usuario: "{usuario}" y la contraseña "{contra}"')
def step_impl(context, usuario, contra):
    context.driver.find_element(By.NAME, 'username').send_keys(usuario)
    context.driver.find_element(By.NAME, 'password').send_keys(contra)


@given(u'oprimo el botón para iniciar sesión')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="submit"]').click()


@given(u'veo la pantalla de inicio de sesión')
def step_impl(context):

    home_screen_element = context.driver.find_element(
        By.XPATH, '//*[@id="panel"]/h1')
    assert home_screen_element.is_displayed(), "Home screen not displayed"


@given(u'presiono una de las categorias de la lista del menú')
def step_impl(context):
    # Espera hasta que el elemento sea visible y clickeable
    element = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'btn-dvst'))
    )

    # Utiliza ActionChains para realizar una acción de clic con un pequeño desplazamiento
    action = ActionChains(context.driver)
    action.move_to_element(element).click().perform()

    time.sleep(3)


@given(u'puedo ver la pantalla de convenios de esa categoria presionada')
def step_impl(context):
    # Implementa el código necesario para verificar que se vea la pantalla de convenios
    home_screen_element = context.driver.find_element(
        By.XPATH, '//*[@id="panel"]/h3')
    assert home_screen_element.is_displayed(), "Home screen not displayed"


time.sleep(5)


@given(u'oprimo en el boton + persona')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div[2]/a[5]').click()
    time.sleep(2)


@given(u'pongo en el nombre de persona: "{persona}"')
def step_impl(context, persona):
    context.driver.find_element(By.NAME, 'nombre').send_keys(persona)
    time.sleep(2)


@given(u'oprimo el save')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '//*[@id="panel"]/div/form/button').click()
    time.sleep(2)


@given(u'oprimo nuevamente en la categoria')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '/html/body/nav/div/div[2]/div/ul[1]/li[2]').click()
    time.sleep(2)


@given(u'oprimo el boton + unidad academica')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div[2]/a[3]').click()
    time.sleep(2)


@given(u'pongo el nombre de unidad: "{nombre}"')
def step_impl(context, nombre):
    context.driver.find_element(By.NAME, 'nombre').send_keys(nombre)
    time.sleep(2)


@given(u'oprimo boton save')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '//*[@id="panel"]/div/form/button').click()
    time.sleep(2)


@given(u'oprimo una vez mas en la categoria')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '/html/body/nav/div/div[2]/div/ul[1]/li[2]').click()
    time.sleep(2)


@given(u'oprimo en el botón +')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div[2]/a[1]').click()
    time.sleep(2)


@given(u'pongo el num de convenio: "{numero}"')
def step_impl(context, numero):
    context.driver.find_element(By.NAME, 'numero').send_keys(numero)


@given(u'pongo en el tipo convenio la diversas instituciones')
def step_impl(context):
    context.driver.find_element(By.ID, "id_tipo_0").click()


@given(u'ingreso la fecha de inicio del convenio: "{clave}"')
def step_impl(context, clave):
    context.driver.find_element(
        By.XPATH, '/html/body/div/div/form/div[4]/input').send_keys(clave)

    sleep(2)


@given(u'ingreso la fecha de ingreso del convenio: "{clave}"')
def step_impl(context, clave):
    context.driver.find_element(
        By.XPATH, '/html/body/div/div/form/div[3]/input').send_keys(clave)

    sleep(2)


@given(u'ingreso la fecha de salida del convenio: "{clave}"')
def step_impl(context, clave):
    context.driver.find_element(
        By.XPATH, '/html/body/div/div/form/div[5]/input').send_keys(clave)

    sleep(2)


@given(u'ingreso la fecha de termino del convenio: "{clave}"')
def step_impl(context, clave):
    context.driver.find_element(
        By.XPATH, '/html/body/div/div/form/div[6]/input').send_keys(clave)

    sleep(2)


@given(u'pongo la persona: Slayyter')
def step_impl(context):
    select = Select(context.driver.find_element(By.NAME, "persona_tramito"))
    select.select_by_index(1)


@given(u'pongo la unidad: Uaz')
def step_impl(context):
    select = Select(context.driver.find_element(By.NAME, "unidad_academica"))
    select.select_by_index(1)


@given(u'oprimo en el boton de guardar el convenio')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '//*[@id="panel"]/div/form/button').click()
    time.sleep(2)


@given(u'obtengo: "{mensaje}"')
def step_impl(context, mensaje):
    assert mensaje in context.driver.page_source
    time.sleep(2)


@given(u'oprimo una ultima vez en la categoria')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '/html/body/nav/div/div[2]/div/ul[1]/li[2]').click()
    time.sleep(2)


@given(u'presiono el botón de los filtros')
def step_impl(context):
    # Espera hasta que el elemento sea visible y clickeable
    element = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="btnFiltros"]'))
    )

    # Utiliza ActionChains para realizar una acción de clic con un pequeño desplazamiento
    action = ActionChains(context.driver)
    action.move_to_element(element).click().perform()


@given(u'escribo la fecha de inicio del convenio "{clave}"')
def step_impl(context, clave):
    context.driver.find_element(
        By.XPATH, '/html/body/div[1]/form/div/div[5]/div[1]/input').send_keys(clave)

    context.driver.find_element(
        By.XPATH, '/html/body/div[1]/form/div/div[5]/div[2]/input').send_keys(clave)

    sleep(2)


@when(u'presiono el botón buscar y filtrar')
def step_impl(context):
    # Espera hasta que el elemento sea visible y clickeable
    element = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="filtrosContainer"]/div[7]/button'))
    )

    # Utiliza ActionChains para realizar una acción de clic con un pequeño desplazamiento
    action = ActionChains(context.driver)
    action.move_to_element(element).click().perform()


@then(u'puedo ver el convenio con fecha de inicio "{clave}" en la tabla de convenios')
def step_impl(context, clave):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/a/div/table'))
    )

    tabla = context.driver.find_element(By.XPATH, '/html/body/a/div/table')
    tbody = tabla.find_element(By.TAG_NAME, 'tbody')
    rows = tbody.find_elements(By.TAG_NAME, 'tr')

    claves = []

    for row in rows:
        tercera_celda = WebDriverWait(row, 10).until(
            EC.presence_of_element_located((By.XPATH, 'td[3]'))
        )
        id = tercera_celda.text
        claves.append(id)

    assert clave in claves

    sleep(5)


@then(u'puedo ver lo siguiente: "No se encontraron resultados."')
def step_impl(context):
    # Espera hasta 10 segundos para que el mensaje aparezca
    mensaje_element = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//h1[contains(text(), "No se encontraron resultados.")]'))
    )
    assert mensaje_element.is_displayed(
    ), "No se encontró el mensaje 'No se encontraron resultados.' en la pantalla"

    sleep(5)


sleep(5)
