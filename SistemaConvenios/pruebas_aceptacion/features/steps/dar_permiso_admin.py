import time
from behave import when, then, given
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@when(u'Presiono en administrar usuarios')
def step_impl(context):
    # Espera hasta que el elemento sea visible y clickeable
    element = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="sidenav-collapse-main"]/ul[2]/li/a'))
    )

    action = ActionChains(context.driver)
    action.move_to_element(element).click().perform()


@when(u'presiono el botón de cambiar permisos al primer usuario')
def step_impl(context):
    # Espera hasta que el elemento sea visible y clickeable
    element = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'btn'))
    )

    action = ActionChains(context.driver)
    action.move_to_element(element).click().perform()


@when(u'selecciono el grupo de admin')
def step_impl(context):
    context.select = Select(context.driver.find_element(By.NAME, 'groups'))
    context.select.select_by_index(1)


@when(u'presiono guardar')
def step_impl(context):
    element = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="panel"]/div/form/input[2]'))
    )

    action = ActionChains(context.driver)
    action.move_to_element(element).click().perform()


@when(u'cierro sesión')
def step_impl(context):
    context.driver.find_element(By.CLASS_NAME, 'ni-user-run').click()


@when(u'ingreso al login')
def step_impl(context):
    context.driver.get('http://127.0.0.1:8000/usuarios/login/')


@when(u'Escribo el usuario "{usuario}" y la contraseña "{contra}"')
def step_impl(context, usuario, contra):
    context.driver.find_element(By.NAME, 'username').send_keys(usuario)
    context.driver.find_element(By.NAME, 'password').send_keys(contra)


@then(u'puedo ver la seccion "{seccion}"')
def step_impl(context, seccion):
    elementos = context.driver.find_elements(By.CLASS_NAME, 'nav-link-text')

    textos = []

    for elemento in elementos:
        texto = elemento.text
        textos.append(texto)

    assert seccion in textos
