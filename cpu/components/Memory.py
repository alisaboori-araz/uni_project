class Memory:
    def __init__(self, size):
        self.size = size
        self.memory = [0] * size
        self.program = []

    def load(self, address):
        if 0 <= address < len(self.program):
            return self.program[address]
        else:
            raise ValueError(f"Invalid instruction address: {address}")

    def load_data(self, address):
        if 0 <= address < self.size:
            return self.memory[address]
        else:
            raise ValueError(f"Invalid data memory address: {address}")

    def store_instruction(self, address, instruction):
        if 0 <= address < self.size:
            if address >= len(self.program):
                self.program.extend([None] * (address - len(self.program) + 1))
            self.program[address] = instruction
        else:
            raise ValueError(f"Invalid instruction address: {address}")

    def store_data(self, address, data):
        if 0 <= address < self.size:
            self.memory[address] = data
        else:
            raise ValueError(f"Invalid data memory address: {address}")

    def display(self):
        print("Instructions:")
        for i, instruction in enumerate(self.program):
            print(f"Address {i}: {instruction}")
        print("\nData:")
        for i, value in enumerate(self.memory):
            if value != 0:
                print(f"Address {i}: {value}")