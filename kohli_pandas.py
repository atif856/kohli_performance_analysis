import pandas as pd

df = pd.read_csv("dataset.csv")

# print(df)
# print(df.head(10))

# print(df.tail(10))

# print(df.info())

# print(df.shape)

# print(df.describe())

# print(df["Opposition"].describe())

# print(df)
# print(df["Runs"].value_counts())

# new_df = df[["Runs", "4s", "6s", "Opposition"]]
# print(new_df)
# # print(new_df.describe())

# print(new_df.iloc[2])           # iloc[row indices]
# print(new_df.iloc[2:5])

# print(new_df.iloc[2:13]["6s"])

# print(new_df.iloc[3]["6s"])

# ********** printing sum of runs against australia **********
# print(df["Opposition"] == "v Australia")
vs_aussies = df[df["Opposition"] == "v Australia"]
# print(vs_aussies.head(10))

# print(vs_aussies["Runs"].sum())
# **************** OR *******************
# df1 = df[df["Opposition"] == "v Australia"]
# print(df1)
# print(df1["Runs"].sum())
#  **************************************************************

# print(vs_aussies["6s"].sum())

#  ************ printing centuries ************************
# print((df["Runs"]>=100).value_counts())
# n_df = df[(df["Runs"]>=100) == True]
# print(n_df)

# ******************* printing centuries against australia *****************

# centuries = vs_aussies[vs_aussies["Runs"]>=100]
# print(centuries)
# ------------------- OR ----------------------
centuries = df[(df["Opposition"] == "v Australia") & (df["Runs"]>=100)]
print(centuries)

#  ******************  apply function ********************************

def find_centuries(x):
    if x>= 100:
        return "OG"
    else:
        return "NOOB"

df["centuries"] = df["Runs"].apply(find_centuries)

print(df.head(5))
#  **********************           **********************************