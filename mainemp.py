# from employee import employee_list,get_employee_address_details
from employee import *

# print(employee_list)
employee_addr_list=get_employee_address_details(employee_list,key="city")
print(employee_addr_list)