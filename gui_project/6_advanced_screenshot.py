import time
import keyboard
from PIL import ImageGrab


def screenshot():
    curr_time = time.strftime("_%Y%m%d_%H%M%S") #time으로 파일이름을 정할 떄 반드시 이렇게 만들 것(안하면 실행이 안됨)
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time))

keyboard.add_hotkey("a",screenshot) #사용자가 F9 키를 누르면 스크릿 샷 저장

keyboard.wait("esc") #사용자가 esc를 누를 때까지 수행