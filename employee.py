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

def get_employee_address_details(employee_list,key):
    emp_address_list=[]
    for emp in employee_list:
        emp_address_list.append({"name": emp["Name"]})
        emp_address_list[employee_list.index(emp)][key]=[]

        for address in emp["address"]:
            emp_address_list[employee_list.index(emp)][key].append(address[key])
    return emp_address_list