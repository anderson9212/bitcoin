from django import forms


# Classe de formulário para receber moedas - Valida e cria formulário
class ReceiveForm(forms.Form):
    value = forms.IntegerField(min_value=1, max_value=1000000, required=True, label='Valor recebido')


# Classe de formulário para enviar moedas - Valida e cria formulário
class SendForm(forms.Form):
    value = forms.IntegerField(min_value=7000, max_value=4000000, required=True, label='Valor Enviado')
