import json

from django.http import response
from django.test import Client
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from src.apps.widgets.models import Widget


class WidgetViewTestCase(APITestCase):
    """
    Test the CRUD actions of the Widget view.
    """

    def setUp(self):
        self.client = Client()
        self.original_widget = Widget.objects.create(
            name='Facebook', number_of_parts=1
        )

    def test_list_widget(self):
        url = reverse('widget-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_widget(self):
        url = reverse('widget-detail', kwargs={'pk': self.original_widget.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.data
        self.assertEqual(self.original_widget.name, data['name'])
        self.assertEqual(
            self.original_widget.number_of_parts, data['number_of_parts']
        )

    def test_delete_widget(self):
        url = reverse('widget-detail', kwargs={'pk': self.original_widget.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Check that widget has been deleted
        url = reverse('widget-list')
        response = self.client.get(url)
        self.assertEqual(len(response.data), 0)

    def test_create_widget(self):
        payload = {
            'name': 'Instagram',
            'number_of_parts': 2
        }
        response = self.client.post(
            reverse('widget-list'),
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_widget(self):
        new_name = 'TikTok'
        payload = {'name': new_name}
        url = reverse('widget-detail', kwargs={'pk': self.original_widget.pk})
        response = self.client.patch(
            url,
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.original_widget.refresh_from_db()
        self.assertEqual(new_name, self.original_widget.name)

    def test_invalid_create(self):
        payload = {
            'name': 'Instagram',
            'number_of_parts': 'not a number'
        }
        response = self.client.post(
            reverse('widget-list'),
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(
            response.status_code, status.HTTP_400_BAD_REQUEST
        )
