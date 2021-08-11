from multiprocessing import Queue
import multiprocessing


def func(a, q):
    for i in a:
        q.put(i * i)


if __name__ == '__main__':
    q = Queue()
    bp = multiprocessing.Process(target=func, args=([5, 6, 7], q))
    bp.start()
    bp.join()
    while q.empty() is False:
        print(q.get())