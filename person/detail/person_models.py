from sqlalchemy import insert, update, delete, select
from sqlalchemy.orm import Session
from person.detail.models import Person


class PersonModel:
    def __init__(self, person_id=None):
        self.id = person_id
        self.code = ""
        self.name = ""
        self.family = ""
        self.is_active = True

    def to_dict(self):
        return {
            "code": self.code,
            "name": self.name,
            "family": self.family,
            "is_active": self.is_active,
        }

    def save(self, db: Session):
        data = self.to_dict()

        if self.id:
            stmt = update(Person).where(Person.id == self.id).values(**data)
            db.execute(stmt)
        else:
            stmt = insert(Person).values(**data)
            result = db.execute(stmt)
            self.id = result.inserted_primary_key[0]

        db.commit()

    def load(self, db: Session):
        stmt = select(Person).where(Person.id == self.id)
        person = db.execute(stmt).scalar_one_or_none()

        if not person:
            raise ValueError("Person not found")

        self.code = person.code or ""
        self.name = person.name or ""
        self.family = person.family or ""
        self.is_active = bool(person.is_active)

        return self.to_dict()

    def delete(self, db: Session):
        stmt = delete(Person).where(Person.id == self.id)
        db.execute(stmt)
        db.commit()
