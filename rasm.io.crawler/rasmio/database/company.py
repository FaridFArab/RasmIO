from rasmio.domain.company import Company
import init_db


class CompanyRepo(Company):
    def get(self, obj_comapny: Company):
        pass

    def insert(self, obj_company: Company):
        try:
            session = init_db.init_database()
            session.add(obj_company)
            session.commit()
            return True, str(0)
        except Exception as ex:
            print('error occured!', str(ex))
            return False, str(ex)

    def update(self, obj_company: Company):
        pass