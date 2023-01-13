import pandas as pd


data = {
    "apples": [3, 4, 6, 9],
    "oranges": [1, 5, 6, 8]
}

index = ["Aaron", "Lee", "Steve", "Shawn"]
purchases = pd.DataFrame(
    data, index=index
)
# purchases = pd.DataFrame(data)     # index: 0,1,2,3,......
print(purchases)
print(type(purchases))

# print(purchases["oranges"])

print(purchases["apples"])
print(purchases.loc["Aaron"])    # loc works only if index has name 