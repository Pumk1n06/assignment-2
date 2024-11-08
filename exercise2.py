import unittest
import requests

class TestAPIStatusCode(unittest.TestCase):
    def test_get_request_status_code(self):
        # Step 1: Make a GET request to the API endpoint
        response = requests.get("https://reqres.in/api/users")

        # Step 2: Validate that the response status code is 200
        if response.status_code == 200:
            print("GET request successful: Status code is 200")
        else:
            print(f"GET request failed: Status code is {response.status_code}")
        
        # Assert to ensure the test fails if the status is not 200
        self.assertEqual(response.status_code, 200, "Status code is not 200")

if __name__ == "__main__":
    unittest.main()
