# pseudoparser

A work-in-progress pseudocode to Python converter.

### Pseudocode examples

```
# This is a comment

# Assignments

a <- 2
a <- 3.5
a <- "Hello"
CONSTANT TAU <- 6.28


# Types
# Integer
x <- 1
# Float
x <- 0.5
# Bool
x <- false
x <- true
# String
x <- "Hello"


# Type conversion
STRING_TO_INT("314")
STRING_TO_FLOAT("3.14")
INT_TO_STRING(314)
FLOAT_TO_STRING(3.14)
CHAR_TO_CODE("a")
CODE_TO_CHAR(97)


# String handling
LEN(x)
POSITION(x, "H")
SUBSTRING(1, 2, x)
x + ", World!"


# Random number generation
x <- RANDOM_INT(1, 5)
# Geneates random number between 1 and 5 inclusive


# Input / Output
# Get user input 
x <- USERINPUT
# Output something
OUTPUT "Hello, ", x



# Arithemetic
a <- 1 + 2
a <- 1 - 2
a <- 1 * 2
a <- 1 / 2

# Integer division
a <- 5 DIV 3
OUTPUT a
# 1

# Modulus
a <- 5 MOD 3
OUTPUT a
# 2


# Relational operators
a < b
a > b
a = b
a != b
a <= b
a >= b


# Boolean logic
a <- true
b <- false
a AND b
a OR b
NOT a


# Iteration
WHILE x
    [STATEMENTS]
    # Statements technically do not have to be indented
    # BREAK or CONTINUE keyword can be here  
ENDWHILE

FOR x <- 5 TO 10 
    [STATEMENTS]
    # Statements technically do not have to be indented
    # BREAK or CONTINUE keyword can be here 
ENDFOR

FOR x <- 5 TO 10 STEP 1
    [STATEMENTS]
    # Statements technically do not have to be indented
    # BREAK or CONTINUE keyword can be here 
ENDFOR

FOR x IN iterable
    [STATEMENTS]
    # Statements technically do not have to be indented
    # BREAK or CONTINUE keyword can be here 
ENDFOR


# Selection
IF x THEN 
    [STATEMENTS]
    # Statements do not have to be indented
ENDIF

IF x THEN 
    [STATEMENTS]
    # Statements do not have to be indented
ELSE
    [STATEMENTS]
    # Statements do not have to be indented
ENDIF

IF x THEN 
    [STATEMENTS]
    # Statements do not have to be indented
ELSE IF y THEN
    [STATEMENTS]
    # Statements do not have to be indented
ELSE
    [STATEMENTS]
    # Statements do not have to be indented
ENDIF


# Arrays
# Note: Only 1D arrays are supported

# Assignment 
array <- [1, 2, 3]

# Access element
a <- array[0]

# Update element
array[0] <- 50

# Get length of array
LEN(array)


# Records
RECORD RecordIdentifier
    field_1 : String
    field_2 : Integer
ENDRECORD

x <- RecordIdentifier(val_1, val_2)
x.field_1 <- "Hello"
OUTPUT x.field_1


# Subroutine
SUBROUTINE SubroutineIdentifier(parameters)
    [STATEMENTS]
    # Statements do not have to be indented
    # Subroutines do noy have to have a return value
    RETURN "Hello, World"
ENDSUBROUTINE

x <- SubroutineIdentifier()

```
