# Generated by Selenium IDE

# 1- Importar Bibliotecas / Pacotes

import pytest                                   # Framework de Teste de Unidade / Engine / Motor
import time                                     # Controle do Tempo
import json                                     # Ler e Escrever no formato JSON
from selenium import webdriver                  # Bibliotecas do Selenium webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# 2- Classes e Definições

class TestConsultaMantis():
    def setup_method(self, method):
        #Instanciar o objeto do Selenium WebDriver como Chrome
        self.driver = webdriver.Chrome('C:/Users/aless/PycharmProjects/Cursos_Iterasys/FTS132/drivers/chrome/versao_96/chromedriver.exe')
        self.driver.implicitly_wait(30)  # O robô (selenium) irá esperar por até 30 segundos pelos elementos, realizando tentativas de 1 em 1 segundo
        self.driver.maximize_window()    # Maximizar a janela do navegador
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_consultaMantis(self):
        self.driver.get("https://iterasys.com.br/plataforma/home/index.php?action=initial")
        self.driver.set_window_size(1552, 840)
        self.driver.find_element(By.ID, "searchtext").click()
        self.driver.find_element(By.ID, "searchtext").send_keys("mantis")
        self.driver.find_element(By.ID, "btn_form_search").click()
        self.driver.find_element(By.CSS_SELECTOR, ".comprar").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".item-title").text == "Mantis"
        assert self.driver.find_element(By.CSS_SELECTOR, ".new-price").text == "R$ 59,99"
