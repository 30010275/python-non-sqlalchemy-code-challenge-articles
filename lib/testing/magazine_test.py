class Article:
    instances = []

def __init__(self, author, magazine, title):
    self.author = author
    self.magazine = magazine
    if len(title) < 5 or len(title) > 50:
        raise ValueError("Title must be between 5 and 50 characters.")
    self.title = title
    Article.instances.append(self)
class Author:
    def init(self, name):
        self.name = name

def articles(self):
    return [article for article in Article.instances if article.author == self]

def magazines(self):
    return list(set(article.magazine for article in Article.instances if article.author == self))

def add_article(self, magazine, title):
    new_article = Article(self, magazine, title)
    return new_article

def topic_areas(self):
    return sorted(set(magazine.category for magazine in self.magazines()))
class Magazine:
    def init(self, name, category):
        self.name = name
        self.category = category

def articles(self):
    return [article for article in Article.instances if article.magazine == self]

def contributors(self):
    return list(set(article.author for article in Article.instances if article.magazine == self))

def article_titles(self):
    return [article.title for article in Article.instances if article.magazine == self]

def contributing_authors(self):
    author_counts = {}
    for article in Article.instances:
        if article.magazine == self:
            author_counts[article.author] = author_counts.get(article.author, 0) + 1
    return [author for author, count in author_counts.items() if count > 0]


@classmethod
def top_publisher(cls):
    magazine_counts = {}
    for article in Article.instances:
        magazine_counts[article.magazine] = magazine_counts.get(article.magazine, 0) + 1
    if not magazine_counts:
        return None
    return max(magazine_counts, key=magazine_counts.get)