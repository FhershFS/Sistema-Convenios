from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


@when(u'selecciono el grupo de movilidad')
def step_impl(context):
    context.select = Select(context.driver.find_element(By.NAME, 'groups'))
    context.select.select_by_index(3)
