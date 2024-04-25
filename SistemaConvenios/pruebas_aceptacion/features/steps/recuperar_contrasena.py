from behave import when, then, given
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time


@given(u'Ingreso a la pantalla para recuperar contraseña')
def step_impl(context):
    driver = webdriver.Chrome()
    driver.get('http://127.0.0.1:8000/usuarios/reset_password/')
    context.driver = driver


time.sleep(5)


@given(u'ingrese un correo electrónico reviamente registrado en el sistema "{correo}"')
def step_impl(context, correo):
    context.driver.find_element(By.NAME, 'email').send_keys(correo)


time.sleep(5)


@given(u'presiono el boton para resetear password')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '//*[@id="content"]/form/fieldset/input').click()


@when(u'cuando entre a mi correo electrónico con mis datos "{correo}" y mi contraseña "{contra}"')
def step_impl(context, correo, contra):
    driver = webdriver.Chrome()
    driver.get('https://login.live.com/login.srf')
    email = driver.find_element(By.NAME, 'loginfmt')
    email.send_keys(correo + Keys.RETURN)
    time.sleep(5)
    contrasenia = driver.find_element(By.NAME, 'passwd')
    contrasenia.send_keys(contra + Keys.RETURN)
    time.sleep(5)
    driver.find_element(By.ID, 'idSIButton9').click()
    time.sleep(5)
    driver.find_element(By.ID, 'id__24').click()
    time.sleep(5)
    url_actual = driver.current_url
    time.sleep(5)
    ventanas = driver.window_handles
    driver.switch_to.window(ventanas[-1])
    url_actual = driver.current_url
    time.sleep(5)
    context.driver = driver


@then(u'entonces encontrare un correo de "{correo}"')
def step_impl(context, correo):
    context.driver
    assert context.driver.find_element(By.CSS_SELECTOR, f'[title="{correo}"]')
