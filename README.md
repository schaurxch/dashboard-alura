# 📊 Dashboard em Dash  

Dashboard desenvolvido durante o curso de **Dash** na [Alura](https://www.alura.com.br/).  
O projeto combina **visualização de dados** e **machine learning**, permitindo:  

- 📈 Analisar dados do conjunto **Heart Disease** (UCI Repository) por meio de gráficos interativos como histogramas e boxplots.  
- 🧑‍⚕️ Preencher um **formulário** com variáveis relevantes (idade, colesterol, pressão arterial, etc.) para gerar predições automáticas.  
- 🤖 Utilizar um modelo de **Machine Learning (XGBoost)** previamente treinado, que retorna se há ou não risco de doença cardíaca.  
- 🎨 Disponibilizar uma interface intuitiva com o framework **Dash** e componentes estilizados via **Dash Bootstrap Components (DBC)**.  

Esse projeto integra conceitos de **ciência de dados, estatística e IA**, em um ambiente web interativo.

---

## 🚀 Tecnologias Utilizadas

- [Visual Studio Code](https://code.visualstudio.com/) - Editor de código-fonte  
- [Python](https://www.python.org/) - Linguagem de programação  
- [Pandas](https://pandas.pydata.org/) - Manipulação e análise de dados  
- [Plotly Express](https://plotly.com/python/plotly-express/) - Criação de gráficos interativos  
- [UCI Machine Learning Repository](https://archive.ics.uci.edu/) - Fonte de dados para aprendizado de máquina  
- [Dash](https://dash.plotly.com/) - Framework para criação de dashboards interativos em Python  
- [HTML](https://developer.mozilla.org/pt-BR/docs/Web/HTML) - Estruturação da interface  
- [Dash Bootstrap Components (DBC)](https://dash-bootstrap-components.opensource.faculty.ai/) - Componentes de estilo baseados no Bootstrap  
- [Scikit-learn](https://scikit-learn.org/stable/) - Biblioteca para Machine Learning  
- [XGBoost](https://xgboost.readthedocs.io/) - Biblioteca para modelos de gradient boosting  

---

## ⚙️ Como Executar o Projeto

Antes de rodar o projeto, certifique-se de ter o **Python 3.8+** instalado em sua máquina.

1. Faça download do repositório e abra a pasta **Dash** no VS Code
2. Abra o terminal e certifique-se que está no diretório correto
3. Rode os comandos abaixo, em ordem:

```bash
python -m venv .venv
```
No Terminal CMD:
```bash
.\.venv\Scripts\activate.bat
```
Ou no PowerShell:
```bash
.\.venv\Scripts\activate
```
Em seguida:
```bash
pip install -r requirements.txt
```
```bash
python main.py
```



