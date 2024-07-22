# from django.test import TestCase

# # Create your tests here.

# from django.urls import reverse
# from django.contrib.auth import get_user_model
# from .models import Car

# class PetsTests(TestCase):

#     def test_list_page_status_code(self):
#         url = reverse('cars')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)

#     def test_list_page_template(self):
#         url = reverse('pets')
#         response = self.client.get(url)
#         self.assertTemplateUsed(response, 'pets_list.html')
#         self.assertTemplateUsed(response, 'base.html')

#     def setUp(self):

#         self.user = get_user_model().objects.create_user(
#             username= 'test_user',
#             email="test@email.com",
#             password="1234"
#         )

#         self.pet = Pet.objects.create(
#             owner = self.user,
#             name = "test_pet",
#             des = "test des",
#             breed = "breed_test"
#         )

#     def test_str_method(self):
#         self.assertEqual(str(self.pet), "test_pet")

    
#     def test_details_view(self):
#         url = reverse('pet_details', args=[self.pet.id])
#         response = self.client.get(url)
#         self.assertTemplateUsed(response,'pet_details.html')

#     def test_create_view(self):

#         obj= {
#             "owner": self.user.id,
#             "name":"test_cat",
#             "des":"....",
#             "breed":"...."
#         }

#         url = reverse('create_pet')
#         response = self.client.post(path = url, data= obj, follow= True)
#         # self.assertEqual(len(Pet.objects.all()), 2)
#         self.assertRedirects(response, reverse('pet_details', args=[2]))

