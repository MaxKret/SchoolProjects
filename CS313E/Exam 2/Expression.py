#  File: Expression.py

#  Description: Evaluates a tokenized boolean expression.

#  Student Name: Maxwell Kretschmer

#  Student UT EID: mtk739

#  Course Name: CS 313E

#  Unique Number: 86610

VALID_CHARS = ['T', 'F', '&', '|', '(', ')', ' ']

class Tokenizer(object):
    def __init__(self, string):
        self.__string = string.strip()
        self.__curr_idx = 0
        self.__has_next = len(self.__string) > 0
    
    def peek(self):
        old_curr_idx = self.__curr_idx
        old_has_next = self.__has_next

        next_val = self.next()

        self.__curr_idx = old_curr_idx
        self.__has_next = old_has_next

        return next_val

    def next(self):
        if not self.has_next():
            raise ValueError('String has no additional characters to tokenize.')
        elif self.__string[self.__curr_idx] not in VALID_CHARS:
            raise ValueError('Invalid character in given string.')
        elif self.__string[self.__curr_idx] == ' ':
            self.__curr_idx += 1
            return self.next()
        else:
            self.__curr_idx += 1

            if self.__curr_idx >= len(self.__string):
                self.__has_next = False
            

            return_val = self.__string[self.__curr_idx - 1]

            if return_val == 'T':
                return_val = True
            elif return_val == 'F':
                return_val = False
            return return_val
    
    def has_next(self):
        return self.__has_next
        

class Evaluator(object):
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.tokenizerPrep = tokenizer
    
    def evaluate_expression(self):
    # FILL THIS IN: evaluate the expression given by the tokenizer and return the boolean value
        operator1 = ""
        operator2 = ""
        operand = ""
        tokens = []
        stack = []

        # POPULATE TOKEN LIST
        if self.tokenizerPrep.has_next():
            while self.tokenizerPrep.has_next():
                tokens.append(self.tokenizerPrep.next())
        else: return None

        #POPULATE STACK WHILE EVALUATING PARENTHESES
        operate = {
            "|": lambda x, y: x or y,
            "&": lambda x, y: x and y,
        }
        for i in range(len(tokens)):
            token = tokens[i]
            #OPEN PAREN
            if token == "(":
                continue
            #CLOSE PAREN
            elif token == ")":
                operator2 = stack.pop()
                operand = stack.pop()
                operator1 = stack.pop()
                stack.append(operand(operator1, operator2))
            #TOKEN IS T OR F
            elif token in [True, False]:
                stack.append(token)
            #TOKEN IS OR OR AND
            else:
                stack.append(operate[token])


        #FINAL EVALUATION OF STACK
        if len(stack) > 1:
            for i in range(0, len(stack) - 1, 2):
                stack[i + 2] = stack[i + 1](stack[i], stack[i + 2])
            return stack[-1]
        #IF RESULT ALREADY AVAILABLE, RETURN
        return stack[0]



    def parse_or(self):
        # SUGGESTED HELPER METHOD (NOT REQUIRED)
        return  
    def parse_and(self):
        # SUGGESTED HELPER METHOD (NOT REQUIRED)
        return
    def parse_paren(self):
        # SUGGESTED HELPER METHOD (NOT REQUIRED)
        return
    def parse_token(self):
        # SUGGESTED HELPER METHOD (NOT REQUIRED)
        return

def main():
    boolean_expr = input()

    print(Evaluator(Tokenizer(boolean_expr)).evaluate_expression())

if __name__ == "__main__":
    main()
