#-*- coding: utf-8 -*-

""" 
unit test for network.py
"""

import sys
sys.path.insert(0, '..')


import unittest
from solution import network, main


class TestNetwork(unittest.TestCase):
    def test_queue_enqueue_dequeue(self):
        q = network.Queue()
        q.enqueue(2)
        assert(q.dequeue() == 2)
        assert(q.empty())

    def test_queue_dequeue_exception(self):
        q = network.Queue()
        self.assertRaises(IndexError, q.dequeue)

    def test_network_distance_success_dist1(self):
        map_, pairs = main.read_people('../data/test_data_1.txt')
        net = network.Network(pairs, map_)
        assert(net.distance('HORACE_LAMPSHIRE', 'JOAN_SCHWIMMER') == 1)

    def test_network_distance_success_dist2(self):
        map_, pairs = main.read_people('../data/SocialNetwork.txt')
        net = network.Network(pairs, map_)
        assert(net.distance('ARON_OHAIR', 'DEMARCUS_HAMILL') == 2)

    def test_network_distance_success_dist3(self):
        map_, pairs = main.read_people('../data/SocialNetwork.txt')
        net = network.Network(pairs, map_)
        assert(net.distance('CHARLIE_PAYTES', 'HECTOR_MICHENER') == 3)

    def test_network_distance_success_dist4(self):
        map_, pairs = main.read_people('../data/SocialNetwork.txt')
        net = network.Network(pairs, map_)
        assert(net.distance('CHARLIE_PAYTES', 'CHRISTOPER_BRAKE') == 4)

    def test_network_distance_success_dist5(self):
        map_, pairs = main.read_people('../data/SocialNetwork.txt')
        net = network.Network(pairs, map_)
        assert(net.distance('CHARLIE_PAYTES', 'SCOTTY_NEMAN') == 5)

    def test_network_distance_success_dist6(self):
        map_, pairs = main.read_people('../data/SocialNetwork.txt')
        net = network.Network(pairs, map_)
        assert(net.distance('CHARLIE_PAYTES', 'ART_DELRE') == 5)


if __name__ == '__main__':
    unittest.main()