# materials/tests.py
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Material


class MaterialAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_material(self):
        url = reverse('material-create')
        data = {'formula': 'H2O', 'density': 1.0}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('id' in response.data)

    def test_retrieve_material(self):
        material = Material.objects.create(formula='CO2', density=1.87)
        url = reverse('material-retrieve', args=[material.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], material.id)
        self.assertEqual(response.data['formula'], material.formula)
        self.assertEqual(response.data['density'], material.density)

    def test_search_materials(self):
        Material.objects.create(formula='H2O', density=1.5)
        Material.objects.create(formula='CH4', density=2.0)
        url = reverse('material-search') + '?min_density=1.0&max_density=2.0&include_elements=H&exclude_elements=Fe'
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any(material['formula'] == 'H2O' for material in response.data))
