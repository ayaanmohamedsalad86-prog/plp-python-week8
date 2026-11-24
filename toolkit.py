
# Personal Mini-Toolkit
# This program provides three useful tools.

print("Welcome to My Personal Mini-Toolkit!")

# A list to store tasks
tasks = []

# Main menu loop
while True:
    print("\n===== PERSONAL MINI-TOOLKIT =====")
    print("1. Simple Calculator")
    print("2. To-Do List")
    print("3. Number Checker")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    # Tool 1: Simple Calculator
    if choice == "1":
        print("\n--- Simple Calculator ---")

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        print("Choose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        operation = input("Enter operation (1-4): ")

        if operation == "1":
            result = num1 + num2
            print(f"The answer is {result}")
        elif operation == "2":
            result = num1 - num2
            print(f"The answer is {result}")
        elif operation == "3":
            result = num1 * num2
            print(f"The answer is {result}")
        elif operation == "4":
            if num2 != 0:
                result = num1 / num2
                print(f"The answer is {result}")
            else:
                print("Sorry, you cannot divide by zero.")
        else:
            print("Invalid operation.")

    # Tool 2: To-Do List
    elif choice == "2":
        print("\n--- To-Do List ---")
        print("1. Add a task")
        print("2. View tasks")

        task_choice = input("Choose an option: ")

        if task_choice == "1":
            new_task = input("Enter your task: ")
            tasks.append(new_task)
            print(f"Task '{new_task}' added successfully!")

        elif task_choice == "2":
            if len(tasks) == 0:
                print("Your to-do list is empty.")
            else:
                print("\nYour tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")
        else:
            print("Invalid option.")

    # Tool 3: Number Checker
    elif choice == "3":
        print("\n--- Number Checker ---")

        number = float(input("Enter a number: "))

        if number > 0:
            print(f"{number} is a positive number.")
        elif number < 0:
            print(f"{number} is a negative number.")
        else:
            print("The number is zero.")

    # Quit the program
    elif choice == "4":
        print("Thank you for using my toolkit. Goodbye!")
        break

    # Handle invalid menu choices
    else:
        print("Invalid choice. Please select a number from 1 to 4.")
