import asyncio
import sys

tasks = []

def taskSort(start, finish, B, event):
    if abs(finish - start) < 2:
        event.set()
        return
    left_event = asyncio.Event()
    right_event = asyncio.Event()
    tasks.append(asyncio.create_task(merge(B, B, start, (start+finish)//2, \
                                           finish, left_event, right_event, \
                                           event)))
    taskSort(start, (start+finish)//2, B, left_event)
    taskSort((start+finish)//2, finish, B, right_event)


async def merge(A, B, start, middle, finish, event_in1, event_in2, event_out):
    await asyncio.gather(
        event_in1.wait(),
        event_in2.wait())
    A = A.copy()
    counter = 1
    i = start
    j = middle
    k = start
    while i < middle and j < finish:
        if A[i] <= A[j]:
            B[k] = A[i]
            i += counter
        if A[i] > A[j]:
            B[k] = A[j]
            j += counter
        k += counter
    while counter:
        if i > middle:
            break
        B[k] = A[i]
        i += counter
        k += counter
    while counter:
        if j > finish:
            break
        B[k] = A[j]
        j += counter
        k += counter    
    event_out.set()

async def mtasks(A):
    B = A.copy()
    taskSort(0, len(B), B, asyncio.Event())    
    return (tasks, B)

exec(sys.stdin.read())
