from enum import Enum

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return "<Type: {}, Value {}>".format(self.type, self.value)

        
class TokenType(Enum):
    WORD, ASSIGN, INTEGER, PLUS, MINUS, MUL, DIV, EOF, RPAREN, LPAREN, LESS, GREATHER, EQUAL, NOT_EQUAL, LESS_EQ, GREATHER_EQ = (
        'WORD', 'ASSIGN', 'INTEGER', 
        'PLUS', 'MINUS', 'MUL', 'DIV', 'EOF', 
        'RPAREN', 'LPAREN', 
        'LESS', 'GREATHER', 'EQUAL', 'NOT_EQUAL',
        'LESS_EQ', 'GREATHER_EQ'
    )

