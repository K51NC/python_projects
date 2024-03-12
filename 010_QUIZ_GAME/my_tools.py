from time import sleep

def printer(string: str, time: float=0.005):
    for char in string:
        print(char, end="", flush=True)
        sleep(time)
    print()