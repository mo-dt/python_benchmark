import timeit

def fun():
    for i in range(100000):
        a=i*i

if __name__ == '__main__':
    timeit.timeit('fun()', 'from __main__ import fun', number=1)