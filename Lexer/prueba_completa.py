import lexer_rules
import parser_rules

from ply.lex import lex
from ply.yacc import yacc

archivo = open("texto.txt","r")
texto = ""

for linea in archivo:
    if linea[-1] == '\n':
        linea = linea[:-1]
    texto += linea+ " "
    
lexer = lex(module=lexer_rules)
parser = yacc(module=parser_rules)
expression = parser.parse(texto, lexer)
print expression
"""
result = expression.evaluate()
print result
"""
