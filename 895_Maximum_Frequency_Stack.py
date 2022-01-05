class FreqStack:

    def __init__(self):
        self.VtoF = {} # value: frequency
        self.freqStair = [[]]# frequency: [value, old -> new]
        self.maxFreq = 0

    def push(self, val: int) -> None:
        freq = self.VtoF.get(val, 0) + 1
        self.VtoF[val] = freq
        if len(self.freqStair) == freq:
            self.freqStair.append([val])
        else:
            self.freqStair[freq].append(val)
        self.maxFreq = max(self.maxFreq, freq)

    def pop(self) -> int:
        num = self.freqStair[self.maxFreq].pop()
        self.VtoF[num] -= 1
        if len(self.freqStair[self.maxFreq]) == 0:
            self.maxFreq -= 1
        return num