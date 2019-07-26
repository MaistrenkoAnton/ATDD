import app
from unittest import TestCase
from unittest.mock import patch
from blog import Blog
from post import Post


class AppTest(TestCase):

    def setUp(self) -> None:
        self.blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': self.blog}

    def test_menu_calls_create_blog(self):
        with patch('builtins.input') as input_mock:
            input_mock.side_effect = ('c', 'Test Create Blog', 'Test Author', 'q')
            app.menu()
            self.assertIsNotNone(app.blogs['Test Create Blog'])

    def test_menu_input_prompt(self):
        with patch('builtins.input', return_value='q') as input_mock:
            app.menu()
            input_mock.assert_called_with(app.MENU_PROMPT)

    def test_menu_calls_print_blog(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value='q'):
                app.menu()
                mocked_print_blogs.assert_called()

    def test_print_blogs(self):
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Test by Test Author (0 posts)')

    def test_ask_create_blog(self):
        with patch('builtins.input') as input_mock:
            input_mock.side_effect = ('Test', 'Test Author')
            app.ask_create_blog()
            self.assertEqual(str(app.blogs['Test']), 'Test by Test Author (0 posts)')

    def test_ask_to_read_blog(self):
        self.blog.posts.append(Post('Post', 'Content'))
        with patch('builtins.input', return_value='Test'):
            with patch('builtins.print') as print_mock:
                app.ask_to_read_blog()
                print_mock.assert_called_with('\n--- Post ---\n\nContent\n    \n')

    def test_ask_create_post(self):
        with patch('builtins.input') as input_mock:
            input_mock.side_effect = ('Test', 'Test post title', 'Test content')
            app.ask_create_post()
            self.assertEqual(app.blogs['Test'].posts[0].title, 'Test post title')
            self.assertEqual(app.blogs['Test'].posts[0].content, 'Test content')
