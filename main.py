def readFile():
    file = open("todos.txt", "r")
    todos = file.readlines()
    file.close()
    return todos


def writeFile(todos):
    file = open("todos.txt", "w")
    file.writelines(todos)
    file.close()


while True:
    user_choice = input("Type add, show, edit, complete or exit: ")
    user_choice = user_choice.strip()

    match user_choice:
        case "add":
            todos = readFile()
            todo = input("Enter a todo: ") + "\n"
            todos.append(todo)
            writeFile(todos)

        case "show":
            todos = readFile()
            if not todos:
                print("all todos completed")
            for i, item in enumerate(todos):
                item = item.strip("\n")
                row = f"{i + 1} - {item}"
                print(row)

        case "edit":
            todos = readFile()
            num = int(input("Number of todo to edit: "))
            num = num - 1
            new_todo = input("Enter new todo: ")
            todos[num] = new_todo
            writeFile(todos)

        case "complete":
            todos = readFile()
            num = int(input("Number of todo to complete: "))
            todos.pop(num - 1)
            writeFile(todos)

        case "exit":
            break
