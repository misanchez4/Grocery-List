#Mia Sanchez
#01-12-2024
#To-Do List #2

#Initialize
#Functions

todoList = ["milk", "eggs", "apples", "bananas", "strawberries", "butter", "cheese", "steak"]

while True:

    x = int(input("Choose a function: \n1. Add a task to the to-do list \n2. View the current to-do list \n3. Mark a task as completed \n4. Remove a task from the to-do list \n5. Remove all tasks \n6. Sort list alpabetically \n7. Count number of items on list \n8. Exit the program \n"))

    if x == 1:
        item = input("What item would you like to add?")
        todoList.append(item)

    if x == 2 : 
        print(todoList)

    if x == 3:
        task = input("Which task is completed?")
        position = int(todoList.index(task))
        todoList[position] = task + " x"

    if x == 4:
        item = input("What item would you like to delete?")
        todoList.remove(item)
    
    if x == 5:
        todoList.clear()

    if x == 6:
        todoList.sort()

    if x == 7:
        print(len(todoList))

    if x == 8:
       break
