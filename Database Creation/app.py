from datetime import date
from model import Wallet
from model import Base
from sqlalchemy import create_engine


def create_people():
    session = session_factory()
    bruno = Person("Bruno Krebs", date(1984, 10, 20), 182, 84.5)
    john = Person("John Doe", date(1990, 5, 17), 173, 90)
    session.add(bruno)
    session.add(john)
    session.commit()
    session.close()


def get_people():
    session = session_factory()
    people_query = session.query(Person)
    session.close()
    return people_query.all()


def get_wallet():
	session = session_factory()
	wallet_query = session.query(Wallet)
	wallet_query = session.query


if __name__ == "__main__":
    people = get_people()
    if len(people) == 0:
        create_people()
    people = get_people()

    for person in people:
        print(f'{person.name} was born in {person.date_of_birth}')