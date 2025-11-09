# Scraper Reclame Aqui

## Objetivo

O script automatiza a navegação no site Reclame Aqui para extrair dados da categoria "Casa de Aposta". Ele coleta as "Melhores" e "Piores" empresas e extrai as seguintes métricas:

  * Nota
  * Reclamações respondidas (%)
  * Voltariam a fazer negócio (%)
  * Índice de solução (%)

Os dados coletados são salvos em uma planilha Excel.

## Tecnologias

  * **Python**
  * **Selenium** (para automação do navegador)
  * **Beautiful Soup** (para extração de dados do HTML)
  * **Pandas** (para exportar para Excel)

## Como Executar

**1. Pré-requisitos:**

  * Python 3.x
  * Google Chrome
  * **ChromeDriver**: Deve ser compatível com sua versão do Chrome e estar no `PATH` do sistema.

**2. Instale as dependências:**
Crie um arquivo `requirements.txt` com o conteúdo abaixo:

```txt
selenium
beautifulsoup4
pandas
openpyxl
```

Em seguida, instale-o:

```bash
pip install -r requirements.txt
```

**3. Execute o script:**

```bash
python main.py
```

## Resultado

Ao final da execução, o script criará um arquivo chamado **`casas_de_aposta.xlsx`** no mesmo diretório, contendo os dados das empresas.