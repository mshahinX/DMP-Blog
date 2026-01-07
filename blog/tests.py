from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
class BlogAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

        self.other_user = User.objects.create_user(username='otheruser', password='12345')



    def test_user_can_login(self):
        url = reverse("token_obtain_pair")

        response = self.client.post(url, {'username': 'testuser', 'password': '12345'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)  
        self.assertIn('refresh', response.data)




    def authenticate(self):
        response = self.client.post(reverse("token_obtain_pair"), {'username': 'testuser', 'password': '12345'}, format='json')

        token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)



    def test_user_can_create_blog(self):
        self.authenticate()

        response = self.client.post("/api/blogs/", {'title': 'Test Blog', 'content': 'This is a test blog.'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Test Blog')
        self.assertEqual(response.data['content'], 'This is a test blog.')


    def test_user_cannot_access_others_blogs(self):
        self.client.force_authenticate(user=self.other_user)
        self.client.post("/api/blogs/", {'title': 'Other Blog', 'content': 'This is other user blog.'}, format='json')

        self.client.force_authenticate(user = None)
        self.authenticate()

        response = self.client.get("/api/blogs/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 0)


    def test_authenticated_user_cannot_create_blog(self):
        response = self.client.post("/api/blogs/", {'title': 'Test Blog', 'content': 'This is a test blog.'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)