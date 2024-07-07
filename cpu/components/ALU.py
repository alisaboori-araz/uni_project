class ALU:
    def operate(self, operation, operand1, operand2):
        if operation == 'ADD':
            return operand1 + operand2
        elif operation == 'SUB':
            return operand1 - operand2
        elif operation == 'AND':
            return operand1 & operand2
        elif operation == 'OR':
            return operand1 | operand2
        elif operation == 'XOR':
            return operand1 ^ operand2
        else:
            raise ValueError(f"Invalid operation: {operation}")
