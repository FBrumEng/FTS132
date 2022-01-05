# 1- Importar Bibliotecas
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import pytest

caminho_print = 'C:/Users/aless/PycharmProjects/Cursos_Iterasys/FTS132/prints/' \
                + datetime.now().strftime('%Y-%m-%d %H-%M-%S') + '/'

# 2- Classe
class Test_Selenium_Webdriver:

    # Definição de inicio - Executa antes do teste
    def setup_method(self):
        # Declarar o objeto do Selenium e instanciar como o navegador desejado
        self.driver = webdriver.Chrome('C:/Users/aless/PycharmProjects/Cursos_Iterasys/FTS132/drivers/chrome/versao_96/chromedriver.exe')
        self.driver.implicitly_wait(40) # O Selenium vai esperar até 3 segs pelos elementos
        self.driver.maximize_window()  # Maximizar a janela do navegador

    # Criar a pasta com data e hora para guardar os prints
    try:
        os.mkdir(caminho_print)
    except:
        print('A pasta já existia')

    # Definição de Fim - Executa depois do teste
    def teardown_method(self):
        # Destruir o objeto do Selenium
        self.driver.quit()

    # Definição do Teste
    def testar_comprar_curso_mantis_com_click_na_lupa(self):
        # O Selenium abre a url indicada - site alvo do teste
        self.driver.get('https://www.iterasys.com.br')
        # O Selenium clica na caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').click()
        # O Selenium apaga o conteúdo da caixa de pesquisa (bug)
        self.driver.find_element(By.ID, 'searchtext').clear()
        # O Selenium escreve 'mantis' na caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').send_keys('mantis')
        # O Selenium clica no botão da Lupa
        self.driver.find_element(By.ID, 'btn_form_search').click()
        # O Selenium clica em matricule-se
        self.driver.find_element(By.CSS_SELECTOR, 'span.comprar').click()
        # O Selenium valida o nome do curso no carrinho de compras
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.item-title').text == 'Mantis'
        # O Selenium valida o preço do curso no carrinho de compras
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.new-price').text == 'R$ 59,99'

    def testar_comprar_curso_mantis_com_enter(self):
        # O Selenium abre a url indicada - site alvo do teste
        self.driver.get('https://www.iterasys.com.br')
        # O Selenium clica na caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').click()
        # O Selenium apaga o conteúdo da caixa de pesquisa (bug)
        self.driver.find_element(By.ID, 'searchtext').clear()
        # O Selenium escreve 'mantis' na caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').send_keys('mantis')
        # O Selenium pressiona a tecla Enter
        self.driver.find_element(By.ID, 'btn_form_search').send_keys(Keys.ENTER)
        # O Selenium clica em matricule-se
        self.driver.find_element(By.CSS_SELECTOR, 'span.comprar').click()
        # O Selenium valida o nome do curso no carrinho de compras
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.item-title').text == 'Mantis'
        # O Selenium valida o preço do curso no carrinho de compras
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.new-price').text == 'R$ 59,99'

    def testar_comprar_curso_ctfl_com_click_na_lupa(self):
        # O Selenium abre a url indicada - site alvo do teste
        self.driver.get('https://www.iterasys.com.br')
        # O Selenium clica na caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').click()
        # O Selenium apaga o conteúdo da caixa de pesquisa (bug)
        self.driver.find_element(By.ID, 'searchtext').clear()
        # O Selenium escreve 'mantis' na caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').send_keys('ctfl')
        # O Selenium clica no botão da Lupa
        self.driver.find_element(By.ID, 'btn_form_search').click()
        # O Selenium clica em matricule-se
        self.driver.find_element(By.CSS_SELECTOR, 'span.comprar').click()
        # O Selenium valida o nome do curso no carrinho de compras
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.item-title').text == 'Preparatório CTFL'
        # O Selenium valida o preço do curso no carrinho de compras
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.new-price').text == 'R$ 199,00'

    # Data driven tests - a partir da massa de dados criada
    @pytest.mark.parametrize('id, termo, curso, preco',[
        ('1', 'mantis', 'Mantis', 'R$ 59,99'),
        ('2', 'ctfl', 'Preparatório CTFL', 'R$ 199,00'),
    ])

    def testar_comprar_curso_mantis_com_click_na_lupa(self, id, termo, curso, preco):
        # O Selenium abre a url indicada - site alvo do teste
        self.driver.get('https://www.iterasys.com.br')
        self.driver.get_screenshot_as_file(f'{caminho_print}teste {id}_passo1_home.png')
        # O Selenium clica na caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').click()
        # O Selenium apaga o conteúdo da caixa de pesquisa (bug)
        self.driver.find_element(By.ID, 'searchtext').clear()
        # O Selenium escreve 'mantis' na caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').send_keys(termo)
        self.driver.get_screenshot_as_file(f'{caminho_print}teste {id}_passo2_pesquisa_pelo_curso.png')
        # O Selenium clica no botão da Lupa
        self.driver.find_element(By.ID, 'btn_form_search').click()
        # O Selenium clica em matricule-se
        self.driver.find_element(By.CSS_SELECTOR, 'span.comprar').click()
        # O Selenium valida o nome do curso no carrinho de compras
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.item-title').text == curso
        # O Selenium valida o preço do curso no carrinho de compras
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.new-price').text == preco