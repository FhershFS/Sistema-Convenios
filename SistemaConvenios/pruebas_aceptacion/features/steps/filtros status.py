import time
from time import sleep
from behave import when, then, given
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


@given(u'que inicio en el sistema')
def step_impl(context):
    driver = webdriver.Chrome()
    driver.get('http://127.0.0.1:8000/usuarios/login/')
    context.driver = driver


@given(u'pongo el nombre "{usuario}" y su contraseña: "{contra}"')
def step_impl(context, usuario, contra):
    context.driver.find_element(By.NAME, 'username').send_keys(usuario)
    context.driver.find_element(By.NAME, 'password').send_keys(contra)


@given(u'oprimo para dentificarme')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="submit"]').click()


@given(u'veo el inicio del sistema')
def step_impl(context):

    home_screen_element = context.driver.find_element(
        By.XPATH, '//*[@id="panel"]/h1')
    assert home_screen_element.is_displayed(), "Home screen not displayed"


@given(u'presiono alguna de las categoria de convenios')
def step_impl(context):
    # Espera hasta que el elemento sea visible y clickeable
    element = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'btn-dvst'))
    )

    # Utiliza ActionChains para realizar una acción de clic con un pequeño desplazamiento
    action = ActionChains(context.driver)
    action.move_to_element(element).click().perform()

    time.sleep(3)


@given(u'puedo ver en la pantalla de convenios los de esa categoria')
def step_impl(context):
    # Implementa el código necesario para verificar que se vea la pantalla de convenios
    home_screen_element = context.driver.find_element(
        By.XPATH, '//*[@id="panel"]/h3')
    assert home_screen_element.is_displayed(), "Home screen not displayed"


time.sleep(5)


@given(u'presiono el botón para los filtros')
def step_impl(context):
    # Espera hasta que el elemento sea visible y clickeable
    element = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="btnFiltros"]'))
    )

    # Utiliza ActionChains para realizar una acción de clic con un pequeño desplazamiento
    action = ActionChains(context.driver)
    action.move_to_element(element).click().perform()
    sleep(3)


@given(u'selecciono la status "{status}"')
def step_impl(context, status):
    # Encuentra el elemento select por su id
    select_element = context.driver.find_element(By.ID, 'status')

    # Usa la clase Select para interactuar con el elemento select
    select = Select(select_element)

    # Selecciona la opción por su texto visible (en este caso, la variable persona ya es la cadena correcta)
    select.select_by_visible_text(status)

    # Puedes esperar un tiempo opcional si es necesario
    sleep(3)


@when(u'presiono en Buscar')
def step_impl(context):
    # Espera hasta que el elemento sea visible y clickeable
    element = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="filtrosContainer"]/div[7]/button'))
    )

    # Utiliza ActionChains para realizar una acción de clic con un pequeño desplazamiento
    action = ActionChains(context.driver)
    action.move_to_element(element).click().perform()


@then(u'puedo ver el convenio con su status "{clave}" en la tabla de convenios')
def step_impl(context, clave):
    # Espera hasta 10 segundos para que la tabla aparezca
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/a/div/table'))
    )

    tabla = context.driver.find_element(By.XPATH, '/html/body/a/div/table')
    tbody = tabla.find_element(By.TAG_NAME, 'tbody')
    rows = tbody.find_elements(By.TAG_NAME, 'tr')

    for row in rows:
        # Espera hasta 10 segundos para que la quinta celda aparezca
        sexta_celda = WebDriverWait(row, 10).until(
            EC.presence_of_element_located((By.XPATH, 'td[7]'))
        )

        # Verifica si el texto en la sexta celda coincide con la clave
        if sexta_celda.text == clave:
            # Muestra un mensaje si encuentra la clave
            print(
                f"Se encontró la clave '{clave}' en la septima columna de la tabla.")
            break
    time.sleep(5)


@then(u'Veo: "No se encontraron resultados."')
def step_impl(context):
    # Espera hasta 10 segundos para que el mensaje aparezca
    mensaje_element = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//h1[contains(text(), "No se encontraron resultados.")]'))
    )
    assert mensaje_element.is_displayed(
    ), "No se encontró el mensaje 'No se encontraron resultados.' en la pantalla"

    sleep(5)
