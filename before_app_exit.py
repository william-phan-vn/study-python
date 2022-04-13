import atexit
import time


def exit_handler():
    print('My application is ending!')


atexit.register(exit_handler)

if __name__ == "__main__":
    print('APP START')
    time.sleep(3)
    print('APP END')
