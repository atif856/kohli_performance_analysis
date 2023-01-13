var1 = 100
var2 = 150

# mul = var1*var2
# print(mul)

def multiply():
    # global var1 = 10
    # global var2 = 20
    res = var1*var2
    return res

print(multiply())
# print(var1*var2)


# ---------------- lambda function ------------------

output = lambda var1, var2: var1*var2      
print(output(var1, var2))

