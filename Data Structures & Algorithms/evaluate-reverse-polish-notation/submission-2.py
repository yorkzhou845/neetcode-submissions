class Solution:
    def calculate(self, operand1: int, operand2: int, operator: str) -> int:
        match operator:
            case "+":
                return operand1 + operand2
            case "-":
                return operand1 - operand2
            case "*":
                return operand1 * operand2
            case "/":
                #return operand1 // operand2 rounds towards negative infinity but you need rounding to 0
                return int(operand1 / operand2)
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []#hold numbers

        for item in tokens:
            if item not in "+-*/":#correctly handles negative integers
                stack.append(int(item))
            else:
                operator = item
                operand2 = stack.pop()
                operand1 = stack.pop()
                
                stack.append(self.calculate(operand1, operand2, operator))
        return stack[0]

        