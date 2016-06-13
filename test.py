import unittest
from game import *

class TestEntity(unittest.TestCase):

    def test_add_component(self):
        entity = Entity(0)
        component = Component()
        entity.add_component(component)
        self.assertIn(Component, entity.components)

    def test_has_component(self):
        entity = Entity(0)
        entity.add_component(Component())
        self.assertTrue(entity.has_component(Component))

    def test_get_component(self):
        entity = Entity(0)
        component = Component()
        entity.add_component(component)
        returned = entity.get_component(Component)
        self.assertEqual(component, returned)
        
unittest.main()
