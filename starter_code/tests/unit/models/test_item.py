from unittest import TestCase

from models.item import ItemModel


class ItemTest(TestCase):
    def test_create_item(self):
        item = ItemModel('book', 20)
        self.assertEqual(item.name, 'book')
        self.assertEqual(item.price, 20.00)

    def test_create_json(self):
        item = ItemModel('book', 20)
        self.assertEqual(item.json(), {'name': 'book', 'price': 20.00})
