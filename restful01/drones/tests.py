from django.utils.http import urlencode
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from drones.models import DronesCategory
from drones import views


class DroneCategoryTests(APITestCase):
    def post_drone_category(self, name):
        url = reverse("dronecategory-list")
        data = {"name": name}
        response = self.client.post(url, data, format="json")
        return response

    # Testa o método POST
    def test_post_and_get_drone_category(self):
        new_drone_category_name = "Hexacopter"
        response = self.post_drone_category(new_drone_category_name)
        print("PK {0}".format(DronesCategory.objects.get().pk))
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(1, DronesCategory.objects.count())
        self.assertEqual(new_drone_category_name, DroneCategory.objects.get().name)