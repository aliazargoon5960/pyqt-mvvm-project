from sqlalchemy import select
from sqlalchemy.orm import Session
from person.detail.models import Person


class PersonListModel:

    @staticmethod
    def get_all(db: Session):
        stmt = select(Person)
        persons = db.execute(stmt).scalars().all()

        result = []
        for p in persons:
            result.append({
                "id": p.id,
                "code": p.code,
                "name": p.name,
                "family": p.family,
                "is_active": p.is_active
            })

        return result
