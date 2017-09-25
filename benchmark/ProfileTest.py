import profile

def fun():
    for i in range(100000):
        a=i*i

if __name__ == '__main__':
    profile.run('fun()')