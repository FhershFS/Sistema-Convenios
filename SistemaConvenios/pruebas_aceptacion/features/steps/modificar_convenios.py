import time
from behave import when, then, given
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select


@given(u'veo la pagina de login')
def step_impl(context):
    driver = webdriver.Chrome()
    driver.set_window_size(1366, 768)
    driver.get('http://127.0.0.1:8000/usuarios/login/')
    context.driver = driver


@given(u'redacto el usuario "{usuario}" y la contrasenia "{contra}"')
def step_impl(context, usuario, contra):
    context.driver.find_element(By.NAME, 'username').send_keys(usuario)
    context.driver.find_element(By.NAME, 'password').send_keys(contra)


@when(u'hago clic en el botón identificarse')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="submit"]').click()
    time.sleep(2)


@when(u'puedo visualizar la página de inicio')
def step_impl(context):
    home_screen_element = context.driver.find_element(
        By.XPATH, '//*[@id="panel"]/h1')
    assert home_screen_element.is_displayed(), "Home screen not displayed"


@when(u'hago clic en alguna de las categoria de los convenios')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '/html/body/nav/div/div[2]/div/ul[1]/li[2]').click()
    time.sleep(2)


@when(u'hago click en el boton + persona')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div[2]/a[5]').click()
    time.sleep(2)


@when(u'redacto el nombre "{nombre}"')
def step_impl(context, nombre):
    context.driver.find_element(By.NAME, 'nombre').send_keys(nombre)
    time.sleep(2)


@when(u'hago click en save en la persona')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '//*[@id="panel"]/div/form/button').click()
    time.sleep(2)


@when(u'hago click nuevamente la categoria del convenio')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '/html/body/nav/div/div[2]/div/ul[1]/li[2]').click()
    time.sleep(2)


@when(u'hago click en el boton + unidad academica')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div[2]/a[3]').click()
    time.sleep(2)


@when(u'redactoo el nombre "{nombre}"')
def step_impl(context, nombre):
    context.driver.find_element(By.NAME, 'nombre').send_keys(nombre)
    time.sleep(2)


@when(u'hago click en save en la unidad academica')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '//*[@id="panel"]/div/form/button').click()
    time.sleep(2)


@when(u'hago click por ultima vez la categoria del convenio')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '/html/body/nav/div/div[2]/div/ul[1]/li[2]').click()
    time.sleep(2)


@when(u'hago clic el botón +Convenio')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div[2]/a[1]').click()
    time.sleep(2)


@when(u'redacto el número "{numero}"')
def step_impl(context, numero):
    context.driver.find_element(By.NAME, 'numero').send_keys(numero)


@when(u'redacto el tipo diversas instituciones')
def step_impl(context):
    context.driver.find_element(By.ID, "id_tipo_0").click()


@when(u'selecciono la persona')
def step_impl(context):
    select = Select(context.driver.find_element(By.NAME, "persona_tramito"))
    select.select_by_index(1)


@when(u'selecciono la unidad')
def step_impl(context):
    select = Select(context.driver.find_element(By.NAME, "unidad_academica"))
    select.select_by_index(1)


@when(u'hago clic en save convenio')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '//*[@id="panel"]/div/form/button').click()
    time.sleep(2)


@when(u'por utimizima vez hago click en la categoria del convenio')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '/html/body/nav/div/div[2]/div/ul[1]/li[2]').click()
    time.sleep(2)


@when(u'hago clic en el boton con el simbolo de mas a la derecha del convenio')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '/html/body/a/div/table/tbody/tr/td[8]/div/a[3]').click()
    time.sleep(2)


@when(u'modifico el campo numero con "{numero}"')
def step_impl(context, numero):
    context.driver.find_element(By.NAME, 'numero').send_keys(numero)


@when(u'hago click en save')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '//*[@id="panel"]/div/form/button').click()
    time.sleep(2)


@then(u'recibo el mensaje "{mensaje}"')
def step_impl(context, mensaje):
    assert mensaje in context.driver.page_source
    # Eliminar convenio
    context.driver.find_element(
        By.XPATH, '/html/body/nav/div/div[2]/div/ul[1]/li[2]').click()
    context.driver.find_element(
        By.XPATH, '/html/body/a/div/table/tbody/tr/td[8]/div/a[1]').click()
    context.driver.find_element(
        By.XPATH, '//*[@id="panel"]/div/form/button').click()
    time.sleep(2)
