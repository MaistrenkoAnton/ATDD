from unittest import TestCase

from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Test Author')

        self.assertEqual(b.title, 'Test')
        self.assertEqual(b.author, 'Test Author')
        self.assertListEqual(b.posts, [])
        self.assertEqual(len(b.posts), 0)
