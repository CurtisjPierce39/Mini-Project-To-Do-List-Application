to_do_tasks = []

# def welcome():

def add_task(task, priority, due_date):
    task = {
        'task': task,
        'priority': priority,
        'due date': due_date,
        'complete': False
    }
    to_do_tasks.append(task)
    print("New Task Added! :-) ")

def view_tasks():
    if len(to_do_tasks) == 0:
        print("Nothing to do!")
    for index, to_do in enumerate(to_do_tasks):
        print(f"{index + 1}. {to_do['task']} - Due: {to_do['due date']} - Priority: {to_do['priority']} - {'Complete' if to_do['complete'] else 'Incomplete'}")


def task_complete(index):
    if index >= 0 and index < len(to_do_tasks):
        to_do_tasks[index]['complete'] = True
    else:
        print("Please enter a valid task number")

def delete_task():
    if len(to_do_tasks) == 0:
        print("Nothing to delete!")

    index = int(input("Enter number of task to be removed: ")) - 1
    
    if 0 <= index < len(to_do_tasks):
        removed_task = to_do_tasks.pop(index)
        print(str(f"{removed_task} has been removed!"))

def main():
    # welcome()
    while True:
        print("Welcome to the To-Do List App! ")
        print("Menu:")
        print("1. Add a Task")
        print("2. View Tasks")
        print("3. Mark a Task as Complete")
        print("4. Delete a Task")
        print("5. Quit App")
        user_input = input("Please select an option (1/2/3/4/5): ")
    
        if user_input == '1':
            task = input("Please enter a new task: ")
            priority = input("Enter priority(1-Low, 2-Medium, 3-High)")
            due_date = input("Enter due date (mm/dd/yyyy)")
            add_task(task, priority, due_date)
        elif user_input == '2':
            view_tasks()
        elif user_input == '3':
            index = int(input("Enter number of task to be marked complete: ")) - 1
            task_complete(index)
        elif user_input == '4':
            delete_task()
        elif user_input == '5':
            print("Thank you for using the To-Do App!")
            break
        else:
            print("Not a valid entry. Please try again")

main()