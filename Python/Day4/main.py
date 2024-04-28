todos=[]
while True:
    useraction=input("Type Add or Show or edit or exit: ").strip()
    match useraction:
        case 'add':
            todo=input("Enter the to do: ")
            todos.append(todo)
        case 'show':
            for i in todos:
                print(i)
        case 'edit':
            index_edit=int(input("Enter the item to edit: "))
            new=input(f"Enter the new item instead of '{todos[index_edit-1]}': ")
            todos[index_edit-1]=new
        case 'exit':
            break