""""
Lexer for Veclang
"""
import typing

import ply.lex as lex


class ConstantValue:
    """
    Object for constant value
    """

    def __init__(
            self,
            value: typing.Any,
            value_type: str
    ) -> None:
        self.value = value
        self.type = value_type


# List of token names.   This is always required
tokens = (
    # builtin types
    "INTEGER_LITERAL",
    "FLOAT_LITERAL",
    "BOOL_LITERAL",
    "STRING_LITERAL",
    "ARRAY_LITERAL",

    "TYPE",

    # operators
    "ASSIGNMENT",
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    "INTEGER_DIVISION",
    "EXPONENTIATION",

    "EQUAL",
    "NOT_EQUAL",
    "LESS_THAN",
    "LESS_THAN_OR_EQUAL",
    "GREATER_THAN",
    "GREATER_THAN_OR_EQUAL",

    "AND",
    "OR",
    "NOT",

    # control flow
    "WHILE", "ENDWHILE",
    "FOR", "ENDFOR",
    "IF",
    "ELSEIF",
    "ELSE",
    "ENDIF",
    "BREAK",
    "CONTINUE",
    "RETURN",

    # other stuff
    "LEFT_PARENTHESIS",
    "RIGHT_PARENTHESIS",

    "LEFT_SQUARE_BRACKET",
    "RIGHT_SQUARE_BRACKET",

    "COMMA",
    "DOT",
    "COLON",
    "NEWLINE",

    "COMMENT",

    "IDENTIFIER"
)

# Regular expression rules for simple tokens

t_TYPE = r"Integer|Float|Bool|String|Array"

t_ASSIGNMENT = r"<-"
t_PLUS = r"\+"
t_MINUS = r"-"
t_TIMES = r"\*"
t_DIVIDE = r"/"
t_INTEGER_DIVISION = r"//"
t_EXPONENTIATION = r"%"

t_EQUAL = "=="
t_NOT_EQUAL = "!="
t_LESS_THAN = r"\<"
t_LESS_THAN_OR_EQUAL = r"\<="
t_GREATER_THAN = r"\>"
t_GREATER_THAN_OR_EQUAL = r"\>="

t_AND = "AND"
t_OR = "OR"
t_NOT = "NOT"

t_WHILE = "WHILE"
t_ENDWHILE = "ENDWHILE"
t_FOR = "FOR"
t_ENDFOR = "ENDFOR"
t_IF = "IF"
t_ELSEIF = "ELSEIF"
t_ELSE = "ELSE"
t_ENDIF = "ENDIF"
t_BREAK = "BREAK"
t_CONTINUE = "CONTINUE"
t_RETURN = "RETURN"

t_LEFT_PARENTHESIS = r"\("
t_RIGHT_PARENTHESIS = r"\)"
t_LEFT_SQUARE_BRACKET = r"\["
t_RIGHT_SQUARE_BRACKET = r"\]"

t_COMMA = r"\,"
t_DOT = r"\."
t_COLON = r"\:"
t_NEWLINE = r"\n"

# really dodgy hack lol
t_IDENTIFIER = (
    r"\b(?!Integer\b|Float\b|Bool\b|String\b|Array\b"
    r"|AND\b|OR\b|NOT\b|WHILE\b|ENDWHILE\b|FOR\b|ENDFOR\b"
    r"|IF\b|ELSEIF\b|ELSE\b|ENDIF\b|BREAK\b|CONTINUE\b|RETURN\b)"
    r"[a-zA-Z_][a-zA-Z_0-9]*"
)


# A regular expression rule with some action code
# noinspection PyPep8Naming
# noinspection PySingleQuotedDocstring
def t_INTEGER_LITERAL(t):
    r"[+-]?\d+"
    t.value = ConstantValue(int(str(t.value)), "integer")
    return t


# noinspection PyPep8Naming
# noinspection PySingleQuotedDocstring
def t_FLOAT_LITERAL(t):
    r"[+-]?\d+\.\d+"
    t.value = ConstantValue(float(str(t.value)), "float")
    return t


# noinspection PyPep8Naming
# noinspection PySingleQuotedDocstring
def t_BOOLEAN_LITERAL(t):
    r"(true|false)"
    if t.value in {"true", "false"}:
        t.value = ConstantValue(t.value == "true", "float")
    else:
        raise ValueError("Boolean literal must be 'true' or 'false'")
    return t


# noinspection PyPep8Naming
# noinspection PySingleQuotedDocstring
def t_STRING_LITERAL(t):
    r"\".*\""
    t.value = t.value[1:-1]
    if t.value[0] == '"':
        # triple quoted
        t.value = ConstantValue(t.value[2:-2], "string")
    if '"' in t.value:
        raise ValueError("String cannot contain '\"' character.")
    return t


# noinspection PyPep8Naming
# noinspection PySingleQuotedDocstring
def t_ARRAY_LITERAL(t):
    r"(\[(\d|\d.\d|,\s*)*])|(\[(true|false|,\s*)*])|(\[(\".*\"|,\s*)*])"
    t.value = t.value[1:-1]
    if t.value[0] == '"':
        # triple quoted
        t.value = ConstantValue(t.value[2:-2], "string")
    if '"' in t.value:
        raise ValueError("String cannot contain '\"' character.")
    return t


# noinspection PyPep8Naming
# noinspection PySingleQuotedDocstring
def t_COMMENT(t):
    r"\#.*\n"
    t.value = t.value[2:]
    return t


# Define a rule so we can track line numbers
# noinspection PyPep8Naming
# noinspection PySingleQuotedDocstring
def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = "\t "


# Error handling rule
def t_error(t):
    """Error handling rule"""
    print(f"Illegal character {t.value[0]}")
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex(debug=True)


def tokenize(input_str: str) -> typing.List[lex.LexToken]:
    """Given an input str, returns a list of LexTokens."""
    lexer.lineno = 0
    lexer_tokens = []
    # Give the lexer some input
    lexer.input(input_str)

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        lexer_tokens.append(tok)
    return lexer_tokens
