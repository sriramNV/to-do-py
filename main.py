while True:
    user_choice = input("Type add, show, edit, complete or exit: ")
    user_choice = user_choice.strip()

    file = open("todos.txt", "r")
    todos = file.readlines()
    file.close()

    match user_choice:
        case "add":
            todo = input("Enter a todo: ") + "\n"

            todos.append(todo)

            file = open("todos.txt", "w")
            file.writelines(todos)
            file.close()

        case "show":
            for i, item in enumerate(todos):
                item = item.strip("\n")
                row = f"{i + 1} - {item}"
                print(row)

        case "edit":
            num = int(input("Number of todo to edit: "))
            num = num - 1
            new_todo = input("Enter new todo: ")
            todos[num] = new_todo

        case "complete":
            num = int(input("Number of todo to complete: "))
            todos.pop(num - 1)

        case "exit":
            break
