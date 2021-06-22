import ctypes

class RNG:
    def __init__(self, seed=0):
        self.seed = (seed ^ 0x5DEECE66D) & ((1 << 48) - 1)

    def setSeed(self, seed):
        self.seed = seed

    def next(self, bits):
        self.seed = (self.seed * 0x5DEECE66D + 0xB) & ((1 << 48) - 1)
        return ctypes.c_int(self.seed>>(48-bits)).value

    def nextInt(self):
        return self.next(32)

    def nextIntBound(self, bound):
        if (bound <= 0):
            raise ValueError('bound must be larger than 0')
        else:
            if (bound & -bound) == bound:
                return ctypes.c_int(bound * ctypes.c_ulong(self.next(31)).value).value >> 31
            while True:
                bits = ctypes.c_uint(self.next(31)).value
                val = bits % bound
                if (bits - val + (bound-1)) >= 0:
                    break
            return val


