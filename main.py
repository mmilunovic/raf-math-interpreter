from lexer import Lexer
from memory import Memory
from interpreters import Interpreter, PostfixInterpreter, PrefixInterpreter


INFIX, PREFIX, POSTFIX = ('INFIX', 'PREFIX', 'POSTFIX')


def main():
    memory = Memory()
    state = INFIX

    while True:
        try:
            text = input(state + ' --> ')
        except:
            break

        if not text:
            continue

        if text.lower() == 'exit':
            break

        if text.upper() in (INFIX, PREFIX, POSTFIX):
            state = text.upper()
            continue

        lexer = Lexer(text)

        if state == POSTFIX:
            interpreter = PostfixInterpreter(lexer, memory)
        elif state == PREFIX:
            interpreter = PrefixInterpreter(lexer, memory)
        else:
            interpreter = Interpreter(lexer, memory)

        result = interpreter.resolve()
        
        print(result)


if __name__ == "__main__":
    main()

