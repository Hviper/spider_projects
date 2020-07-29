import greenlet
def run1():
    print('执行代码一')
    g2.switch()
    print('执行代码二')
    g2.switch()

def run2():
    print('执行代码三')
    g1.switch()
    print('执行代码四')

g1 = greenlet.greenlet(run1)
g2 = greenlet.greenlet(run2)
g1.switch()
