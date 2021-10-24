import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Test_WebDriver():
    def setup_method(self, method):
        self.driver = webdriver.Chrome('drivers/chrome/94/chromedriver.exe')
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_consultar_curso_free(self):
        self.driver.get('https://www.iterasys.com.br')

    # Página 01 - Home
        self.driver.find_element(By.ID, 'searchtext').click()
        self.driver.find_element(By.ID, 'searchtext').clear()
        self.driver.find_element(By.ID, 'searchtext').send_keys('python')
        self.driver.find_element(By.ID, 'btn_form_search').click()

    # Página 02 - Acessar
        self.driver.find_element(By.CSS_SELECTOR, 'span.acessar').click()

    # Página 03 - Validar Modal Cadastro Rápido
        self.driver.find_element(By.ID, 'cadastro-rapido').click()
        wait = WebDriverWait(self.driver, 3)
        assert self.driver.find_element(By.CSS_SELECTOR, 'h4.modal-title').text == 'Cadastro Rápido'
        assert self.driver.find_element(By.ID, 'btn_form_cad_cr').text == 'Cadastre-se'
