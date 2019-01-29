from django.shortcuts import render, redirect
from blockcypher import get_address_details, get_transaction_details, send_faucet_coins
from apps.site_bitcoin.forms import SendForm, ReceiveForm
import requests

# Dicionário python com principais parâmetros do sistema
data_blockcypher = {
    'address': 'C1meuDnZ4RNBjDhZD6FwLVhG1ecr4sDhfZ',
    'private': '1c8134cbcbeedebee9ff5add6224cf542ec8d8c82f45d650d404bfb0e4a1aacf',
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
    if request.method == 'POST':
        form = SendForm(request.POST)
        if form.is_valid():
            value = int(form.cleaned_data['value'])

            data = {'from_private': data_blockcypher['private'],
                    'to_address': data_blockcypher['address'], 'value_satoshis': value}
            params = {'token': data_blockcypher['api_key']}
            requests.post(data_blockcypher['url'], data=data, params=params)

            return redirect('home')
    else:
        form = SendForm()

    return render(request, 'send.html', {'form': form})


# Função para receber frações de moedas
def receive(request):
    if request.method == 'POST':
        form = ReceiveForm(request.POST)
        if form.is_valid():
            value = int(form.cleaned_data['value'])
            send_faucet_coins(address_to_fund=data_blockcypher['address'], satoshis=value,
                              api_key=data_blockcypher['api_key'])

            return redirect('home')
    else:
        form = ReceiveForm()

    return render(request, 'receive.html', {'form': form})
