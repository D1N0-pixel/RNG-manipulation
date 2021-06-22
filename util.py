import ctypes
from . import rng

def nextInt(seed):
    rand = rng.RNG()
    rand.setSeed(seed)
    return rand.nextInt(), rand.seed

def findFullSeed(seed1, seed2):
    for i in range(2**16):
        n, full = nextInt((ctypes.c_uint(seed1).value << 16) + i)
        if n == seed2:
            return full

def findNextRepeat(seed, want, mod):
    rand = rng.RNG()
    rand.setSeed(seed)
    i = 0
    while True:
        n = ctypes.c_uint(rand.nextInt()).value % mod
        if n == want:
            return i
        i += 1


