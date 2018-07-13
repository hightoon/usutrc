#-*- coding: utf-8 -*-

import sys

DATA_FILE = '../data/SocialNetwork.txt'


def read_people(file):
    """ read people and construct name to id dict
        name - people's name read from DATA_FILE, as string
        id - unique integer as people's identification
    """
    name_id_map = {}
    id = 0
    with open(file, 'rb') as datafile:
        for line in datafile:
            persons = line.strip('\n\r').split(',')
            for person in persons:
                if person not in name_id_map:
                    name_id_map[person] = id
                    id += 1
    return name_id_map

def count_num_of_people(people):
    return len(people)

def get_distance(src, dest):
    return 0

def print_help():
    help = """
    usage:
      python main.py count - get total number of people
      python main.py A B   - get distance between A and B
    """
    print(help)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('error: too few input parameters')
        print_help()
        raise SystemExit(1)

    if len(sys.argv) == 2 and sys.argv[1] == 'count':
        print(count_num_of_people(read_people(DATA_FILE)))
    elif len(sys.argv) == 3:
        print(get_distance(sys.argv[1], sys.argv[2]))
