# Web Scraping Automatizado

Este é um script Python para automatizar o processo de web scraping usando a biblioteca Selenium. O script coleta dados de um site de mapeamento econômico.

## Pré-requisitos

Certifique-se de ter as seguintes bibliotecas Python instaladas:

- `selenium`
- `openpyxl`
- `pandas`
- `tqdm`
- `webdriver_manager`

Você pode instalá-las usando o seguinte comando:

```
pip install selenium openpyxl pandas tqdm webdriver_manager
```
Como usar

Clone o repositório ou copie o código em um arquivo .py.

Abra o arquivo e edite a seção Scrap para definir suas configurações, como link do site, usuário e senha.

Certifique-se de ter o navegador Firefox instalado, pois o script utiliza o driver do Firefox.

Execute o script Python.

O script irá:
        Efetuar login no site de mapeamento econômico.
        Coletar informações de diversas cidades.
        Exportar os dados coletados em arquivos Excel.

Personalização

Você pode personalizar as cidades a serem coletadas na lista SITE_LIST_CITY.

  O código possui diversos métodos para diferentes ações, como login, abertura de links, preenchimento de campos, coleta de informações etc. Você pode adaptar ou estender esses métodos conforme necessário.

Observações

  Este script é fornecido como exemplo e pode precisar de ajustes para atender às suas necessidades específicas.

   Certifique-se de seguir as diretrizes éticas e legais ao realizar web scraping de qualquer site.

Contribuições

Contribuições são bem-vindas! Se você encontrar bugs, melhorias ou quiser adicionar mais funcionalidades, fique à vontade para abrir uma issue ou enviar um pull request.





