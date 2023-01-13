# avengerList=["IronMan", "Captain America", "Thor"]
# # # print(avengerList, type(avengerList))
# # # print(avengerList[1])

# ratingList=[10,9,8]

# newList=[]

# for i in range(0,len(ratingList)):
#     newList.append(avengerList[i])
#     newList.append(ratingList[i])

# # print(newList)

# # # Extract the superhero and its score
# # print(newList[-2:])
# # print(newList[:2])

# avengerList[1]="Loki"
# print(avengerList)

# ------------------------- 2D LIST -----------------------------

ratedAvengerList = [
    ["Spiderman",8],
    ["Groot",7],
    ["Blackwidow",8]
]

# for i in range(len(ratedAvengerList)):
#     print(ratedAvengerList[i])

# print("\n")

# for i in range(len(ratedAvengerList)):
#     for j in range(len(ratedAvengerList[i])):
#         print(ratedAvengerList[i][j])

""" i=0: i=0,j=0->spiderman
         i=0,j=1->8
    i=1: i=1,j=0->Groot
         i=1,j=1->7
    i=2: i=2,j=0->Blackwidow
         i=2,j=1->8  
"""

# for elem in ratedAvengerList:
#     for innerElem in elem:
#         print(innerElem)

# ------------------------ Tuples(immutable) --------------------------

# avengerTuple = ("Ironman","Captain America", "Thor")
# print(avengerTuple)

# avengerTuple[2]="Loki"
# print(avengerTuple)

# ------------------ Dictionary ----------------

# avengerDict={"spiderman": 8,
#             "Groot": 7,
#             "Blackwidow": 8
#             }

# print(avengerDict)

# x = avengerDict.get("spiderman")
# print("\nspiderman score:", x)

# y=avengerDict["Groot"]
# print("\nGroot score", y)

# for i in avengerDict:
#     print(i)

# for i in avengerDict.values():
#     print(i)

# employee = {
#     "name": "atif",
#     "empid": 7,
#     "address": [
#             {
#             "line1": "chaity block",
#             "line2": "kshudiram nagar",
#             "city": "haldia",
#             "pin": 721657
#             },
#             {
#             "line1": "aaa",
#             "line2": "bbb",
#             "city": "ccc",
#             "pin": 721607
#             }  
#     ]
# }

employee_list=[
    {
    "Name": "atif",
    "empid": 7,
    "address": [
            {
            "line1": "chaity block",
            "line2": "kshudiram nagar",
            "city": "haldia",
            "pincode": 721657
            },
            {
            "line1": "aaa",
            "line2": "bbb",
            "city": "ccc",
            "pincode": 721607
            }  
    ]
},
{
    "Name": "faisal",
    "empid": 8,
    "address": [
            {
            "line1": "fff",
            "line2": "ggg",
            "city": "hhh",
            "pincode": 721543
            },
            {
            "line1": "aab",
            "line2": "bbc",
            "city": "ccd",
            "pincode": 721608
            }  
    ]
}

]

# for emp in employee_list:
#     print("\nname", emp["name"])
#     print("empid", emp["empid"])
#     for address in emp["address"]:
#         print("line1", address["line1"])
#         print("pin", address["pin"])


emp_pin = {}

# emp_pin["emp_name"] = "Tony"
# print(emp_pin)

# create a list of dictionaries containing individual employee and
# their corresponding pincodes from the above employee list

emp_pin_list = []
for emp in employee_list:
    emp_pin_list.append({"name": emp["Name"]})
    print(emp_pin_list)
    print(employee_list.index(emp))
    emp_pin_list[employee_list.index(emp)]["pincode"]=[]

    for address in emp["address"]:
        
        emp_pin_list[employee_list.index(emp)]["pincode"].append(address["pincode"])
        print("pincode: ", address["pincode"])




print(emp_pin_list)