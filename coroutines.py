def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g

    return inner


def sub_gen():
    message = yield
    print("Subgen received: ", message)


@coroutine
def avg():
    """

    python - i coroutines.py
    g = avg()
    g.send(5)
    output 5.0
    g.send(4)
    output 4.5
    g.throw(StopIteration) or custom Exception
    output 4.5
    #  try:
    #      g.throw(StopIteration)
    #  except StopIteration as e:
    #      print("Avg: ", e.value)
    # output stop iteration
    # output Avg:  4.5

    """
    count = 0
    summ = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print("stop iteration")
            break
        except CustomException:
            print("custom exception")
            break
        else:
            count += 1
            summ += x
            average = round(summ / count, 2)
    return average


class CustomException(Exception):
    ...
