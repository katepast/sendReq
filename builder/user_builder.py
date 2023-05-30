from faker import Faker


class UserBuilder:
    def __init__(self):
        self.fake = Faker()
        self.response = {
            "first_name": self.fake.first_name(),
            "last_name": self.fake.last_name(),
            "company_id": self.fake.random.randint(1, 3)
        }
        self.build()

    def set_first_name(self, first_name):
        self.response["first_name"] = first_name
        return self

    def set_last_name(self, last_name):
        self.response["last_name"] = last_name
        return self

    def set_company_id(self, company_id):
        self.response["company_id"] = company_id
        return self

    def build(self):
        return self.response
