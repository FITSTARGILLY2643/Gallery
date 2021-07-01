from django.test import TestCase
from .models import Location,Image,Category
import datetime as dt
# Create your tests here.
class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.location = Location(id=1,name = 'karatina')
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))
        
    # Testing Save Method
    def test_save_method(self):
        self.location.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)
# Testing delete Method
    def test_delete_location(self):
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location)== 0) 
        # Testing update location Method
    def test_update_location(self):
        self.location.save_location()
        self.location.update_location(self.location.id, 'Kiambu')
        changed_location = Location.objects.filter(name ='Kiambu')
        self.assertTrue(len(changed_location) > 0) 