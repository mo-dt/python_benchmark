from memory_profiler import profile


@profile
def fun():
    for i in range(100000):
        a=i*i

fun()