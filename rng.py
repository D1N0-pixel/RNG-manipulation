import ctypes

class RNG:
    def __init__(self, s):
        self.seed = (s ^ 0x5DEECE66D) & ((1 << 48) - 1)

    def nextInt(self, m=2**32):
        self.seed = (self.seed * 0x5DEECE66D + 0xB) & ((1 << 48) - 1)
        return ctypes.c_int(self.seed>>16).value % m


