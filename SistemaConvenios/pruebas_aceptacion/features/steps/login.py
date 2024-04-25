from behave import when, then, given
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time


@given(u'Ingreso al sistema en su apartado de login')
def step_impl(context):
    driver = webdriver.Chrome()
    driver.get('http://127.0.0.1:8000/usuarios/login/')
    context.driver = driver


time.sleep(10)


@given(u'escribo el nombre de usuario "{usuario}" y la contraseña "{contra}"')
def step_impl(context, usuario, contra):
    context.driver.find_element(By.NAME, 'username').send_keys(usuario)
    context.driver.find_element(By.NAME, 'password').send_keys(contra)


@when(u'presiono el botón Identificarse')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="submit"]').click()


time.sleep(10)


@then(u'puedo ver el mensaje de error "{mensaje}"')
def step_impl(context, mensaje):
    resultado = context.driver.find_element(
        By.XPATH, '/html/body/div/div[2]/div/div/div/div/form/ul/li').text
    assert mensaje in resultado


@then(u'puedo verla pantalla de inicio.')
def step_impl(context):

    home_screen_element = context.driver.find_element(
        By.XPATH, '//*[@id="panel"]/h1')
    assert home_screen_element.is_displayed(), "Home screen not displayed"


time.sleep(3)
