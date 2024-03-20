import random

from faker import Faker


def random_number(start: int = 100, end: int = 1000) -> int:
    return random.randint(start, end)


def random_name():
    faker = Faker()
    return faker.last_name()


def random_email():
    faker = Faker()
    return faker.email()


def random_gender():
    return random.choice(['male', 'female'])


def random_status():
    return random.choice(['active', 'inactive'])
