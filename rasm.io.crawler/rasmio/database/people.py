from rasmio.domain.people import People
from rasmio.database import init_db


class PeopleRepo(People):
    def get(self, obj_comapny: People):
        pass

    def insert(self, obj_people: People):
        try:
            session = init_db.init_database()
            session.add(obj_people)
            session.commit()
            return True, str(0)
        except Exception as ex:
            print('error occured!', str(ex))
            return False, str(ex)

    def update(self, obj_company: People):
        pass