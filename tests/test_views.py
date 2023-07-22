from django.test import TestCase
from restaurant.models import MenuItem
from restaurant.serializers import MenuSerializer
class MenuViewTest(TestCase):
    def setup(self):
        MenuItem.objects.create(title="Chocolate", price=5, inventory=8)

    def test_getall(self):        
        serializer_class = MenuSerializer(data=MenuItem.objects.all())        
        self.assertEqual(serializer_class.is_valid(), False)

