MENU_PROMPT = 'Enter "c" to create  blog, "l" to list the blogs, "r" to read one, "p" to create a post, or "q" to quit:'

blogs = dict()


def menu():
    selection = input(MENU_PROMPT)
    print_blogs()


def print_blogs():
    for key, blog in blogs.items():
        print('- {}'.format(blog))

