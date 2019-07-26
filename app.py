from blog import Blog
from post import Post

MENU_PROMPT = 'Enter "c" to create  blog, "l" to list the blogs, "r" to read one, "p" to create a post, or "q" to quit:'
POST_TEMPLATE = '''
--- {} ---

{}
    
'''
blogs = dict()


def menu():
    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == '1':
            print_blogs()
        elif selection == 'r':
            ask_to_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)


def print_blogs():
    for key, blog in blogs.items():
        print('- {}'.format(blog))


def ask_create_blog():
    title = input('Enter your blog title: ')
    author = input('Enter your name: ')
    blogs[title] = Blog(title, author)


def ask_to_read_blog():
    title = input('Enter the blog you want to read:')
    print_posts(blogs.get(title))


def print_posts(blog):
    for post in blog.posts:
        print_post(post)


def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))


def ask_create_post():
    blog_name = input('Enter your post title: ')
    title = input('Enter your post title: ')
    content = input('Enter the content: ')
    blogs[blog_name].create_post(title, content)
