#To do
todos=[]
while True:
    useraction=input("Type Add or Show or exit: ").strip()
    match useraction:
        case 'add':
            todo=input("Enter the to do: ")
            todos.append(todo)
        case 'show':
            for i in todos:
                print(i)
        case 'exit':
            break
