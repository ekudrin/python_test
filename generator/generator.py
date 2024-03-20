import random

from faker import Faker

from data.data import Person

faker_ru = Faker('ru_RU')
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        age=random.randint(10, 80),
        salary=random.randint(1000, 100000),
        department=faker_ru.job(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        mobile=faker_ru.msisdn()
    )


def generated_file():
    path = rf'C:\Users\chest\PycharmProjects\python_test\filetest{random.randint(0, 10)}.txt'
    file = open(path, 'w+')
    file.write('Hello hello')
    file.close()
    return file.name, path
