import tkinter as tk
from tkinter import filedialog
from cpu.CPU import CPU

def main():
    print("Please write your program in a text file with each instruction on a new line.")
    print("\n\nFor example:")
    print("\nLOADI R0, 0\nHALT\n\n\n")
    input("Press Enter to open the file explorer and select your program file...")

    root = tk.Tk()
    root.withdraw()  
    file_path = filedialog.askopenfilename(title="Select program file", filetypes=[("Text Files", "*.txt")])

    if file_path:
        cpu = CPU()
        cpu.load_program_from_file(file_path)
        cpu.run()
        print("Program executed successfully.")
        print("Register contents after program execution:")
        cpu.rf.display()

        print("\nMemory contents after program execution:")
        cpu.mem.display()
    else:
        print("No file selected.")

if __name__ == "__main__":
    main()