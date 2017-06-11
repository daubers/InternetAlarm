import pygame
import pyping
import time
import datetime
import argparse


def play_sound(sound_file):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    clock = pygame.time.Clock()
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        print("Playing...")
        clock.tick(1000)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mp3file", type=str,
                        help="Music file to play")
    parser.add_argument("ping_location", type=str,
                        help="Location to ping")
    args = parser.parse_args()
    while True:
        try:
            r = pyping.ping(args.ping_location)
            if r.ret_code == 0:
                print("{0} INTERNETS!!!! :(".format(datetime.datetime.utcnow()))
                play_sound(args.mp3file)
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
