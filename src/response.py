
class Response:
    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_code = response.status_code
        self.parsed_object = None

    def validate(self, schema):
        if isinstance(self.response, list):
            for item in self.response_json:
                parsed_object = schema.parse_obj(item)
                self.parsed_object = parsed_object
            else:
                schema.parse_obj(self.response_json)
            raise AssertionError("Could not map received object to pydantic schema")

    def assert_status_code(self, code):
        assert code == self.response_code, f"Status code is not equal to {code}"
