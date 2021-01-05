import unittest

import .src.modules.starships.services.ListStarshipsRankedService as ListStarshipsRankedService


class TestStarshipsMethods(unittest.TestCase):

    def test_list(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_ranked(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())


if __name__ == '__main__':
    unittest.main()
    