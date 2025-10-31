Aqui está uma versão simplificada do README para o seu projeto.

-----

# Desafio Bluetape: Scraper Reclame Aqui

[cite\_start]Este projeto é um web scraper em Python [cite: 6, 10] desenvolvido para o desafio técnico da Bluetape.

## 🎯 Objetivo

[cite\_start]O script automatiza a navegação no site Reclame Aqui [cite: 22, 24] [cite\_start]para extrair dados da categoria "Casa de Aposta"[cite: 31]. [cite\_start]Ele coleta as "Melhores" e "Piores" empresas [cite: 30, 31] [cite\_start]e extrai as seguintes métricas[cite: 27]:

  * Nota
  * Reclamações respondidas (%)
  * Voltariam a fazer negócio (%)
  * Índice de solução (%)

[cite\_start]Os dados coletados são salvos em uma planilha Excel[cite: 32].

## 🛠️ Tecnologias

  * **Python**
  * [cite\_start]**Selenium** [cite: 14] (para automação do navegador)
  * [cite\_start]**Beautiful Soup** [cite: 18] (para extração de dados do HTML)
  * [cite\_start]**Pandas** [cite: 16] (para exportar para Excel)

## 🚀 Como Executar

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

## 📄 Resultado

Ao final da execução, o script criará um arquivo chamado **`casas_de_aposta.xlsx`** no mesmo diretório, contendo os dados das empresas.