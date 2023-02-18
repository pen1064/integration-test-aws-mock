import unittest
from helper_functions import create_dynamodb, destroy_dynamodb


class PutDynamodbTest(unittest.TestCase):
    def setUp(self) -> None:
        self.cache_table = create_dynamodb()

    def tearDown(self) -> None:
        destroy_dynamodb()


    def test_put_function(self):
        response = self.cache_table.put_item(Item={'key': 'Canada', 'value': 30000000})
        print(response)
        self.assertEqual(response.get("ResponseMetadata").get("HTTPStatusCode"), 200)

        response1 = self.cache_table.get_item(Key={'key': 'Canada'})
        print(response1.get("Item").get("value"))


if __name__ == "__main__":
    unittest.main()
