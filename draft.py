#!/usr/bin/env python3

import random

coaches = ["Zenyeezus", "Fish", "Squid", "RZ", "Narwhal", "BirdLawy3r"]


def main(coaches):

    random.shuffle(coaches)
    return coaches


print(main(coaches))

if __name__ == "__main__":
    main(coaches)
