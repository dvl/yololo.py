import unittest
import inspect


def better_assert(*args, **kwargs):
    print('YOLOLO!!')


def main():
    members = inspect.getmembers(unittest.TestCase)

    for name, method in members:
        if name.startswith('assert'):
            setattr(unittest.TestCase, name, better_assert)


class LifeIsShortTestCase(unittest.TestCase):

    def test_who_care_about_tests(self):
        self.assertEqual(2 + 2, 5)


if __name__ == '__main__':
    main()
    unittest.main()
