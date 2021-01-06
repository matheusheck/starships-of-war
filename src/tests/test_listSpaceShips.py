import unittest

import .src.modules.starships.services.ListStarshipsRankedService as ListStarshipsRankedService


class test_starships_methods(unittest.TestCase):

    def test_list(self):
        self.isInstance(ListStarshipsRankedService(), 'FOO')

    def test_ranked(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())


if __name__ == '__main__':
    unittest.main()
    