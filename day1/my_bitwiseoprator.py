# Bitwise operators perform operations on the binary (0s and 1s) representation of numbers.
# & (Bitwise AND) - > Returns 1 only if both bits are 1.
# | (Bitwise OR) -> Returns 1 if at least one bit is 1.
# ^ (Bitwise XOR) -> Returns 1 if the bits are different.
# ~ (Bitwise NOT) -> Inverts all the bits.
# << (Left Shift)->Shifts the bits to the left.
# >> (Right Shift) -> Shifts the bits to the right.


a = 6   # Binary: 0110
b = 2   # Binary: 0010

print("Bitwise AND:", a&b)

print("Bitwise OR:", a|b)

print("Bitwise XOR:", a^b)

print("Bitwise NOT:", ~a)

print("Left shift:", a<<b) #shortcut :Multiply by 2ⁿ

print("Right shift",a>>b)  #shortcut :Integer (floor) divide by 2ⁿ



