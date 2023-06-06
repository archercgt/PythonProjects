#Build a command-line task management application that allows users to create, view, update, and delete tasks. 
#Users should be able to add a task with a title and description, mark tasks as complete, and view their task list.

#Global variables definition
dict_task = {}
menu = True

#Functions definition
def main():
    while menu:
        option = input("Please enter the number of the option you want to execute:\n\
    1. Add task\n\
    2. Update task\n\
    3. Complete a task\n\
    4. View the task list\n\
    5. Exit\n")
        switch_case(option)

def switch_case(option):
    if option == '1':
        # Code for case1
        add_task()
    elif option == '2':
        # Code for case2
        update_task()
    elif option == '3':
        # Code for case3
        complete_task()
    elif option == '4':
        # Code for case3
        view_tasks()
    elif option == '5':
        # Code for case3
        global menu
        menu = False
        print("Thank, come back soon\n")
    else:
        # Code for the default case
        print("The entered option is not valid")

def add_task():
    task = input("Enter the task name: ")
    description = input("Enter the description of the task: ")
    dict_task[task] = description
    print("Task was added\n")

def update_task():
    task = input("Enter the task name: ")
    if task in dict_task:
        description = input("Enter the description of the task: ")
        dict_task[task] = description
        print("Task was updated\n")
    else: 
        print("The entered task was not found\n")

def complete_task():
    task = input("Enter the task name: ")
    if task in dict_task:
        del dict_task[task]
        print("The task was completed\n")
    else:
        print("The entered task does not exist\n")

def view_tasks():
    if len(dict_task) == 0:
        print("There are no tasks to list\n")
    else: 
        counter = 1
        print("This is the list of task: ")
        for k,v in dict_task.items():
            print("{}. Task: {}\n Description: {}".format(counter, k, v))
            counter += 1
        print("")

# Start of code
main()