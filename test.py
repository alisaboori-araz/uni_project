

from cpu.CPU import CPU


extended_program = [
    "LOADI R1, 10",    # Load 10 into R1

    "LOADI R0, 20",    # Load 20 into R0
    "STORE R0, 0x01",    # Store R0 into 0x01
    "LOADI R0, 5",    # Load 5 into R0
    "STORE R0, 0x04",   # Store R0 into 0x04
    "LOADI R0, 100",    # Load 100 into R0
    "STORE R0, 0x06",     # Store R0 into 0x06
    "LOADI R0, 0",    # Load 0 into R0 to clear it

    "LOAD R2, 0x01",    # Load 20 into R2
    "ADD R3, R1, R2",   # R3 = R1 + R2 (30)
    "STORE R3, 0x02",   # Store R3 (30) to memory address 0x02
    "SUB R4, R2, R1",   # R4 = R2 - R1 (10)
    "STORE R4, 0x03",   # Store R4 (10) to memory address 0x03
    "LOAD R5, 0x04",    # Load 5 into R5
    "ADD R6, R3, R5",   # R6 = R3 + R5 (35)
    "STORE R6, 0x05",   # Store R6 (35) to memory address 0x05
    "BEQ R1, R2, 0x12", # Branch if R1 == R2 (should not branch)
    "JMP 0x13",         # Jump to address 0x13
    "HALT",             # This should be skipped
    "LOAD R7, 0x06",    # Load 100 into R7
    "ADD R7, R7, R6",   # R7 = R7 + R6 (135)
    "STORE R7, 0x07",   # Store R7 (135) to memory address 0x07
    "BNE R4, R5, 0x18", # Branch if R4 != R5 (should branch)
    "HALT",             # This should be skipped
    "SUB R0, R7, R6",   # R0 = R7 - R6 (100)
    "STORE R0, 0x08",   # Store R0 (100) to memory address 0x08
    "HALT"              # End program
]

# Initialize CPU and memory
cpu = CPU()


# Run the program
cpu.load_program(extended_program)
cpu.run()

# Display results
print("Register contents after program execution:")
cpu.rf.display()

print("\nMemory contents after program execution:")
cpu.mem.display()

# Verify specific results
expected_results = {
    "R0": 100,
    "R1": 10,
    "R2": 20,
    "R3": 30,
    "R4": 10,
    "R5": 5,
    "R6": 35,
    "R7": 135
}

memory_results = {
    0x02: 30,
    0x03: 10,
    0x05: 35,
    0x07: 135,
    0x08: 100
}

print("\nVerifying results:")
all_correct = True

for reg, expected in expected_results.items():
    actual = cpu.rf.read(int(reg[1]))
    if actual == expected:
        print(f"{reg} is correct: {actual}")
    else:
        print(f"{reg} is incorrect. Expected: {expected}, Got: {actual}")
        all_correct = False

for addr, expected in memory_results.items():
    actual = cpu.mem.load_data(addr)
    if actual == expected:
        print(f"Memory[0x{addr:02X}] is correct: {actual}")
    else:
        print(f"Memory[0x{addr:02X}] is incorrect. Expected: {expected}, Got: {actual}")
        all_correct = False

if all_correct:
    print("\nAll tests passed successfully!")
else:
    print("\nSome tests failed. Please check the output above for details.")