from .Memory import Memory
from .ALU import ALU
from .RegisterFile import RegisterFile


class CPU:
    def __init__(self, memory_size=256):
        self.alu = ALU()
        self.rf = RegisterFile()
        self.mem = Memory(memory_size)
        self.pc = 0  # Program Counter
        self.halted = False

    def fetch(self):
        instruction = self.mem.load(self.pc)
        self.pc += 1
        return instruction

    def decode(self, instruction):
        parts = instruction.split()
        opcode = parts[0]
        operands = parts[1:]
        return opcode, operands

    def execute(self, opcode, operands):
        if opcode == 'ADD':
            reg_dest, reg_src1, reg_src2 = [int(op[1]) for op in operands]
            result = self.alu.operate('ADD', self.rf.read(reg_src1), self.rf.read(reg_src2))
            self.rf.write(reg_dest, result)
        elif opcode == 'SUB':
            reg_dest, reg_src1, reg_src2 = [int(op[1]) for op in operands]
            result = self.alu.operate('SUB', self.rf.read(reg_src1), self.rf.read(reg_src2))
            self.rf.write(reg_dest, result)
        elif opcode == 'LOAD':
            reg_dest = int(operands[0][1])
            address = int(operands[1], 16)
            value = self.mem.load_data(address)
            self.rf.write(reg_dest, value)
        elif opcode == 'LOADI':
            reg_dest = int(operands[0][1])
            immediate = int(operands[1])
            self.rf.write(reg_dest, immediate)
        elif opcode == 'STORE':
            reg_src = int(operands[0][1])
            address = int(operands[1], 16)
            value = self.rf.read(reg_src)
            self.mem.store_data(address, value)
        elif opcode == 'JMP':
            self.pc = int(operands[0], 16)
        elif opcode == 'BEQ':
            reg_src1, reg_src2 = int(operands[0][1]), int(operands[1][1])
            address = int(operands[2], 16)
            if self.rf.read(reg_src1) == self.rf.read(reg_src2):
                self.pc = address
        elif opcode == 'BNE':
            reg_src1, reg_src2 = int(operands[0][1]), int(operands[1][1])
            address = int(operands[2], 16)
            if self.rf.read(reg_src1) != self.rf.read(reg_src2):
                self.pc = address
        elif opcode == 'HALT':
            self.halted = True
        else:
            raise ValueError(f"Invalid opcode: {opcode}")

    def run(self):

        """ self.load_program(program)
        self.halted = False
        self.pc = 0  # Reset PC to 0
        while not self.halted and self.pc < len(program):
            # print(self.pc)
            instruction = self.fetch()
            opcode, operands = self.decode(instruction)
            self.execute(opcode, operands) """
        
        self.halted = False
        self.pc = 0
        while self.pc < len(self.mem.memory):
            instruction = self.fetch()
            if instruction == "HALT":
                break
            opcode, operands = self.decode(instruction)
            self.execute(opcode, operands)

    def load_program(self, program):
        for i, instruction in enumerate(program):
            self.mem.store_instruction(i, instruction)
            
    def load_program_from_file(self, filename):
        with open(filename, 'r') as file:
            program = [line.strip() for line in file.readlines()]
        self.load_program(program)






