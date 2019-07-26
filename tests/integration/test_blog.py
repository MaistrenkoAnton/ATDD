from unittest import TestCase

from blog import Blog


class BlogTest(TestCase):
    def test_create_post_in_blog(self):
        b = Blog('The best book', 'John Doe')
        b.create_post('Test Post', 'Test content')

        self.assertEqual(len(b.posts), 1)
        self.assertEqual(b.posts[0].title, 'Test Post')
        self.assertEqual(b.posts[0].content, 'Test content')

    def test_json_no_posts(self):
        b = Blog('The best book', 'John Doe')
        expect = {
            'title': 'The best book',
            'author': 'John Doe',
            'posts': []
        }

        self.assertDictEqual(expect, b.json())

    def test_json(self):
        b = Blog('The best book', 'John Doe')
        b.create_post('Test Post', 'Test content')
        expect = {
            'title': 'The best book',
            'author': 'John Doe',
            'posts': [{
               'title': 'Test Post',
               'content': 'Test content',
            }]
        }
        self.assertDictEqual(expect, b.json())
