class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self):
        return f'{self.title} by {self.author} ({len(self.posts)} post{"" if len(self.posts) == 1 else "s"})'

    def create_post(self):
        pass

    def json(self):
        pass
