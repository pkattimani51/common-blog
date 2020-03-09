import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'personal_portfolio.settings')

import django
django.setup()

import random
from blogs.models import Post, Comment, Category
from faker import Faker

fake = Faker()


def create_categories(n):
    for i in range(n):
        cat = Category.objects.get_or_create(name=fake.word())[0]
        cat.save()


def get_category():
    out = list(Category.objects.all())
    random.shuffle(out)
    return out[0:random.randint(3, 8)]


def populate_fake_data(N=5):
    for i in range(N):
        title = fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
        body = " ".join(fake.texts(nb_texts=3, max_nb_chars=200, ext_word_list=None))
        created_on = fake.date_time_between(start_date='-2y', end_date='now', tzinfo=None)
        # updated_on = fake.date_time_between(start_date='-2y', end_date='now', tzinfo=None)
        post = Post(title=title, body=body, created_on=created_on)
        post.save()
        for cat in get_category():
            post.categories.add(cat)
        create_comments(post)


def create_comments(obj, n=5):
    for i in range(n):
        author = fake.name()
        comm_body = " ".join(fake.texts(nb_texts=3, max_nb_chars=100, ext_word_list=None))
        comment = Comment.objects.get_or_create(author=author, body=comm_body, post=obj)


if __name__ == "__main__":
    create_categories(50)
    populate_fake_data(100)