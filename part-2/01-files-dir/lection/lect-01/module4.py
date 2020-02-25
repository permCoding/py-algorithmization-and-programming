class WorkData():
    num_dec = 0
    num_bin = '0'

    def __init__(self, dec = 0):
        self.num_dec = dec

    def bin_to_dec(self, b):
        i = len(b) - 1
        d = 0
        for smb in b:
            d += int(smb)*2**i
            i -= 1
        return d

    def bin_to_dec_(self):
        self.num_dec = self.bin_to_dec(self.num_bin)

    def bin_to_dec_rec(self, b):
        '''
        рекурсивная функция перевода
        b(2) => d(10)
        '''
        return 0

