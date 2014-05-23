from logic import GameServer
import sys
from utils import *


def render(shoe):
    return "A Shoe"


def print_option(max_size):
    sys.stdout.write("(options: ")
    for i in range(max_size):
        sys.stdout.write(chr(97 + i) + " ")
    sys.stdout.write("or s for showing the current recommendation, q for quit)\n")


def demo_start(game_server):
    while True:
        shoes = game_server.get_next_samples(2)
        print "Which of the two shoes you like better?"
        for (index, shoe) in enumerate(shoes):
            print chr(97 + index) + ":" + render(shoe)
        print_option(len(shoes))
        option = get_option(len(shoes))
        while option == -1:
            results = game_server.get_current_rank()
            for (index, shoe) in enumerate(results):
                print str(index + 1) + ":" + render(shoe)
            print_option(len(shoes))
            option = get_option(len(shoes))
        if option == -2:
            sys.exit(0)
        game_server.feed_option(shoes[option])
        print "Em..."


def get_option(max_size):
    while True:
        a = getch()
        print a
        if a == 's' or a == 'S':
            return -1
        if a == 'q' or a == 'Q':
            return -2
        if 97 <= ord(a) < 97 + max_size:
            return ord(a) - 97
        print_option(max_size)


if __name__ == '__main__':
    game_server = GameServer()
    demo_start(game_server)