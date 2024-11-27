import time
import sys
from pyfiglet import Figlet

def render(text):
    f = Figlet()
    print(f.renderText(text))

def play_song():
    lines = [
        ("I've been up all night", 0.06),
        ("no sleep", 0.09),
        ("Cause I feel like I'm always dreaming", 0.08),
        ("All night", 0.08),
        ("no sleep", 0.09),
        ("Cause I feel like I'm always dreaming", 0.08),
        ("Cause I feel like I'm always dreaming", 0.04),
        ("Sometimes I tend to lose myself", 0.04),
        ("When I'm out here on my own", 0.04),
        ("I never seem to get it right", 0.04),
        ("But I guess that's how it goes", 0.04),
    ]

    delays = [0.85, 0.8, 0.75, 0.7, 0.6, 11.0, 0.8, 0.8, 0.8, 0.8, 0.8]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end="")
            sys.stdout.flush()
            time.sleep(char_delay)
        time.sleep(delays[i])
        print()

render("All Night")
play_song()