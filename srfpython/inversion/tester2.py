from srfpython.standalone.display import *
import numpy as np
from metropolis2 import *
import time

#########################################################
def test2():
    """test ND pdfs"""
    x = np.linspace(0., 1., 200)
    y = np.linspace(0., 2., 215)
    X, Y = np.meshgrid(x, y)
    #l = LogUniND([0.1, 0.1], [0.3, 0.5], k = 20.)
    #l = LogGaussND([0.2, 0.2], [0.1, 1000.], [0.1, 0.1], [0.3, 0.5], k = 20.)
    l = LogGaussNDCov([0.2, 0.2], [0.1, 0.2], [0.1, 0.1], [0.3, 0.5], rho = [[1.0, 0.9], [0.9, 1.0]], k = 20., nanbehavior=0)
    Z = l.callargs(X, Y)
    gcf().add_subplot(121)
    gca().pcolormesh(X, Y, Z)
    gcf().add_subplot(122, sharex = gca(), sharey = gca())
    gca().pcolormesh(X, Y, np.exp(Z))
    showme()


#########################################################
def test211():
    """speed test, nans expected"""
    l = LogGaussND(
        vmeans = [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2],
        vuncs  = [0.1, 0.2, 0.1, 0.2, 0.1, 0.2, 0.1, 0.2, 0.1, 0.2, 0.1, 0.2, 0.1, 0.2, 0.1, 0.2, 0.1, 0.2, 0.1, 0.2, 0.1, 0.2, 0.1, 0.2],
        vinfs  = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
        vsups  = [0.3, 0.5, 0.3, 0.5, 0.3, 0.5, 0.3, 0.5, 0.3, 0.5, 0.3, 0.5, 0.3, 0.5, 0.3, 0.5, 0.3, 0.5, 0.3, 0.5, 0.3, 0.5, 0.3, 0.5],
        k      = 20.,
        nanbehavior = 1)
    start = time.time()
    for _ in range(1000):
        l.call1([np.nan, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2])
    print(time.time() - start)

def test212():
    """speed test, no nans expected"""
    l = LogGaussND(
        vmeans=[0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2],
        vuncs=[0.1, 0.2, 0.1, 0.2, 0.1, 0.2, 0.1, 0.2, 0.1, 0.2, 0.1, 0.2, 0.1, 0.2, 0.1, 0.2, 0.1, 0.2, 0.1, 0.2, 0.1, 0.2, 0.1, 0.2],
        vinfs=[0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
        vsups=[0.3, 0.5, 0.3, 0.5, 0.3, 0.5, 0.3, 0.5, 0.3, 0.5, 0.3, 0.5, 0.3, 0.5, 0.3, 0.5, 0.3, 0.5, 0.3, 0.5, 0.3, 0.5, 0.3, 0.5],
        k=20.,
        nanbehavior=0)

    start = time.time()
    for _ in range(1000):
        l.call1(
            [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2,
             0.2, 0.2, 0.2, 0.2, 0.2])
    print(time.time() - start)


test2()
test211()
test212()
