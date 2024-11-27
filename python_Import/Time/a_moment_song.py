import time
import sys
from pyfiglet import Figlet

def render(text):
    print(Figlet().renderText(text))

def play_song():
    lines = [
        ["...", 1],
        ["อย่าทิ้งฉันไว้ลำพัง", 0.11],
        ["อย่าขังฉันไว้คนเดียว", 0.12],
        ["อย่าปล่อยให้ฉันต้องทุกข์ทนจมอยู่กับตัวเอง", 0.12],
        ["เพราะฉันก็มีน้ำตา", 0.2],
        ["อ่อนแอไม่แพ้กว่าใคร", 0.12],
        ["แต่กลับต้องเก็บเอาไว้ในใจ ตลอดมา", 0.15]
    ]

    delays = [0.3, 1.5, 1.9, 3.5, 1.5, 1.5, 1.2]
    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end="")
            time.sleep(char_delay)
            sys.stdout.flush()
        time.sleep(delays[i])
        print()

render("A Moment")
play_song()