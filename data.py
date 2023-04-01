#!/usr/bin/env python
from json import loads


def Data(msg):
    dict = loads(msg)
    #dict = msg
    """@dataclass
    class Game:
        mode: str = dict['mode']
        time_limit: int = dict['time_limit']
        players: list = dict['players']
        dob: list = dict['dob']"""
    mode: str = dict['mode']
    time_limit: int = dict['time_limit']
    players: list = dict['players']
    dob: list = dict['dob']
    print(mode)
    print(time_limit)
    print(players)
    print(dob)

    return mode, time_limit, players, dob


if __name__ == "__main__":
    Data(msg)
