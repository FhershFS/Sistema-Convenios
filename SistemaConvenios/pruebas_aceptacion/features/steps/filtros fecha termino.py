import time
from time import sleep
from behave import when, then, given
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


@given(u'el inicio sesión en el sistema')
def step_impl(context):
    driver = webdriver.Chrome()
    driver.get('http://127.0.0.1:8000/usuarios/login/')
    context.driver = driver


@given(u'ingreso nombre de usuario: "{usuario}" y la contraseña: "{contra}"')
def step_impl(context, usuario, contra):
    context.driver.find_element(By.NAME, 'username').send_keys(usuario)
    context.driver.find_element(By.NAME, 'password').send_keys(contra)


@given(u'oprimo el botón para iniciar en el sistema')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="submit"]').click()


@given(u'veo la pantalla inicial del sistema')
def step_impl(context):

    home_screen_element = context.driver.find_element(
        By.XPATH, '//*[@id="panel"]/h1')
    assert home_screen_element.is_displayed(), "Home screen not displayed"


@given(u'presiono una categoria de la lista en el menú')
def step_impl(context):
    # Espera hasta que el elemento sea visible y clickeable
    element = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'btn-dvst'))
    )

    # Utiliza ActionChains para realizar una acción de clic con un pequeño desplazamiento
    action = ActionChains(context.driver)
    action.move_to_element(element).click().perform()

    time.sleep(3)


@given(u'puedo ver la pantalla de convenios de esa categoria que se eligió en el menú')
def step_impl(context):
    # Implementa el código necesario para verificar que se vea la pantalla de convenios
    home_screen_element = context.driver.find_element(
        By.XPATH, '//*[@id="panel"]/h3')
    assert home_screen_element.is_displayed(), "Home screen not displayed"


time.sleep(5)


@given(u'presiono el botón de filtrar los convenios')
def step_impl(context):
    # Espera hasta que el elemento sea visible y clickeable
    element = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="btnFiltros"]'))
    )

    # Utiliza ActionChains para realizar una acción de clic con un pequeño desplazamiento
    action = ActionChains(context.driver)
    action.move_to_element(element).click().perform()


@given(u'escribo la fecha de término del convenio "{clave}"')
def step_impl(context, clave):
    context.driver.find_element(
        By.XPATH, '/html/body/div[1]/form/div/div[6]/div[1]/input').send_keys(clave)

    context.driver.find_element(
        By.XPATH, '/html/body/div[1]/form/div/div[6]/div[2]/input').send_keys(clave)

    sleep(2)


@when(u'presiono el botón para buscar algún convenio')
def step_impl(context):
    # Espera hasta que el elemento sea visible y clickeable
    element = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="filtrosContainer"]/div[7]/button'))
    )

    # Utiliza ActionChains para realizar una acción de clic con un pequeño desplazamiento
    action = ActionChains(context.driver)
    action.move_to_element(element).click().perform()


@then(u'puedo ver el convenio con fecha de término 3/12/2023 y el número de convenio "{clave}" en la tabla de convenios')
def step_impl(context, clave):
    # Espera hasta 10 segundos para que la tabla aparezca
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/a/div/table'))
    )

    tabla = context.driver.find_element(By.XPATH, '/html/body/a/div/table')
    tbody = tabla.find_element(By.TAG_NAME, 'tbody')
    rows = tbody.find_elements(By.TAG_NAME, 'tr')

    claves = []

    for row in rows:
        # Espera hasta 10 segundos para que la celda de la clave aparezca
        clave_element = WebDriverWait(row, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'td'))
        )
        id = clave_element.text
        claves.append(id)

    assert clave in claves

    sleep(5)


@then(u'se muestra el mensaje siguiente: "No se encontraron resultados."')
def step_impl(context):
    # Espera hasta 10 segundos para que el mensaje aparezca
    mensaje_element = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//h1[contains(text(), "No se encontraron resultados.")]'))
    )
    assert mensaje_element.is_displayed(
    ), "No se encontró el mensaje 'No se encontraron resultados.' en la pantalla"

    sleep(5)
