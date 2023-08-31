from time import time


def gen_filename():
    while True:
        pattern = 'file-{}.jpeg'
        t = int(time() * 1000)
        yield pattern.format(t)


# TODO Round Robin

def gen_str(s: str):
    for char in s:
        yield char


def gen_num(n: int):
    for num in range(n):
        yield num


strings_to_char = gen_str("Chingiz")
numbers = gen_num(5)

tasks = [strings_to_char, numbers]

while tasks:
    task = tasks.pop(0)

    try:
        i = next(task)
        print(i)
        tasks.append(task)
    except StopIteration:
        ...
