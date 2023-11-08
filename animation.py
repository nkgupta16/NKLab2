import os
import time

frames = [
    r'''
 /\_/\
( o.o )
 > ^ <
    ''',  # Neutral
    r'''
 /\_/\
( -.- )
 > ^ <
    ''',  # Sad
    r'''
 /\_/\
( o.o )
 > . <
    ''',  # Surprised
    r'''
 /\_/\
( ^.^ )
 > ^ <
    ''',  # Happy
]

while True:
    for frame in frames:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(frame)
        time.sleep(0.5)
