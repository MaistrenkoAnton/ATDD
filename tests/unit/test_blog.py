from unittest import TestCase

from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Test Author')

        self.assertEqual(b.title, 'Test')
        self.assertEqual(b.author, 'Test Author')
        self.assertListEqual(b.posts, [])
        self.assertEqual(len(b.posts), 0)

    def test_repr(self):
        b1 = Blog('Test', 'Test Author')
        b2 = Blog('The best book', 'John Doe')
        self.assertEqual(b1.__repr__(), 'Test by Test Author (0 posts)')
        self.assertEqual(b2.__repr__(), 'The best book by John Doe (0 posts)')

    def test_repr_multiple_posts(self):
        b1 = Blog('The best book', 'John Doe')
        b1.posts = ['first', 'second', 'third']
        self.assertEqual(b1.__repr__(), 'The best book by John Doe (3 posts)')

    def test_repr_single_post(self):
        b1 = Blog('The best book', 'John Doe')
        b1.posts = ['first']
        self.assertEqual(b1.__repr__(), 'The best book by John Doe (1 post)')
