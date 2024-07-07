class RegisterFile:
    def __init__(self, num_registers=8, register_size=16):
        self.num_registers = num_registers
        self.register_size = register_size
        self.registers = [0] * num_registers

    def read(self, reg_num):
        if 0 <= reg_num < self.num_registers:
            return self.registers[reg_num]
        else:
            raise ValueError(f"Invalid register number: {reg_num}")

    def write(self, reg_num, data):
        if 0 <= reg_num < self.num_registers:
            self.registers[reg_num] = int(data) & ((1 << self.register_size) - 1)
        else:
            raise ValueError(f"Invalid register number: {reg_num}")
        
    def display(self):
        for i, value in enumerate(self.registers):
            print(f"R{i}: {value}")