from rply import ParserGenerator
from model.lexer import *
from model.ast import *


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['SCANF', 'OPEN_PAREN', 'CLOSE_PAREN', 'POINT', 'PLUS', 'COMMA', 'SEMI_COLON',
             'CONNECTION_CLASS', 'EXEC_FUNC', 'VAR', 'STRING']
        )

    def parse(self):
        @self.pg.production('program : connection scan execute')
        def program(p):
            return Program()

        @self.pg.production('connection : CONNECTION_CLASS VAR SEMI_COLON')
        def connection(p):
            return Connection()

        @self.pg.production('scan : SCANF OPEN_PAREN STRING COMMA VAR CLOSE_PAREN SEMI_COLON')
        def scan(p):
            return Scan()

        @self.pg.production('execute: VAR POINT EXEC_FUNC OPEN_PAREN STRING PLUS VAR PLUS STRING CLOSE_PAREN SEMI_COLON')
        def execute(p):
            return Execute()

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()


text_input = """
QSqlQuery query;
scanf("%s", login);
query.exec("SELECT name, salary FROM employee WHERE login = '" + login + "';");
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

variables = {}
for token in tokens:
    print(token)
for token in tokens:
    print(token)
    if (token.gettokentype() == "VAR"):
        variables.append(token.value)

print(variables)

# pg = Parser()
# pg.parse()
# parser = pg.get_parser()
# parser.parse(tokens).eval()