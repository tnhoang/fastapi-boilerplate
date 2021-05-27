from datetime import datetime

import factory

from app.models.item import Item
from app.models.user import User


class UserFactory(factory.Factory):
    class Meta:
        model = User

    id = factory.Sequence(lambda n: n)
    full_name = factory.Faker("name")
    email = factory.Faker("email")
    is_active = True
    is_superuser = False


class ItemFactory(factory.Factory):
    class Meta:
        model = Item

    id = factory.Sequence(lambda n: n)
    title = "title"
    description = datetime.now()
    owner = factory.SubFactory(UserFactory)
