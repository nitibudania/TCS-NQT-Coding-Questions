binary = input("enter number: ")
decimal = 0
power = 0
for digit in binary[::-1]:
    decimal+=(int(digit))*(2**power)
    power+=1
print(decimal)
# hexa = input("Enter hexadecimal number: ").upper()

# digits = {
#     'A':10,
#     'B':11,
#     'C':12,
#     'D':13,
#     'E':14,
#     'F':15
# }

# decimal = 0

# power = 0


# for ch in hexa[::-1]:

#     if ch.isdigit():

#         value = int(ch)

#     else:

#         value = digits[ch]

#     decimal += value * (16 ** power)

#     power += 1


# print("Decimal number is:", decimal)