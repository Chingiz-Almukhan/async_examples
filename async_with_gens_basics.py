from time import sleep

queue = []


def counter():
    _counter = 0
    while True:
        print(_counter)
        _counter += 1
        yield


def printer():
    _counter = 0
    while True:
        if _counter % 3 == 0:
            print("Bang")
        _counter += 1
        yield


def main():
    while True:
        g = queue.pop(0)
        next(g)
        queue.append(g)
        sleep(0.5)


if __name__ == "__main__":
    g_1 = counter()
    queue.append(g_1)
    g_2 = printer()
    queue.append(g_2)
    main()
