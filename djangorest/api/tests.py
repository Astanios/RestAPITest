from django.test import TestCase
from .models import Car
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
# Create your tests here.
class ModelTestCase(TestCase):
    def setUp(self):
        self.car_name = "Mustang"
        self.brand = "Ford"
        self.color = "Red"
        self.automatic = True
        self.insured = False
        self.car = Car(name=self.car_name, brand=self.brand, color=self.color, automatic=self.automatic, insured=self.insured)

    def test_model_can_create_a_car(self):
        old_Count = Car.object.count()
        self.car.save()
        new_count = Car.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_api_can_get_a_car(self):
        car = Car.objects.get()
        response = self.client.get(
            reverse('details'),
            kwargs={'pk': car.id},
            format = "json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, car)

    def test_api_can_update_car(self):
        change_car = {'name':  'New'}
        res = self.client.put(
            reverse('details', kwargs={'pk': car.id}),
            change_car, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_car(self):
        car = Car.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': car.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
class ViecTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.car_data = {'name': 'Impala', 'brand' : 'Chevrolet', 'color': 'Green'}
        self.response = self.client.post(
            reverse('create'),
            self.car_data,
            format="json")
