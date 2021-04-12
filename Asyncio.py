import asyncio
# import time
import functools
from asyncio import CancelledError
from asyncore import loop
from datetime import datetime
from socket import timeout
from turtle import done

"""async def display_date(s):
    loop = asyncio.get_running_loop()
    end_time = loop.time() + s
    while True:
        print(datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)

async def main(sleep, say):
    for i in range(5):
        await asyncio.sleep(sleep, result=True)
        print(say + str(i + 1))

async def main2(sleep, say):
    for i in range(5):
        await asyncio.sleep(sleep)
        print(say + str(i + 1))"""

# Python 3.7+
"""async def mainly():"""
# print(f"Started at {time.strftime('%X')}")

# Forma de crear tareas
"""task1 = asyncio.create_task(
    main(3, 'hello'),
    name='Tarea1'
)
task2 = asyncio.ensure_future(
    main2(2, 'world')
)"""

"""    task3 = asyncio.create_task(
        display_date(50)
    )
"""
    # print(task1.get_name())

    # await task1
    # await task2
"""    await task3"""

# Forma con await

"""await main(1, 'hello')
await main2(1, 'world')"""

    # print(f"Finished at {time.strftime('%X')}")

"""asyncio.run(mainly())"""
# Forma de llamar con Run
"""asyncio.run(main(1, 'hello'))
asyncio.run(main2(1, 'world'))"""

"""class Exep(Exception):
    pass

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(0.5)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")

async def cancelar(t):
    return t.cancel()
    # pass

async def main():
    # Schedule three calls *concurrently*:
    try:
        f = asyncio.ensure_future(factorial("C", 4))
        f.add_done_callback(
            functools.partial(print, 'finished the')
        )
        # f.remove_done_callback(print)
        print(f.get_loop())
        await asyncio.gather(
            # cancelar(f),
            factorial("A", 2),
            asyncio.shield(factorial("B", 3)),
            asyncio.wait({f}, timeout=10),
            return_exceptions=False
        )
        if f.done():
            print('Done')
        elif asyncio.as_completed(f):
            print(f.__str__())
        else:
            print('Not Done')
    except ZeroDivisionError:
        print('Huge mistake')
    except asyncio.TimeoutError:
        print('Timeout')
    finally:
        if CancelledError:
            print('f cancelled!!')
        else:
            print(f.result())
        print('Final', f)

asyncio.run(main())"""

# --------------------------------------------------------

# Create a coroutine
"""async def dormir():
    return await asyncio.sleep(1, result=3)

coro = dormir()

# Submit the coroutine to a given loop
future = asyncio.run_coroutine_threadsafe(coro, loop)

# Wait for the result with an optional timeout argument
assert future.result(timeout) == 3

try:
    result = future.result(timeout)
except asyncio.TimeoutError:
    print('The coroutine took too long, cancelling the task...')
    future.cancel()
except Exception as exc:
    print(f'The coroutine raised an exception: {exc!r}')
else:
    print(f'The coroutine returned: {result!r}')"""


"""import asyncio
import threading
import time


async def coro_func():
    return await asyncio.sleep(3, 42)


def another_thread(_loop):
    coro = coro_func()  # is local thread coroutine which we would like to run in another thread

    # _loop is a loop which was created in another thread

    future = asyncio.run_coroutine_threadsafe(coro, _loop)
    print(f"{threading.current_thread().name}: {future.result()}")
    time.sleep(15)
    print(f"{threading.current_thread().name} is Finished")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    main_th_cor = asyncio.sleep(10)
    # main_th_cor  is used to make loop busy with something until another_thread will not send coroutine to it
    print("START MAIN")
    x = threading.Thread(target=another_thread, args=(loop, ), name="Some_Thread")
    x.start()
    time.sleep(1)
    loop.run_until_complete(main_th_cor)
    print(asyncio.all_tasks.__str__())
    print("FINISH MAIN")"""

async def cancel_me():
    print('cancel_me(): before sleep')

    try:
        # Wait for 1 hour
        await asyncio.sleep(3600)
    except asyncio.CancelledError:
        print('cancel_me(): cancel sleep')
        raise
    finally:
        print('cancel_me(): after sleep')

async def main():
    # Create a "cancel_me" Task
    task = asyncio.create_task(cancel_me())

    # Wait for 1 second
    await asyncio.sleep(1)

    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("main(): cancel_me is cancelled now")

asyncio.run(main())
