from behave import when, then, given
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time


@given(u'Ingreso al sistema en su apartado de registro')
def step_impl(context):
    driver = webdriver.Chrome()
    driver.get('http://127.0.0.1:8000/usuarios/register/')
    context.driver = driver


@given(u'escribir el nombre de usuario "{usuario}", mi correo "{correo}", la contraseña "{contra}", y repito mi contraseña "{contra}"')
def step_impl(context, usuario, correo, contra):
    context.driver.find_element(By.NAME, 'username').send_keys(usuario)
    context.driver.find_element(By.NAME, 'email').send_keys(correo)
    context.driver.find_element(By.NAME, 'password1').send_keys(contra)
    context.driver.find_element(By.NAME, 'password2').send_keys(contra)


@when(u'presiono el botón Registrase')
def step_impl(context):
    context.driver.find_element(By.ID, 'submit').click()


@then(u'puedo ver la pantalla de login.')
def step_impl(context):
    home_screen_element = context.driver.find_element(
        By.XPATH, '/html/body/div/div[2]/div/div/div/div/div/small')
    assert home_screen_element.is_displayed(), "Sign in with credentials"
