# def multiplier(param1,param2):
#     result=param1*param2
#     return result

# result=multiplier(param1=2,param2=3)
# print(result)

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

# emp_pin_list=[]


# for emp in employee_list:
#     emp_pin_list.append({"name": emp["Name"]})
#     print(emp_pin_list)
#     print(employee_list.index(emp))
#     emp_pin_list[employee_list.index(emp)]["pincode"]=[]

#     for address in emp["address"]:
        
#         emp_pin_list[employee_list.index(emp)]["pincode"].append(address["pincode"])
#         print("pincode: ", address["pincode"])


def get_employee_address_details(employee_list,key):
    emp_address_list=[]
    for emp in employee_list:
        emp_address_list.append({"name": emp["Name"]})
        emp_address_list[employee_list.index(emp)][key]=[]

        for address in emp["address"]:
            emp_address_list[employee_list.index(emp)][key].append(address[key])
    return emp_address_list


emp_addr_list=get_employee_address_details(employee_list,key="city")
print(emp_addr_list)