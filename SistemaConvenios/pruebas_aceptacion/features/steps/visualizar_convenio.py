import time
from behave import when, then, given
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select


@given(u'que puedo apreciar el login')
def step_impl(context):
    driver = webdriver.Chrome()
    driver.set_window_size(1366, 768)
    driver.get('http://127.0.0.1:8000/usuarios/login/')
    context.driver = driver


@given(u'transcribo el usuario "{usuario}" y la contraseña "{contra}"')
def step_impl(context, usuario, contra):
    context.driver.find_element(By.NAME, 'username').send_keys(usuario)
    context.driver.find_element(By.NAME, 'password').send_keys(contra)


@when(u'clickeo el botón identificarse')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="submit"]').click()
    time.sleep(2)


@when(u'puedo mirar la página de inicio')
def step_impl(context):
    home_screen_element = context.driver.find_element(
        By.XPATH, '//*[@id="panel"]/h1')
    assert home_screen_element.is_displayed(), "Home screen not displayed"


@when(u'clickeo alguna de las categoria de los convenios')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '/html/body/nav/div/div[2]/div/ul[1]/li[2]').click()
    time.sleep(2)


@when(u'cliceko el boton + persona')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div[2]/a[5]').click()
    time.sleep(2)


@when(u'transcribo el nombre "{nombre}"')
def step_impl(context, nombre):
    context.driver.find_element(By.NAME, 'nombre').send_keys(nombre)
    time.sleep(2)


@when(u'cliceko save en la persona')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '//*[@id="panel"]/div/form/button').click()
    time.sleep(2)


@when(u'clickeo nuevamente la categoria del convenio')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '/html/body/nav/div/div[2]/div/ul[1]/li[2]').click()
    time.sleep(2)


@when(u'clickeo en el boton + unidad academica')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div[2]/a[3]').click()
    time.sleep(2)


@when(u'transcriboo el nombre "{nombre}"')
def step_impl(context, nombre):
    context.driver.find_element(By.NAME, 'nombre').send_keys(nombre)
    time.sleep(2)


@when(u'clickeo save en la categoria')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '//*[@id="panel"]/div/form/button').click()
    time.sleep(2)


@when(u'clickeo otra vez la categoria del convenio')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '/html/body/nav/div/div[2]/div/ul[1]/li[2]').click()
    time.sleep(2)


@when(u'clickeo el botón +Convenio')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div[2]/a[1]').click()
    time.sleep(2)


@when(u'transcribo el número "{numero}"')
def step_impl(context, numero):
    context.driver.find_element(By.NAME, 'numero').send_keys(numero)


@when(u'transcribo el tipo diversas instituciones')
def step_impl(context):
    context.driver.find_element(By.ID, "id_tipo_0").click()


@when(u'transcribo la persona')
def step_impl(context):
    select = Select(context.driver.find_element(By.NAME, "persona_tramito"))
    select.select_by_index(1)


@when(u'transcribo la unidad')
def step_impl(context):
    select = Select(context.driver.find_element(By.NAME, "unidad_academica"))
    select.select_by_index(1)


@when(u'clickeo save')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '//*[@id="panel"]/div/form/button').click()
    time.sleep(2)


@when(u'clickeo por ultima vez la categoria del convenio')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '/html/body/nav/div/div[2]/div/ul[1]/li[2]').click()
    time.sleep(2)


@when(u'clickeo el boton con el icono de ojo a la derecha del convenio')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '/html/body/a/div/table/tbody/tr/td[8]/div/a[5]').click()
    time.sleep(2)


@then(u'observo los datos del convenio, cuyo primero campo es "{campo}"')
def step_impl(context, campo):
    assert campo in context.driver.page_source
    context.driver.find_element(
        By.XPATH, '/html/body/nav/div/div[2]/div/ul[1]/li[2]').click()
    context.driver.find_element(
        By.XPATH, '/html/body/a/div/table/tbody/tr/td[8]/div/a[1]').click()
    context.driver.find_element(
        By.XPATH, '//*[@id="panel"]/div/form/button').click()
    time.sleep(2)
