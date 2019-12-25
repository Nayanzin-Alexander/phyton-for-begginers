print('Hello World!')

# Sinle line comment

"""
Multiline 
comment
"""


print("\nEscape Sequenceses")
print("""
    \\b - backspace
    \\a - Sound System bell
    \\n - new line
    \\t - horizontal tab
    \\' - single quotation mark
    \\" - double quotation mark
""")

print("\nString concatenation")
print("The only way to join" + " two strings")

print("\nFormatted output")
print("%15s %14s %11s" % ("Name", "Marks", "Age"))
print("%15s %14.2f %11d" % ("John Doe", 80.67, 27))

# Types of Variables
city = 'London' # A string var assigment
money = 100.75  # A floating point assigment
count = 4       # An integer assigment
a = b = c = 1   # Multiple assigment


# Data types in Python
print("\nData types in Python")

intVar = 200
print ("%30s %10d" % ("Integer: ", intVar))

longVar = 3000000000
print("%30s %10d" % ("Long: ", longVar))

float1 = 2.55e100
print("%30s %10s" % ("Float Scientific notation: ", str(float1)))

float2 = 42.0542342
print("%30s %10.5f" % ("Float: ", float2))

complexVar = complex(10, 15)
print("%30s %10s" % ("Complex: ", str(complexVar)))

boolVar = 'True'
print("%30s %10s" % ("Boolean: ", str(boolVar)))


# Arithmetic expressions
print("\nArithmetic expressions")
print("%30s %d" % ("Exponent: 3 ** 2 =", 3 ** 2))
print("%30s %d" % ("Multiplication:  3 * 2 =", 3 * 2))
print("%30s %f" % ("Division: 10 / 2 =", 10 / 2))
print("%30s %d" % ("Modulus: 10 % 3 =", 10 % 3))
print("%30s %d" % ("Addition: 10 + 1 =", 10 + 1))
print("%30s %d" % ("Substraction: 10 - 1 =", 10 - 1))


# Type conversions
print("\nType conversions")
print("%30s %d" % ("int(4.77) =", int(4.77)))
print("%30s %d" % ("long(65) =", long(65)))
print("%30s %f" % ("float(65) =", float(65)))


# Operators
print("\nOperators")

print ("\nComparison operators")
print(" ==  <  >  <=  >=  !=  <>")

print ("\nAssignment operators")
print(" =  +=  -=  *=  /=  **=")

print ("\nBitwise operators")
print("%30s %d" % ("Binary OR |", 10 - 1))