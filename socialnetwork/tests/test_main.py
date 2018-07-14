#-*- coding: utf-8 -*-

""" 
unit test for main.py
"""

import sys
sys.path.insert(0, '..')

import unittest
from solution import main


class TestMian(unittest.TestCase):
    def test_name_to_id(self):
        people, _ = main.read_people('../data/test_data_1.txt')
        assert(people['HORACE_LAMPSHIRE'] == 0)
        assert(people['ELLSWORTH_BRILLA'] == 4)

    def test_friend_pair(self):
        _, pairs = main.read_people('../data/test_data_1.txt')
        assert(len(pairs) == 4)
        assert(pairs[3] == ['HORACE_LAMPSHIRE', 'ELLSWORTH_BRILLA'])

    def test_count_num_of_people(self):
        assert(main.count_num_of_people(main.read_people('../data/test_data_1.txt')[0]) == 5)


if __name__ == '__main__':
    unittest.main()