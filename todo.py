import json
from datetime import date

# check if the JSON document is empty
emptyDoc=False
taskCount=0

# f = open("todoDB.json","r")
task = {}

while True:
    with open("todoDB.json","r") as f:
        # reading the todoDB.json
        todoData = json.load(f)

    keys = list(todoData.keys())        #format the "dict keys" into list(check the keys)
    currentDate = date.today()     #checks current date

    # checking whether the user is the new user or not
    if len(todoData) == 0:
        emptyDoc = True
        username = input(
            "\nHi there!! Welcome to todoCLI, Please enter your name:  "
        )
        todoData["Name"] = username
        todoData["Date"] = str(currentDate)
        print(f"\nHey {username}! I hope you had a good start of the day, let's plan your day together\nYou can create your first task by typing create task or add task")
        print("\nType <break> or <close> to exit ")
        
        
        cmd = input(">>")
        todoData["Today"] = []

        if cmd == "create task" or cmd == "add task":
            print("\nPlease provide details about your task as per cli instructions")
            print("\nAdd time in military format i.e, if it's 9AM write 0900 or it's 9PM write 2100")
            
            # take the task description as input
            task_description = input("Please enter your task description:  ")
            scheduled_time = input("Please enter the scheduled time:  ")

            task = {
                "task_id": taskCount,
                "description": task_description,
                "scheduled_time": scheduled_time,
                "status": "TBD"
            }
            todoData["Today"].append(task)

            with open("todoDB.json", "w") as f:
                json.dump(todoData, f, indent=4)
                #(dict, file object, int[shows indentation])   save the data to todoDB.json
            taskCount = taskCount +1

        elif cmd == "break" or cmd == "close":
            break

    elif "Today" in list(todoData.keys()):
        tasks = todoData["Today"]
        username = todoData["Name"]

        print(f"\nToday is {currentDate}")
        # show the user all the existing tasks
        print(f"\nHey {username}, here are tasks of your day")
        for task in tasks:
            print(f"Task {tasks.index(task) + 1}")
            taskCount = tasks.index(task) + 1
            print("\nTask ID: ", task["task_id"])
            print("\nTask_description: ", task["description"])
            print("\nScheduled_time: ", task["scheduled_time"])
            print("\nStatus: ",task["status"])

        print("\nAdd more tasks of the day")
        print("\ntype <create task> or <add task> to add more tasks")
        print("\ntype <done> or <exit> to exit from the app")
        print("\ntype <delete user> to delete the user")
        print("\ntype <clear task> to delete the task")
        print("\ntype <mark task as done> to change the status ofv the task")

        cmd = input(">>")

        if cmd == "create task" or cmd == "add task":
            task_description = input("\nEnter  your task description: ")
            scheduled_time = input("\nEnter your scheduled_time: ")

            task = {
                "task_id": taskCount,
                "description": task_description,
                "scheduled_time": scheduled_time,
                "status": "TBD"
            }

            todoData["Today"].append(task)

            with open("todoDB.json", "r+") as f:   # r+: append the task w/o deleting the existing task
                f.seek(0)                          # f.seek(0,1,2)  0:start of the file  1: to  2: end of the file
                json.dump(todoData, f, indent=4)
            taskCount = taskCount + 1
            
            print("\nTask created successfully")
            continue

        elif cmd == "mark task as done":
            tasks = todoData["Today"]
            username = todoData["Name"]
            print(f"\nToday is {currentDate}")
            # show the user all existing tasks
            print(f"\nHey {username}, here are the tasks for your day")
            for task in tasks:
                print(f"\nTask {tasks.index(task) + 1}")
                print("\nTask description: ", task["description"])
                print("\nScheduled Time: ", task["scheduled_time"])
                print("\nStatus: ", task["status"])

            # status_cmd = input("\ntask>> ")
            task_id = int(input("\n Enter task id: "))

            for task in tasks:
                if task["task_id"] == task_id:
                    todoData["Today"][tasks.index(task)]["status"] = "DONE"
                else: 
                    continue
            
            with open("todoDB.json", "r+") as f:
                f.seek(0)
                json.dump(todoData, f, indent=4)
            continue


        elif cmd == "delete user":
            todoData = {}

            with open("todoDB.json", "w") as f:
                f.seek(0)
                json.dump(todoData, f, indent=4)
                print("\nUser deleted successfully")
            taskCount = 0
            continue

        elif cmd == "clear task":
            todoData["Today"] = []
            
            with open("todoDB.json", "w") as f:
                json.dump(todoData, f, indent=4)
                print("\nTask deleted successfully")
            taskCount = 0
            continue


        elif cmd == "done" or cmd == "exit":
            break

    

        




# print(todoData)
