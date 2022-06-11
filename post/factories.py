# factories.py
import factory
from factory.django import DjangoModelFactory

from .models import *

# Defining a factory


class ThreadFactory(DjangoModelFactory):
    class Meta:
        model = Category

    # creator = factory.SubFactory(UserFactory)
    title = factory.Faker(
        "sentence",
        nb_words=5,
        variable_nb_words=True
    )


# Create a new thread
t = ThreadFactory()
t.title  # Room marriage study
t.creator  # <User: Michelle>
t.creator.name  # Michelle
