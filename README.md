<h1 align='center'>
    <p>Machine Learning - Python</p>
</h1>

## 🙋‍♂️ Equipe de desenvolvedores
<table align='center'>
  <tr>
    <td align="center">
        <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/101208372?v=4" width="100px;" alt=""/><br /><sub><b>Yann Lucas</b></sub></a><br />👨‍🚀</a></td>
    <td align="center">
        <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/60533993?v=4" width="100px;" alt=""/><br /><sub><b>Felipe Pinheiro</b></sub></a><br />👨‍🚀</td>
  </table>

Tabela de conteúdos
=================
<!--ts-->
   * [Sobre](#📘-sobre)
   * [Imports](#imports)
   * [Estrutura do Projeto](#estrutura-do-projeto)
   * [Funcionalidades](#funcionalidades)
      * [Rotas](#rotas)
      * [JSON](#json)
   * [Funcionamento Interno](#funcionamento-interno)
   * [Tecnologias](#🛠-tecnologias)
   * [Comandos](#comandos)
<!--te-->

## 📘 Sobre

Este projeto é uma aplicação web Flask que integra uma interface feita em HTML/CSS com uma API Rest, onde utilizamos um modelo de aprendizado de máquina para uma tarefa de classificação.

### Imports:
```py
app.py
    import joblib
    from flask import Flask, request, jsonify, render_template
```
```py
training.py
    import pandas as pd
    from sklearn import tree
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score
    import joblib
```
```py
test_request_post.py
    import requests
```
```py
app_cors.py
    import joblib
    from flask import Flask, request, jsonify
    from flask_cors import CORS, cross_origin
```

## Estrutura do Projeto
- A API foi escrita em python utilizando Flask.
- Utilizamos o modelo `tree.DecisionTreeClassifier()` da scikit-learn para o treinamento da máquina.
- Para o salvar o modelo treinado, utilizamos a biblioteca `joblib`

## Funcionalidades:
#### rotas :
- `@app.route('/')`: Exibe o formulário que pode ser preenchido pelo usuário.
- `@app.route('/predict', methods=['POST'])` : Essa rota é usada para enviar dados e obter previsões de felicidade.

#### json :
```json
{
    "infoavail" : 5,
    "housecost" : 3,
    "schoolquality" : 3,
    "policetrust" : 3,
    "streetquality" : 3,
    "events" : 5
}
```

## Funcionamento Interno

O usuário fornece dados através de um formulário em uma página web e ao clicar no botão enviar, os dados são encapsulados em um arquivo `JSON` e enviados para nossa `API Rest`, onde ao receber os dados ela realiza a predição utilizando o modelo de aprendizado de máquina e faz o envio da resposta. Essa resposta é encapsulada novamento em um `JSON` pela `API` e é enviada a página `HTML`, assim sendo exibida ao usuário.
 

### 🛠 Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:
| Logo  | Tecnologia |
| ----- | ---------- |
| <img src="static/flask.png" height='40px' align='center'/> |[Flask](https://flask.palletsprojects.com/en/3.0.x/)  |
| <img src="static/python-original.svg" height='30px' align='center'/> | [Python](https://www.python.org)  |
|<img src="static/pandas-original.svg" height='30px' align='center'/> |[Pandas](https://pandas.pydata.org)| 
| <img src="static/joblib_logo.svg" height='30px' align='center'> |[JobLib](https://joblib.readthedocs.io/en/stable/)| 
| <img src="static/logo-small.2a411bc6.svg" height='30px' align='center'> |[Requests](https://pypi.org/project/requests/)| 
| <img src="static/scikit-learn.png" height='30px' align='center'> |[Scikit-Learn](https://scikit-learn.org/stable/)| 


## Comandos

<p> instala todas as dependências listadas em requirements.txt :</p>

    pip install -r requirements.txt    

<p> lista os modulos disponíveis : </p> 

    pip list 