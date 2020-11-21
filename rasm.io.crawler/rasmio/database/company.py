from rasmio.domain.company import Company
from rasmio.database import init_db


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

    def update(self, obj_company: Company, ):
        try:
            session = init_db.init_database()
            query = session.query(Company)
            query = query.filter(Company.Id == company_id)
            query.update({'Title': title, 'Address': address, 'Phone': phone})
            session.commit()
            session.close()
            return True, str(0)
        except Exception as ex:
            print('error occurred!', str(ex))
            return False, str(ex)