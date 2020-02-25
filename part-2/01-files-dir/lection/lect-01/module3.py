class DataWork():
    num_bin = '0'
    num_dec = '0'

    def __init__(self, d = 0):
        self.num_dec = d

    def bin_to_dec(self, b):
        d = 0
        for i in range(len(b)):
            d += int(b[i])*2**(len(b)-1-i)
        return d

    def dec_to_bin(self, d):
        b = ''
        while d > 0:
            b += str(d % 2)
            d //= 2
        return b

    def dec_to_bin_(self):        
        self.num_bin = self.dec_to_bin(self.num_dec)

