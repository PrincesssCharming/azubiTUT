#Create a simple to-do list app that allows the user to add, remove
#and view tasks using loops in python
#Define an empty list to hold the tasks
#Create a loop that asks the user to enter a task and appends it to the llist
#Create a loop that displays the current list of tasks to the user
#Create a loop that allows the user to remove a task from the list
#create a loop that allows the user to exit the application

to_do = []
deleted_tasks = []
while True:
    print("Type 'add' to add a new task.")
    print("Type 'view' to see your tasks.")
    print("Type 'remove' followed by the number of the task you want to remove.")
    print("Type 'exit' to leave the application.")
    action = input().lower()
    if action == "add":
        task = input("Enter your task: ")
        if not task:
            print("You did not enter a task. Please try again.")
        else:
            to_do.append(task)
            print(f"'{task}' added to the list.")
    elif action == "view":
        if len(to_do) > 0:
            for i in range(len(to_do)):
                print(f"{i+1}. {to_do[i]}")
        else:
            print("No tasks added yet!")
    elif action.startswith("remove"):
        try:
            num = int(action[7]) - 1
            deleted_tasks.append(to_do[num])
            del to_do[num]
            print(f"'{deleted_tasks[-1]}' removed from the list.")
        except (IndexError, ValueError):
            print("Invalid task number. Please try again.")
        except IndexError:
            print("Invalid command. Please try again")
    elif action == "exit":
        break
    else:
        print("Invalid command. Please try again.")

