from django.shortcuts import render, redirect
from blockcypher import get_address_details, get_transaction_details, send_faucet_coins
from apps.site_bitcoin.forms import SendForm, ReceiveForm
import requests

# Dicionário python com principais parâmetros do sistema
data_blockcypher = {
    'address': 'BuPY4atfKzg5T5upXak7Hb4estsevLFPPh',
    'private': 'b1798c6c41f4dfc3466cf3b9a08cd5f7bc2d0bcb07106da673a913fea44a9a28',
    'api_key': 'ca2a67fd0abf46cd938570f4f54b2b1f',
    'url': 'https://api.blockcypher.com/v1/bcy/test/txs/micro',
}


# Função da tela inicial
def home(request):
    # Armazena na variável data informações do endereço ao passar o hash do endereço e a moeda
    data = get_address_details(data_blockcypher['address'], coin_symbol='bcy', txn_limit=10)
    # Retorna uma página HTML com informações do endereço
    return render(request, 'index.html', data)


# Função da tela de transação, passando o hash da transação
def transaction(request, hash):
    # Armazena na variável data informações da transação ao passar o hash da transação e a moeda
    data = get_transaction_details(hash, coin_symbol='bcy')
    # Retorna uma página HTML com informações da transação
    return render(request, 'transaction.html', data)


# Função para envio de frações de moedas
def send(request):
    # Verifica se method é do tipo POST
    if request.method == 'POST':
        # Armazena os dados enviado pelo formulário na variável form
        form = SendForm(request.POST)

        # Verifica se o valor submetido no formulário é válido
        if form.is_valid():
            # Transforma o valor retornado em inteiro
            value = int(form.cleaned_data['value'])
            # Preparando parâmetros de envio da moeda
            data = {'from_private': data_blockcypher['private'],
                    'to_address': data_blockcypher['address'], 'value_satoshis': value}
            # Passando a api_token para validar o envio
            params = {'token': data_blockcypher['api_key']}
            # Requisição post com informações sobre a transaçaão
            r = requests.post(data_blockcypher['url'], data=data, params=params)

            try:
                # Retorna a página HTML para enviar frações de moedas com o erro
                return render(request, 'send.html', {'form': form, 'error': r.json()['error']})
            except KeyError:
                # Redireciona para a home(página inicial)
                return redirect('home')
    else:
        # Passa para a variável form os dados da classe form
        form = SendForm()
    # Retorna a página HTML para enviar frações de moedas
    return render(request, 'send.html', {'form': form})


# Função para receber frações de moedas
def receive(request):
    # Verifica se method é do tipo POST
    if request.method == 'POST':
        # Armazena os dados enviado pelo formulário na variável form
        form = ReceiveForm(request.POST)

        # Verifica se o valor submetido no formulário é válido
        if form.is_valid():
            # Transforma o valor retornado em inteiro
            value = int(form.cleaned_data['value'])
            # Função para receber moedas passando: endereço, satoshis e chave da api
            send_faucet_coins(address_to_fund=data_blockcypher['address'], satoshis=value,
                              api_key=data_blockcypher['api_key'])
            # Redireciona para a home(página inicial)
            return redirect('home')
    else:
        # Passa para a variável form os dados da classe form
        form = ReceiveForm()
    # Retorna a página HTML para receber frações de moedas
    return render(request, 'receive.html', {'form': form})
