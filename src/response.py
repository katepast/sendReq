
class Response:
    def __init__(self, response):
        self.response = response
        self.response_json = response.json().get("data")
        self.response_code = response.status_code
        self.parsed_object = None

    def validate(self, schema):
        """
        Method for validating response with the schema
        """
        if isinstance(self.response, list):
            for item in self.response_json:
                parsed_object = schema.parse_obj(item)
                self.parsed_object = parsed_object
            else:
                schema.parse_obj(self.response_json)
            raise AssertionError("Could not map received object to pydantic schema")

    def assert_status_code(self, status_code):
        """
        Method for checking status code
        """
        if isinstance(status_code, list):
            assert self.response_code in status_code, f"Status code {self.response_code} is not equal to {status_code}"
        assert status_code == self.response_code, f"Status code {self.response_code} is not equal to {status_code}"

    def get_length_payload(self):
        return len(self.response_json)
