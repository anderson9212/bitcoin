from django.test import TestCase
from django.urls import reverse


class HomeTest(TestCase):

    def setUp(self):
        self.url = reverse('apps:site_bitcoin:home')

    def test_response_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'templates/index.html')


class TransactionTest(TestCase):

    def setUp(self):
        self.url = reverse('apps:site_bitcoin:transaction')

    def test_response_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'templates/transaction.html')


class SendTest(TestCase):
    def setUp(self):
        self.url = reverse('apps:site_bitcoin:send')

    def test_response_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'templates/send.html')


class ReceiveTest(TestCase):
    def setUp(self):
        self.url = reverse('apps:site_bitcoin:receive')

    def test_response_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'templates/receive.html')
