from selenium import webdriver
from openpyxl import Workbook
import pandas as pd
from tqdm import tqdm
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
import time



class Scrap:
    def __init__(self):
        self.DATABASE = []
        self.SITE_LINK = "https://app.economapas.com.br/login"
        self.USER = 'pesquisa@iemi.com.br'
        self.PASSWORD = 'Iemi270122'
        
    
        self.SITE_LIST_CITY = [
                    'AMERICANA - SP',
                'PORTO ALEGRE - RS',
          
              'VITÓRIA - ES',
         
            
            
          
            'VILA VELHA - ES',
            'JUIZ DE FORA - MG',
            'SÃO JOSÉ DO RIO PRETO - SP'



            ]
        
        self.SITE_PATH_ARQUIVO_CSV = 'G:\\python scrapy\\'
        self.SITE_MAP = {
            'dados': {
                'habitantes': {'xpath': '/html/body/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div/table/tbody/tr[$$NUMBER$$]/td[2]'},
                'cabecalho':{'xpath':'/html/body/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div/table/thead/tr/th[2]'},
                'popfixa':{'xpath':'/html/body/div[3]/div/div[3]/div[1]/div[1]/div[3]/div[2]/table/tbody/tr[4]/td[3]'},
                'popflu':{'xpath' :'/html/body/div[3]/div/div[3]/div[1]/div[1]/div[3]/div[2]/table/tbody/tr[4]/td[3]'},
                'habitantes':{'xpath':'/html/body/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div/table/tbody/tr[$$NUMBER$$]/td[2]'},
                'quantidade_bairros':{'xpath':'//*[@id="t_micro_ranking_info"]'}
            },
            'inputs': {
                'user': {'xpath': '//*[@id="email"]'},
                'password': {'xpath': '//*[@id="password"]'},
                'src_input':{'xpath':'//*[@id="i_municipio"]'}
            },
            'buttons': {
                'btlogin': {'xpath': '/html/body/main/form/button'},
                'src_bt':{'xpath':'/html/body/div[3]/div[1]/form/div/span[2]/button/span'},
                'explorarbairro':{'xpath':'//*[@id="i_mapa"]/div/div/div[2]/div[2]/div/div[4]/div/div/div/div[1]/div/div/div/p/a'},
                'abrirpopup':{'xpath':'/html/body/div[3]/div[1]/div[1]/div[1]/div/button/span[1]'},
                'visaodebairro':{'xpath':'/html/body/div[3]/div[1]/div[1]/div[1]/div/div/form/button'},
                #'consumo':{'xpath':'/html/body/div[3]/div/div[1]/div[3]/ul/li[3]/a'},
                'consumo':{'xpath':'//*[@id="mytabs"]/li[3]/a'},
                'vestuario':{'xpath':'/html/body/div[3]/div[1]/div[3]/div[1]/div[1]/div[3]/div[2]/table/tbody/tr[3]/td[1]/span/a'},
                'bairro':{'xpath':'/html/body/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div/table/tbody/tr[$$NUMBER$$]/td[1]/p/a'} ,
                'popflu':{'xpath':'//*[@id="alterna_exibicao_flutuante"]'}
            },
        }
     
 
      
       
        option = Options()
        option.headless = True
        option.add_argument('window-size=1400,600')
    
        self.browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),options=option)
        self.browser.maximize_window()
       
    
    def Login(self,user,password):
        wait.until(EC.presence_of_element_located((By.XPATH,self.SITE_MAP['inputs']['user']['xpath'])))
        self.browser.find_element(by='xpath',value=self.SITE_MAP['inputs']['user']['xpath']).send_keys(user)
        self.browser.find_element(by='xpath', value=self.SITE_MAP['inputs']['password']['xpath']).send_keys(password)
        self.Clicar(self.SITE_MAP['buttons']['btlogin']['xpath'])
    
    def OpenLink(self,link):
        self.browser.get(link)
     

    def Src(self,name,element):
        wait.until(EC.presence_of_element_located((By.XPATH, element)))
        self.browser.find_element(by='xpath',value=element).send_keys(name)
  
       

    def Clicar(self,element):
        wait.until(EC.presence_of_element_located((By.XPATH,element)))
        self.browser.find_element(by='xpath',value= element).click()
        
       

    def Coletar_Content_value(self,element):
        wait.until(EC.presence_of_element_located((By.XPATH,element)))
        return self.browser.find_element(by='xpath',value=element).text


    def Digitar_input(self,element,texto):
        self.browser.find_element(by='xpath',value=element).send_keys(texto)
        time.sleep(1000)
        self.browser.find_element(by='xpath',value=element).send_keys(Keys.ENTER)
        
       
         
    def Coletar_atributo(self,element,atributo):
        wait.until(EC.presence_of_element_located((By.XPATH,element)))
        return self.browser.find_element(by='xpath',value=element).get_attribute(atributo)
   
    def Loop_coleta(self,url):       
        i = 1
        arr = []
        acabou = False
        contador_erros = 0
       
        while True:
            try:
                obj = {}
                self.OpenLink(url)
                Firefox.Clicar(Firefox.SITE_MAP['buttons']['abrirpopup']['xpath'])  
                
                try:
                    
                    if self.Coletar_Content_value(Firefox.SITE_MAP['buttons']['visaodebairro']['xpath']) == 'Visão Bairros':
                        Firefox.Clicar(Firefox.SITE_MAP['buttons']['visaodebairro']['xpath'])             
                    
                except:
                    ...
                    
                obj['nome_cidade']  = CITY
                obj['nome_bairro'] = self.Coletar_Content_value(Firefox.SITE_MAP['buttons']['bairro']['xpath'].replace("$$NUMBER$$",str(i)))
                obj['numero_habitantes'] = self.Coletar_Content_value(Firefox.SITE_MAP['dados']['habitantes']['xpath'].replace("$$NUMBER$$",str(i)))
                
                
                self.Clicar(self.SITE_MAP['buttons']['bairro']['xpath'].replace("$$NUMBER$$",str(i)))
                
                
                
                self.Clicar(self.SITE_MAP['buttons']['explorarbairro']['xpath'])
                
                self.Clicar(self.SITE_MAP['buttons']['consumo']['xpath'])  
                self.Clicar(self.SITE_MAP['buttons']['vestuario']['xpath'])
                
                obj['gasto_população_fixa'] = self.Coletar_Content_value(Firefox.SITE_MAP['dados']['popfixa']['xpath'].replace("$$NUMBER$$",str(i)))
                
                self.Clicar(self.SITE_MAP['buttons']['popflu']['xpath'])
                
                obj['gasto_população_flutuante'] = self.Coletar_Content_value(Firefox.SITE_MAP['dados']['popfixa']['xpath'].replace("$$NUMBER$$",str(i)))
                
                
                i = i + 1
                arr.append(obj)
                print(obj)
            except Exception as e:
                contador_erros = contador_erros + 1
                i = i + 1  
                if contador_erros >= 8:
                    acabou = True 
                
            if acabou == True:
                return  arr
               
            
   
    
    




            
Firefox = Scrap()

wait = WebDriverWait(Firefox.browser,5)


Firefox.OpenLink(Firefox.SITE_LINK)
Firefox.Login(Firefox.USER,Firefox.PASSWORD)
all_data = pd.DataFrame()

for CITY in tqdm(Firefox.SITE_LIST_CITY,'Regiões coletadas'):
    Firefox.OpenLink('https://app.economapas.com.br/index')



  

    # Pesquisando Cidade do loop    
    try:
        # Pesquisando a cidade
        Firefox.Src(CITY,Firefox.SITE_MAP['inputs']['src_input']['xpath'])
        Firefox.Clicar(Firefox.SITE_MAP['buttons']['src_bt']['xpath'])  

        # Abrir visão de bairros
        Firefox.Clicar(Firefox.SITE_MAP['buttons']['abrirpopup']['xpath'])  
        url = Firefox.browser.current_url
        try:
            Firefox.Clicar(Firefox.SITE_MAP['buttons']['visaodebairro']['xpath'])                         
        except:
           ...
            
        Firefox.DATABASE = Firefox.Loop_coleta(url)     
    except:
        ...    

    DF = pd.DataFrame(data=Firefox.DATABASE)
    all_data = all_data.append(DF, ignore_index=True) 
    all_data.to_excel('dados.xlsx',index=False)

Firefox.browser.close()

    

    







