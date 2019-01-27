from django.shortcuts import render
from blockcypher import get_address_details, get_transaction_details, create_unsigned_tx, simple_spend, \
    list_forwarding_addresses, constants


def home(request):
    # data = get_address_details('1DEP8i3QJCsomS4BSMY2RpU1upv62aGvhD')
    # data = get_address_details('13vCnAofrX7bskFbnKYyAQzWZNJgRDsmBZ')
    data = get_address_details('3BF1M1PnTge94QewuWh3B8mRVw8U4SVnb4')
    return render(request, 'index.html', data)


def transaction(request, hash):
    data = get_transaction_details(hash)
    return render(request, 'transaction.html', data)


def send(request):
    #simple_spend(from_privkey='97838249d77bfa65f97be02b63fd1b7bb6a58474c7c22784a0da63993d1c2f90',
    #             to_address='C1rGdt7QEPGiwPMFhNKNhHmyoWpa5X92pn', to_satoshis=1000, coin_symbol='bcy',
    #             api_key='ca2a67fd0abf46cd938570f4f54b2b1f')

    #inputs = [{'address': 'CEztKBAYNoUEEaPYbkyFeXC5v8Jz9RoZH9'}, ]
    #outputs = [{'address': 'C1rGdt7QEPGiwPMFhNKNhHmyoWpa5X92pn', 'value': 1000000}]
    #unsigned_tx = create_unsigned_tx(inputs=inputs, outputs=outputs, coin_symbol='bcy', api_key='ca2a67fd0abf46cd938570f4f54b2b1f')
    #unsigned_tx

    #print(unsigned_tx)

    data = {}
    data['coin'] = constants.COIN_CHOICES
    return render(request, 'send.html', data)


def receive(request):
    return render(request, 'receive.html')


def email():
    pass


def send_email(request):
    return render(request, 'form_email.html')


def confirm_email():
    pass
