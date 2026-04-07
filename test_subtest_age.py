import unittest
from age import categorize_by_age

class TestAgeSubTest(unittest.TestCase):

    def test_child(self):
        for age in range(0, 10):
            with self.subTest(age=age):
                result = categorize_by_age(age)
                print(f"{age} is considered as a {result}.")
                self.assertEqual(result, "Child")

    def test_adolescent(self):
        for age in range(10, 19):
            with self.subTest(age=age):
                result = categorize_by_age(age)
                print(f"{age} is considered as a {result}.")
                self.assertEqual(result, "Adolescent")

    def test_adult(self):
        for age in range(19, 66):
            with self.subTest(age=age):
                result = categorize_by_age(age)
                print(f"{age} is considered as a {result}.")
                self.assertEqual(result, "Adult")

    def test_golden_age(self):
        for age in range(66, 151):
            with self.subTest(age=age):
                result = categorize_by_age(age)
                print(f"{age} is considered as a {result}.")
                self.assertEqual(result, "Golden age")


if __name__ == "__main__":
    unittest.main(verbosity=2)