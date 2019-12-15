class Memory(list):
    def __setitem__(self, index, value):
        if index >= len(self):
            self.extend([0] * (index - len(self) + 1))
        super().__setitem__(index, value)
    
    def __getitem__(self, index):
        if index >= len(self):
            self.extend([0] * (index - len(self) + 1))
            return 0
        return super().__getitem__(index)

class Intcode():
    def __init__(self, memory, inputs=None):
        self.m = Memory(list(memory))
        if inputs is None:
            inputs = []
        self.inputs = inputs
        self.outputs = []
        self.finished = False
        self.ptr = 0
        self._rel_base = 0

    def run(self):
        while True:
            opcode, m1, m2, m3 = self._parse_modes(self.m[self.ptr])
            if opcode == 1:
                self.m[self._get(m3, self.ptr+3)] = self._get_val(m1, self.ptr+1) + self._get_val(m2, self.ptr+2)
                self.ptr = self.ptr + 4
            elif opcode == 2:
                self.m[self._get(m3, self.ptr+3)] = self._get_val(m1, self.ptr+1) * self._get_val(m2, self.ptr+2)
                self.ptr = self.ptr + 4
            elif opcode == 3:
                if not self.inputs:
                    return
                self.m[self._get(m1, self.ptr+1)] = self.inputs[0]
                self.inputs.pop(0)
                self.ptr = self.ptr + 2
            elif opcode == 4:
                self.outputs.append(self._get_val(m1, self.ptr+1))
                self.ptr = self.ptr + 2
            elif opcode == 5:
                if self._get_val(m1, self.ptr+1) != 0:
                    self.ptr = self._get_val(m2, self.ptr+2)
                else:
                    self.ptr = self.ptr + 3
            elif opcode == 6:
                if self._get_val(m1, self.ptr+1) == 0:
                    self.ptr = self._get_val(m2, self.ptr+2)
                else:
                    self.ptr = self.ptr + 3
            elif opcode == 7:
                if self._get_val(m1, self.ptr+1) < self._get_val(m2, self.ptr+2):
                    self.m[self._get(m3, self.ptr+3)] = 1
                else:
                    self.m[self._get(m3, self.ptr+3)] = 0
                self.ptr = self.ptr + 4
            elif opcode == 8:
                if self._get_val(m1, self.ptr+1) == self._get_val(m2, self.ptr+2):
                    self.m[self._get(m3, self.ptr+3)] = 1
                else:
                    self.m[self._get(m3, self.ptr+3)] = 0
                self.ptr = self.ptr + 4
            elif opcode == 9:
                inc = self._get_val(m1, self.ptr+1)
                assert( self._rel_base + inc > 0)
                self._rel_base = self._rel_base + inc
                self.ptr = self.ptr + 2
            elif opcode == 99:
                self.finished = True
                return
            else:
                raise Exception("Invalid opcode")

    def _get_val(self, mode, value):
        return self.m[self._get(mode, value)]

    def _get(self, mode, value):
        if mode == 0:
            return self.m[value]
        elif mode == 2:
            return self._rel_base + self.m[value]
        else:
            return value

    def _parse_modes(self, code):
        opcode = code % 100
        mode1 = (code // 100) % 10
        mode2 = (code // 1000) % 10
        mode3 = (code // 10000) % 10
        return opcode, mode1, mode2, mode3