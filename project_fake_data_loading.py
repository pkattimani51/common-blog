import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'personal_portfolio.settings')

import django
django.setup()

from projects.models import Project
import random
from faker import Faker

fake = Faker()

images = ['project1.png','project2.png','project3.png','project4.png','project5.png','project6.png','project7.png','project8.png']

def add_project_fake_data(n):
    for i in range(30):
        title = fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
        description = " ".join(fake.texts(nb_texts=3, max_nb_chars=200, ext_word_list=None))
        technology = fake.word()
        image = "/img/"+random.choice(images)
        Project.objects.get_or_create(title=title, description=description, technology=technology, image=image)

if __name__ == "__main__":
    add_project_fake_data(30)
    print("Data created successfully")