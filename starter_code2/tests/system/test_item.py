from models.item import ItemModel
from models.store import StoreModel
from models.user import UserModel
from tests.base_test import BaseTest
import json


class ItemTest(BaseTest):
    def setUp(self):
        super().setUp()
        with self.app() as client:
            with self.app_context():
                UserModel('test', '1234').save_to_db()
                auth_response = client.post(
                    '/auth',
                    data=json.dumps({'username': 'test', 'password': '1234'}),
                    headers={'Content-Type': 'application/json'}
                )
                self.access_token = json.loads(auth_response.data)['access_token']

    def test_get_item_no_auth(self):
        with self.app() as client:
            with self.app_context():
                response = client.get('/item/test')
                self.assertEqual(response.status_code, 401)

    def test_get_item_not_found(self):
        with self.app() as client:
            with self.app_context():
                auth_header = {'Authorization': f'JWT {self.access_token}'}
                response = client.get('/item/test', headers=auth_header)
                self.assertEqual(response.status_code, 404)

    def test_get_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test').save_to_db()
                ItemModel('test', 19.99, 1).save_to_db()
                auth_header = {'Authorization': f'JWT {self.access_token}'}
                response = client.get('/item/test', headers=auth_header)
                self.assertEqual(response.status_code, 200)

    def test_delete_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test').save_to_db()
                ItemModel('test', 19.99, 1).save_to_db()
                response = client.delete('/item/test')
                self.assertEqual(response.status_code, 200)
                self.assertEqual(json.loads(response.data), {'message': 'Item deleted'})

    def test_create_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test').save_to_db()
                response = client.post('/item/test', data={'price': 17.99, 'store_id': 1})
                self.assertEqual(response.status_code, 201)
                self.assertEqual(json.loads(response.data), {'name': 'test', 'price': 17.99})

    def test_duplicate_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test').save_to_db()
                ItemModel('test', 19.99, 1).save_to_db()
                response = client.post('/item/test', data={'price': 17.99, 'store_id': 1})
                self.assertEqual(response.status_code, 400)
                self.assertEqual(json.loads(response.data), {'message': "An item with name 'test' already exists."})

    def test_put_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test').save_to_db()
                response = client.put('/item/test', data={'price': 17.99, 'store_id': 1})
                self.assertEqual(response.status_code, 200)
                self.assertEqual(json.loads(response.data), {'name': 'test', 'price': 17.99})

    def test_put_update_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test').save_to_db()
                ItemModel('test', 19.99, 1).save_to_db()
                response = client.put('/item/test', data={'price': 17.99, 'store_id': 1})
                self.assertEqual(response.status_code, 200)
                self.assertEqual(json.loads(response.data), {'name': 'test', 'price': 17.99})

    def test_put_item_list(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test').save_to_db()
                ItemModel('test', 19.99, 1).save_to_db()

                response = client.get('/items')
                self.assertEqual(response.status_code, 200)
                self.assertEqual(json.loads(response.data), {'items': [{'name': 'test', 'price': 19.99}]})
