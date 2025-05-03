
def multiply(n):
    digits = [int(digit) for digit in str(n)]
    prod = 1
    for digit in digits:
        prod = prod * digit
    return prod

ceil = 1000000
txt = ""
ops = {0: 0}
max_persistance = 0
for nOrigin in range(0, 100000):
    i = 0
    n = nOrigin
    txt += "-> " + str(n) + " :"
    while len(str(n)) > 1:
        n = multiply(n)
        txt += " " + str(n)
        i += 1
    # Log
    ops[nOrigin] = i
    txt += "\n"
    ## Max
    if i > max_persistance:
        max_persistance += 1

# Results
##print(txt)
## Calc max
ops_max = []
for op, persistance in ops.items():
    if persistance == max_persistance:
        ops_max.append(op)

print(f"Max={max_persistance}: ", end="")
print(ops_max)
print(f"Min-Max=" + str(min(ops_max)))



