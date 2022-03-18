# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables.   This is from O'Reilly's
# "Lex and Yacc", p. 63.
# -----------------------------------------------------------------------------

import sys

sys.path.insert(0, "../..")

if sys.version_info[0] >= 3:
    raw_input = input

tokens = (
    'NAME', 'NUMBER', 'BINARY', 'OCT', 'HEX', 'STRING'
)

literals = ['=', '+', '-', '*', '/', '(', ')']

# Tokens

t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'

t_STRING = r'\"[a-zA-Z0-9_]*\"'


# def t_NUMBER(t):
#     r'[1]?\d{1,3}'
#     t.value = int(t.value)
#     return t


def t_NUMBER(t):
    r'[1-9]\d*(\.\d+)?'
    if '.' in t.value:
        t.value = float(t.value)
    else:
        t.value = int(t.value)
    return t


def t_BINARY(t):
    r'0[bB][01]+'
    t.value = int(t.value, 2)
    return t


def t_OCT(t):
    r'0[1-7][0-7]*'
    t.value = int(t.value, 8)
    return t


def t_HEX(t):
    r'0[xX][1-9a-fA-F][0-9a-fA-F]*'
    t.value = int(t.value, 16)
    return t


t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer


import lex


lex.lex()

# Parsing rules

# 结合优先级
precedence = (
    ('left', '+', '-'),  # 左结合 优先级低
    ('left', '*', '/'),  # 左结合 优先级高
    ('right', 'UMINUS'),
)

# dictionary of names
names = {}


def p_statement_assign(p):
    'statement : NAME "=" expression'
    names[p[1]] = p[3]
    p[0] = p[3]


def p_statement_string(p):
    'statement : NAME "=" string'
    names[p[1]] = p[3]
    p[0] = p[3]


def p_statement_assignCon(p):
    'statement : NAME "=" statement'
    names[p[1]] = p[3]
    p[0] = p[3]


def p_statement_expr(p):
    '''statement : expression
                 | string'''
    print(p[1])


def p_expression_binop(p):
    '''expression : expression '+' expression
                  | expression '-' expression
                  | expression '*' expression
                  | expression '/' expression'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]


def p_expression_uminus(p):
    "expression : '-' expression %prec UMINUS"
    p[0] = -p[2]


def p_expression_group(p):
    "expression : '(' expression ')'"
    p[0] = p[2]


def p_expression_number(p):
    '''expression : NUMBER
                  | BINARY
                  | OCT
                  | HEX'''
    p[0] = p[1]


def p_string_plus(p):
    '''string : string '+' expression
              | string '+' string
              | expression '+' string'''
    p[0] = '\"' + str(p[1]).strip('\"') + str(p[3]).strip('\"') + '\"'


def p_string_cheng1(p):
    '''string : expression '*' string
              | string '*' expression'''
    if isinstance(p[1], int):
        p[0] = '\"' + p[1]*p[3].strip('\"') + '\"'
    if isinstance(p[1], str):
        p[0] = '\"' + p[1].strip('\"') * p[3] + '\"'


def p_string_group(p):
    "string : '(' string ')'"
    p[0] = p[2]


def p_string_error(p):
    '''string : string '-' expression
              | string '-' string
              | expression '-' string
              | string '/' string
              | expression '/' string
              | string '/' expression
              | string '*' string'''
    print("运算不符合规则！")
    p[0] = ""


def p_string_str(p):
    "string : STRING"
    p[0] = p[1]


def p_string_name(p):
    "string : NAME"
    try:
        p[0] = names[p[1]]
    except LookupError:
        print("Undefined name '%s'" % p[1])
        p[0] = 0


def p_expression_name(p):
    "expression : NAME"
    try:
        p[0] = names[p[1]]
    except LookupError:
        print("Undefined name '%s'" % p[1])
        p[0] = 0


def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")


import yacc

yacc.yacc()

while 1:
    try:
        s = raw_input('calc > ')
    except EOFError:
        break
    if not s:
        continue
    yacc.parse(s)
