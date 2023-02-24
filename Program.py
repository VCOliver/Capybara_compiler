from enum import Enum

class SyntaxKind(Enum):
    NumberToken = 'NumberToken'
    WhiteSpaceToken = 'WhiteSpaceToken'
    PlusToken = 'PlusToken'
    MinusToken = 'MinusToken'
    StarToken = 'StarToken'
    SlashToken = 'SlashToken'
    OpenParenthesisToken = 'OpenParenthesisToken'
    CloseParenthesisToken = 'CloseParenthesisToken'
    BadToken = 'BadToken'
    EOFToken = 'EOFToken'


class SyntaxToken:
    def __init__(self, position: int, text: str, kind: SyntaxKind, value):
        self.position = position
        self.text = text
        self.kind = kind
        self.value = value

class Lexer:

    position = 0
    text = ''

    current = '\0' if position >= len(text) else text[position]

    def __init__(self, text: str):
        self.text = text   

    def Next(self):
        self.position = self.position + 1

    def NextToken(self) -> SyntaxToken:

        # <numbers>
        # + - * / ()
        # <whitespace>

        if self.position >= len(self.text):
            return SyntaxToken(SyntaxKind.EOFToken, self.position, '\0', None)

        def tryParce(text):
            try:
                return int(text)
            except:
                return False


        char = self.current

        if char.isdigit():
            start = self.position

            while(char.isdigit()):
                self.Next()
                char = self.current
            
            lenght = self.position - start
            text = self.text[start:lenght]
            value = tryParce(text)
            return SyntaxToken(SyntaxKind.NumberToken, start, text, value)
        
        if char.isspace():
            start = self.position

            while(char.isspace()):
                self.Next()
                char = self.current
            
            lenght = self.position - start
            text = self.text[start:lenght]
            value = tryParce(text)
            return SyntaxToken(SyntaxKind.WhiteSpaceToken, start, text, value)
        
        if char == '+':
            return SyntaxToken(SyntaxKind.PlusToken, self.position + 1, '+', None)
        elif char == '-':
            return SyntaxToken(SyntaxKind.MinusToken, self.position + 1, '-', None)
        elif char == '*':
            return SyntaxToken(SyntaxKind.StarToken, self.position + 1, '*', None)
        elif char == '/':
            return SyntaxToken(SyntaxKind.SlashToken, self.position + 1, '/', None)
        elif char == '(':
            return SyntaxToken(SyntaxKind.OpenParenthesisToken, self.position + 1, '(', None)
        elif char == ')':
            return SyntaxToken(SyntaxKind.CloseParenthesisToken, self.position + 1, ')', None)
        
        return SyntaxToken(SyntaxKind.BadToken, self.position + 1, self.text[self.position - 1:1], None)
    
if __name__ == '__main__':
    while True:
        line = input('> ')

        if line in ['\0', ''] or line.isspace():
            exit()
        
        lexer = Lexer(line)
        while True:
            token = lexer.NextToken()
            if token.kind == SyntaxKind.EOFToken:
                break

            print(f"{token.kind}: '{token.text}'")
            if token.value != None:
                print(f" {token.value}")
            
            print()