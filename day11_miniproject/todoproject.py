# Created a simple console-based To-Do List application using Python.

tasks=[]

while True:
    print("\nTodo")
    print("*"*20)
    print(" 1. Add Task")
    print(" 2. View Task")
    print(" 3. Remove Task")
  
    print(" 4. Exit")
    choice=int(input("Enter choice:"))
    if choice==1:
        print("\n ----- Add task -----")
        task=input("Enter task:")
        tasks.append(task)
        print("task added")
      # View Tasks
    elif choice == 2:
        print("\n----- Your Tasks -----")

        if not tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(i, ".",task)

    
    # Remove Task
    elif choice == 3:
        print("\n----- Remove Task -----")

        if not task:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(i, ".", task)

            task_number = int(input("Enter task number to remove: "))

            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print("Task removed:", removed_task)
            else:
                print("Invalid task number.")
      
        # Exit
    elif choice == 4:
        print("Thank you for using To-do list")
        break

    else:
        print("Invalid choice. Please try again.")