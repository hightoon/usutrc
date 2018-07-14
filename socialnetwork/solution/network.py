#-*- coding: utf-8 -*-

"""
undirected graph as model for this social network problem.

distance between A and B is calculated with BFS

"""

class Queue():
    def __init__(self):
        self._q = []

    def enqueue(self, item):
        self._q.append(item)

    def dequeue(self):
        """ we don't raise Exception here, IndexError will be raised by list """
        return self._q.pop(0)

    def empty(self):
        return self._q == []


class Person():
    def __init__(self):
        self.distance = None
        self.parent = None

class Network():
    def __init__(self, friend_pairs, name_id_map):
        self.friend_pairs = friend_pairs
        self.name_id_map = name_id_map
        self.size = len(name_id_map)
        self.adjacency_list = [[] for _ in range(self.size)]
        self._update_adjacency()

    def _update_adjacency(self):
        for pair in self.friend_pairs:
            person, adj = [self.name_id_map[name] for name in pair]
            # undirected, so a -> b ==> b -> a
            self.adjacency_list[person].append(adj)
            self.adjacency_list[adj].append(person)

    def distance(self, src_name, dest_name):
        """ get the distance between src and dest,
            it's calculated by BFS
        """
        try:
            src, dest = self.name_id_map[src_name], self.name_id_map[dest_name]
        except Exception as e:
            print('Tried to get distance for someone not in the network')
            return -1
        bfs_info = [Person() for _ in range(self.size)]
        queue = Queue()
        bfs_info[src].distance = 0
        queue.enqueue(src)
        while not queue.empty():
            root = queue.dequeue()
            for adj in self.adjacency_list[root]:
                if bfs_info[adj].distance is None:
                    bfs_info[adj].parent = root
                    bfs_info[adj].distance = bfs_info[root].distance + 1
                    queue.enqueue(adj)
                    if adj == dest:
                        return bfs_info[adj].distance
        return -1


    def __str__(self):
        return '\n'.join(['{}: {}'.format(
            person, ','.join(map(str, adj)))
            for person, adj in enumerate(self.adjacency_list)])


