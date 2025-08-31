import pandas as pd
from faker import Faker
from datetime import datetime
import random

persons_df = pd.read_csv('data/input/persons.csv')
emails = set(persons_df['EmailAddress'])

def generate_users_schema():
    fake = Faker()
    persons = []
    c = 1

    persons_df = pd.read_csv('data/input/persons.csv')
    emails = set()

    for r in persons_df.iterrows():
        emails.add(r[1]['EmailAddress'])
        persons.append({'id': c, 'firstName': r[1]['FirstName'], 'lastName': r[1]['LastName'], 'email': r[1]['EmailAddress'], 'birthdate': fake.date_between(datetime(1970, 1,1), datetime(1990, 1,1)).strftime('%d/%m/%Y')})
        c += 1

    for _ in range(10000):
        firstName = fake.first_name()
        lastName = fake.last_name()
        date = fake.date_between(datetime(1970, 1,1), datetime(1990, 1,1))
        while True:
            email = firstName.lower() + lastName.lower()[0] + str(random.randint(0,99))  + "@adventure-works.com"
            if email not in emails:
                break
        emails.add(email)
        persons.append({'id': c, 'firstName': firstName, 'lastName': lastName, 'email': email, 'birthdate': date.strftime('%d/%m/%Y') })
        c += 1

    return persons



if __name__ == "__main__":
    generate_users_schema()