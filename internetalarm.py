import pygame
import pyping
import time
import datetime

def play_sound():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('internets.mp3')
    clock = pygame.time.Clock()
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        print("Playing...")
        clock.tick(1000)


def main():
    while True:
        try:
            r = pyping.ping("8.8.8.2")
            if r.ret_code == 0:
                print("{0} INTERNETS!!!! :(".format(datetime.datetime.utcnow()))
                play_sound()
                break
            else:
                print("{0} No internets now :(".format(datetime.datetime.utcnow()))
                time.sleep(10)
        except Exception as e:
            print(e)
            print("{0} No internets lookups now :(".format(datetime.datetime.utcnow()))
            time.sleep(10)

if __name__ == "__main__":
    main()
