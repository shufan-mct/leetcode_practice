class Bitset:

    def __init__(self, size: int):
        self.bitset = ['0'] * size
        self.size = size
        self.ones = 0
        self.flipped = False

    def fix(self, idx: int) -> None:
        if not self.flipped:
            if self.bitset[idx] == '0':
                self.bitset[idx] = '1'
                self.ones += 1
        else:
            if self.bitset[idx] == '1':
                self.bitset[idx] = '0'
                self.ones += 1

    def unfix(self, idx: int) -> None:
        if not self.flipped:
            if self.bitset[idx] == '1':
                self.bitset[idx] = '0'
                self.ones -= 1
        else:
            if self.bitset[idx] == '0':
                self.bitset[idx] = '1'
                self.ones -= 1        

    def flip(self) -> None:
        if self.flipped:
            self.flipped = False
        else:
            self.flipped = True
        self.ones = self.size - self.ones

    def all(self) -> bool:
        return self.ones == self.size

    def one(self) -> bool:
        return self.ones

    def count(self) -> int:
        return self.ones

    def toString(self) -> str:
        if self.flipped:
            for i in range(self.size):
                if self.bitset[i] == '0':
                    self.bitset[i] = '1'
                else:
                    self.bitset[i] = '0'
            self.flipped = False
        return ''.join(self.bitset)