from django.test import TestCase
from apps.site_bitcoin.forms import SendForm, ReceiveForm


class SendFormTest(TestCase):

    def test_SendForm_valid(self):
        form = SendForm(data={'value': 100})
        self.assertTrue(form.is_valid())

    def test_SendForm_invalid(self):
        form = SendForm(data={'value': 0})
        self.assertFalse(form.is_valid())


class ReceiveFormTest(TestCase):

    def test_ReceiveForm_valid(self):
        form = ReceiveForm(data={'value': 100})
        self.assertTrue(form.is_valid())

    def test_ReceiveForm_invalid(self):
        form = ReceiveForm(data={'value': 0})
        self.assertFalse(form.is_valid())
