import time
from time import sleep
from behave import when, then, given
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


@given(u'inicio en el sistema')
def step_impl(context):
    driver = webdriver.Chrome()
    driver.get('http://127.0.0.1:8000/usuarios/login/')
    context.driver = driver


@given(u'pongo el nombre  "{usuario}" y la contraseña "{contra}"')
def step_impl(context, usuario, contra):
    context.driver.find_element(By.NAME, 'username').send_keys(usuario)
    context.driver.find_element(By.NAME, 'password').send_keys(contra)


@given(u'oprimo Identificarse')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="submit"]').click()


@given(u'veo  el inicio')
def step_impl(context):

    home_screen_element = context.driver.find_element(
        By.XPATH, '//*[@id="panel"]/h1')
    assert home_screen_element.is_displayed(), "Home screen not displayed"


@given(u'presiono la categoria de convenios Diversas Instituciones.')
def step_impl(context):
    # Espera hasta que el elemento sea visible y clickeable
    element = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'btn-dvst'))
    )

    # Utiliza ActionChains para realizar una acción de clic con un pequeño desplazamiento
    action = ActionChains(context.driver)
    action.move_to_element(element).click().perform()

    time.sleep(3)


@given(u'puedo ver en la pantalla de convenios Diversas Instituciones.')
def step_impl(context):
    # Implementa el código necesario para verificar que se vea la pantalla de convenios
    home_screen_element = context.driver.find_element(
        By.XPATH, '//*[@id="panel"]/h3')
    assert home_screen_element.is_displayed(), "Home screen not displayed"


time.sleep(5)


@given(u'oprimo en el boton agregar + persona')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div[2]/a[5]').click()
    time.sleep(2)


@given(u'ingreso en el nombre de persona: "{persona}"')
def step_impl(context, persona):
    context.driver.find_element(By.NAME, 'nombre').send_keys(persona)
    time.sleep(2)


@given(u'oprimo el save de la persona ingresada')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '//*[@id="panel"]/div/form/button').click()
    time.sleep(2)


@given(u'oprimo nuevamente en la categoria del convenio de prueba')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '/html/body/nav/div/div[2]/div/ul[1]/li[2]').click()
    time.sleep(2)


@given(u'oprimo el boton de nueva + unidad academica')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div[2]/a[3]').click()
    time.sleep(2)


@given(u'ingreso el nombre de unidad: "{nombre}"')
def step_impl(context, nombre):
    context.driver.find_element(By.NAME, 'nombre').send_keys(nombre)
    time.sleep(2)


@given(u'oprimo boton save en la unidad ingresada')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '//*[@id="panel"]/div/form/button').click()
    time.sleep(2)


@given(u'oprimo una vez mas en la categoria del convenio de prueba')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '/html/body/nav/div/div[2]/div/ul[1]/li[2]').click()
    time.sleep(2)


@given(u'oprimo en el botón + Convenio para crearlo')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div[2]/a[1]').click()
    time.sleep(2)


@given(u'ingreso el num de convenio: "{numero}"')
def step_impl(context, numero):
    context.driver.find_element(By.NAME, 'numero').send_keys(numero)


@given(u'ingreso en el tipo convenio la diversas instituciones')
def step_impl(context):
    context.driver.find_element(By.ID, "id_tipo_0").click()


@given(u'ingreso la persona: Slayyter')
def step_impl(context):
    select = Select(context.driver.find_element(By.NAME, "persona_tramito"))
    select.select_by_index(1)


@given(u'ingreso la unidad: Uaz')
def step_impl(context):
    select = Select(context.driver.find_element(By.NAME, "unidad_academica"))
    select.select_by_index(1)


@given(u'oprimo en el boton de guardar')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '//*[@id="panel"]/div/form/button').click()
    time.sleep(2)


@given(u'obtengo el mensaje siguiente de: "{mensaje}"')
def step_impl(context, mensaje):
    assert mensaje in context.driver.page_source
    time.sleep(2)


@given(u'oprimo una ultima vez en la categoria del convenio de prueba')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '/html/body/nav/div/div[2]/div/ul[1]/li[2]').click()
    time.sleep(2)


@given(u'presiono el botón filtros')
def step_impl(context):
    # Espera hasta que el elemento sea visible y clickeable
    element = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="btnFiltros"]'))
    )

    # Utiliza ActionChains para realizar una acción de clic con un pequeño desplazamiento
    action = ActionChains(context.driver)
    action.move_to_element(element).click().perform()
    sleep(3)


@given(u'selecciono la unidad "{unidad}"')
def step_impl(context, unidad):
    # Encuentra el elemento select por su id
    select_element = context.driver.find_element(By.ID, 'category')

    # Usa la clase Select para interactuar con el elemento select
    select = Select(select_element)

    # Selecciona la opción por su texto visible (en este caso, la variable unidad ya es la cadena correcta)
    select.select_by_visible_text(unidad)

    # Puedes esperar un tiempo opcional si es necesario
    sleep(3)


@when(u'presiono Buscar')
def step_impl(context):
    # Espera hasta que el elemento sea visible y clickeable
    element = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="filtrosContainer"]/div[7]/button'))
    )

    # Utiliza ActionChains para realizar una acción de clic con un pequeño desplazamiento
    action = ActionChains(context.driver)
    action.move_to_element(element).click().perform()


@then(u'puedo ver el convenio con su unidad "{clave}" en la tabla de convenios')
def step_impl(context, clave):
    # Espera hasta 10 segundos para que la tabla aparezca
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/a/div/table'))
    )

    tabla = context.driver.find_element(By.XPATH, '/html/body/a/div/table')
    tbody = tabla.find_element(By.TAG_NAME, 'tbody')
    rows = tbody.find_elements(By.TAG_NAME, 'tr')

    for row in rows:
        # Espera hasta 10 segundos para que la sexta celda aparezca
        sexta_celda = WebDriverWait(row, 10).until(
            EC.presence_of_element_located((By.XPATH, 'td[6]'))
        )

        # Verifica si el texto en la sexta celda coincide con la clave
        if sexta_celda.text == clave:
            # Muestra un mensaje si encuentra la clave
            print(
                f"Se encontró la clave '{clave}' en la sexta columna de la tabla.")
            break
    time.sleep(5)
