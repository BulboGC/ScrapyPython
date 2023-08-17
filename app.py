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
        self.USER = 'seuemail@email.com'
        self.PASSWORD = 'suasenha'
        
        self.SITE_LIST_CITY = [
            'JAÚ - SP',

            'CIANORTE - PR'
           
        ]
        
        self.SITE_PATH_ARQUIVO_CSV = 'G:\\python scrapy\\'
        self.SITE_MAP = {
            'dados': {
                'habitantes': {'xpath': '/html/body/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div/table/tbody/tr[$$NUMBER$$]/td[2]'},
                'cabecalho':{'xpath':'/html/body/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div/table/thead/tr/th[2]'},
                'popfixa':{'xpath':'/html/body/div[3]/div/div[3]/div[1]/div[1]/div[3]/div[2]/table/tbody/tr[4]/td[3]'},
                'setor_popfixa':{'xpath':'/html/body/div[3]/div[1]/div[3]/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[4]/td[3]'},
                                   
                'popflu':{'xpath' :'/html/body/div[3]/div/div[3]/div[1]/div[1]/div[3]/div[2]/table/tbody/tr[4]/td[3]'},
                'habitantes':{'xpath':'/html/body/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div/table/tbody/tr[$$NUMBER$$]/td[2]'},

                'quantidade_bairros':{'xpath':'//*[@id="t_micro_ranking_info"]'},
                'setor_regiao':{'xpath':'/html/body/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div/table/tbody/tr[$$NUMBER$$]/td[2]/a'},               
                'setor_habitantes':{'xpath':'/html/body/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div/table/tbody/tr[$$NUMBER$$]/td[3]'},
               

                'setor_explorar_regiao':{'xpath':'/html/body/div[3]/div[1]/div[3]/div[2]/div[18]/div/div/div[2]/div[2]/div/div[4]/div/div/div/div[1]/div/div/div/p[1]/a'},
                'setor_explorar_regiao2':{'xpath':'/html/body/div[3]/div/div[3]/div[2]/div[20]/div/div/div[2]/div[2]/div/div[4]/div/div/div/div[1]/div/div/div/p[1]/a'}
                                                    
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
                'consumo':{'xpath':'//*[@id="mytabs"]/li[3]/a'},               
                'setor_consumo':{'xpath':'/html/body/div[3]/div[1]/div[1]/div[3]/ul/li[2]/a'},
                
                'vestuario':{'xpath':'/html/body/div[3]/div[1]/div[3]/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[3]/td[1]/span/a'},
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
    
    def Loop_Setores(self,url,CITY):
        i = 1
        arr = [] 
        #PEGAR OS 4 PRIMEIROS BAIRROS COM O VALOR MAIS ALTO        
        for i in range(1,5):
            
            cont_setores = 1
            try:
                obj = {}
                self.OpenLink(url)
                
                # COLETAR NOME DA CIDADE 
                obj['nome_cidade']  = CITY
                
                #COLETAR NOME DO BAIRRO
                try:
                    obj['nome_bairro'] = self.Coletar_Content_value(self.SITE_MAP['buttons']['bairro']['xpath'].replace("$$NUMBER$$",str(i)))
                except:
                    obj['nome_bairro'] = 'erro'
                
                # COLETAR NUMERO DE HABITANTES DO BAIRRO    
                try:
                    obj['numero_habitantes'] = self.Coletar_Content_value(self.SITE_MAP['dados']['habitantes']['xpath'].replace("$$NUMBER$$",str(i)))
                except:
                    obj['numero_habitantes'] = ''     
                    
                # ENTRAR DENTRO DO BAIRRO
                self.Clicar(self.SITE_MAP['buttons']['bairro']['xpath'].replace("$$NUMBER$$",str(i)))
                self.Clicar(self.SITE_MAP['buttons']['explorarbairro']['xpath'])
                
                # COLETAR URL SEM A DIVISÃO DE CONSUMO, SOMENTE POR HABITANTES
                url_setores = self.browser.current_url.replace('calor=1.01.03.06&','')
                
                contador_erros = 0
                acabou = False
                
                while True:
                    
                    objetoFinal =  {}
                    setor_obj = {}
                    self.OpenLink(url_setores)
                    try:
                    
                        # COLETAR NOME DO SETOR
                        try:
                            setor_obj['setor_nome'] = self.Coletar_atributo(self.SITE_MAP['dados']['setor_regiao']['xpath'].replace('$$NUMBER$$',str(cont_setores)),'text')
                        except:                           
                            if contador_erros <= 3:
                                setor_obj['setor_nome'] = f'erro no setor de numero {str(cont_setores)}'
                            if contador_erros > 3:
                                break 
                            contador_erros = contador_erros + 1
                            

                        # COLETAR NUMERO DE HABITANTES DO SETOR
                        try:
                            setor_obj['setor_habitantes'] = self.Coletar_Content_value(self.SITE_MAP['dados']['setor_habitantes']['xpath'].replace('$$NUMBER$$',str(cont_setores)))
                        except:
                            setor_obj['setor_habitantes'] =  f'erro no setor de numero {str(cont_setores)}'

                        # ENTRAR NOS SETORES(EXPLORAR REGIÃO)
                        self.Clicar(self.SITE_MAP['dados']['setor_regiao']['xpath'].replace('$$NUMBER$$',str(cont_setores)))
                        try:
                            self.Clicar(self.SITE_MAP['dados']['setor_explorar_regiao']['xpath'].replace('$$NUMBER$$',str(cont_setores)))
                        except:
                            self.Clicar(self.SITE_MAP['dados']['setor_explorar_regiao2']['xpath'].replace('$$NUMBER$$',str(cont_setores))) 
                        # PEGAR OS DADOS

                        self.Clicar(self.SITE_MAP['buttons']['setor_consumo']['xpath'])
                        self.Clicar(self.SITE_MAP['buttons']['vestuario']['xpath'])
                        
                        try:
                            setor_obj['pop_fixa'] = self.Coletar_Content_value(self.SITE_MAP['dados']['setor_popfixa']['xpath'])
                        except:
                            setor_obj['pop_fixa'] = ' '

                        self.Clicar(self.SITE_MAP['buttons']['popflu']['xpath'])

                        try:
                             setor_obj['pop_flu'] = self.Coletar_Content_value(self.SITE_MAP['dados']['setor_popfixa']['xpath'])
                        except:
                            setor_obj['pop_flu'] = ' '

                        # ENVIANDO DADOS A UM ARRAY
                        objetoFinal= {**obj, **setor_obj}
                        print(objetoFinal)
                        arr.append(objetoFinal)
                        cont_setores = cont_setores + 1
                        
                    except:
                        if setor_obj['setor_nome'] == f'erro no setor de numero {str(cont_setores)}':
                            cont_setores = cont_setores + 1
                            contador_erros = contador_erros + 1
                        else:
                            objetoFinal= {**obj, **setor_obj}
                            print(objetoFinal)
                            arr.append(objetoFinal)
                            cont_setores = cont_setores + 1
                            contador_erros = contador_erros + 1
                    
                    
                    if contador_erros >= 3:
                            acabou = True 
                            
                        
                    
                    
                
                    
                
            except:
              
                objetoFinal = {**obj, **setor_obj}
                print(objetoFinal)
                arr.append(objetoFinal)
                cont_setores = cont_setores + 1  
        return arr
            
                    
   
    
    




            
Firefox = Scrap()

wait = WebDriverWait(Firefox.browser,5)


Firefox.OpenLink(Firefox.SITE_LINK)
Firefox.Login(Firefox.USER,Firefox.PASSWORD)
all_data = pd.DataFrame()

for CITY in tqdm(Firefox.SITE_LIST_CITY,'Regiões coletadas'):
    Firefox.OpenLink('https://app.economapas.com.br/index')



  

    
    try:
        cidade_tratada = CITY.replace(' ','+')
        url = f'https://app.economapas.com.br/mapas?calor=1.01.03.06&verifica=1&lat_lng_trava=0&filtro=all&tipo_area=bairros&n_municipio={cidade_tratada}'
   
        
        Firefox.DATABASE = Firefox.Loop_Setores(url,CITY)     
        
    except:
        ...    
    
    DF = pd.DataFrame(data=Firefox.DATABASE)
    all_data = all_data.append(DF, ignore_index=True) 
    all_data.to_excel(f'Setores_{CITY}.xlsx',index=False)
    Firefox.DATABASE = []
   
        
    

Firefox.browser.close()

    

    







