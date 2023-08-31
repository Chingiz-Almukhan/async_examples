def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g

    return inner


class CustomException(Exception):
    ...


def sub_gen() -> str:  # reader
    while True:
        try:
            message = yield
        except StopIteration:
            print("Stop iteration")
            break
        except CustomException:
            print("Yo")
            break
        else:
            print("-" * 10, message)

    return "Returned from sub_gen()"


@coroutine
def delegator(g):  # translator
    # while True:
    #     try:
    #         data = yield
    #         g.send(data)
    #     except StopIteration:
    #         ...
    #     except CustomException as e:
    #         g.throw(e) or ↓
    res = yield from g  # await
    print(res)  # output "Returned from sub_gen()"

    # example:
    #       def a():
    # ...       yield from "Chingiz"
    # ...
    # ...   >>> g = a()
    # ...   next(g)
    # ...   "C"
    # ...   next(g)
    # ...   "h" etc...
