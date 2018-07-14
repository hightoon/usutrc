#-*- coding: utf-8 -*-

""" 
unit test for network.py
"""

import sys
sys.path.insert(0, '..')


import unittest
from solution import network


class TestNetwork(unittest.TestCase):
    def test_queue_enqueue_dequeue(self):
        q = network.Queue()
        q.enqueue(2)
        assert(q.dequeue() == 2)
        assert(q.empty())

    def test_queue_dequeue_exception(self):
        q = network.Queue()
        self.assertRaises(IndexError, q.dequeue)


if __name__ == '__main__':
    unittest.main()