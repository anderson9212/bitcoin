# Sistema Bitcoin

Sistema para enviar e receber frações de moedas, utilizando uma rede blockchain alternativa do Bitcoin para testes

[Clique aqui para acessar o sistema](http://bitcoin.debr.com.br)


## Detalhes de Implemetação
Foi utilizado a tecnologia para back-end Django(webframework do python), com as dependências:<br>
<strong>BlockCypher, Bitcoin, Django-widget-Tweaks, requests</strong>, entre outros.
Para uma lista completa das dependências, verificar o arquivo 'requirements.txt' ou através do comando:
```
pip list
```


Foram utilizadas as tecnologias para front-end: HTML5, CSS3, JavaScript e Jquery.

## Como rodar a aplicação
Com a linguagem de programação Python instalado no computador, entrar na pasta do projeto, criar um ambiente virtual e instalar as dependências do projeto através do comando no terminal:

```
pip install -r requirements.txt
```
Após instalar as dependências, criar uma variável de ambiente no sistema operacional:
```
DJANGO_SECRET_KEY='olnsu1ad*#5r()&yt8ldy*v)e6oga2v@%6*v48)cx^m-z)3u14'
```
Para executar o servidor interno do Django, executar o comando no terminal:
```
python manage.py runserver
```
O retorno será o IP local para acessar a aplicação


## Como utilizar a aplicação
Através do sistema, é possível: 

* Enviar Satohis(tela de enviar moedas), será preciso inserir a quantidade de Satohis entre 7000 e 4000000
* Receber Satohis(tela de receber moedas), será preciso inserir a quantidade de Satohis entre 1 e 1000000
* Informações sobre um endereço(tela inicial)
* Informações detalhada sobre uma transação realizada(tela de transações)


## Testes
O sistema utiliza a estrutura de testes do Django, para testar o sistema, executar o comando no terminal:
```
python manage.py tests
```
