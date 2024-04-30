todos=[]
i=1
while True:
    useraction=input("Type Add or Show or edit or exit or complete: ").strip()
    match useraction:
        case 'add':
            todo=input("Enter the to do: ")
            todos.append(todo)
        case 'show':
            for i,items in enumerate(todos):
                print(f"{i - items}")
                
        case 'edit':
            index_edit=int(input("Enter the item to edit: "))
            new=input(f"Enter the new item instead of '{todos[index_edit-1]}': ")
            todos[index_edit-1]=new

        case 'complete':
            num=int(input("Enter the todo to complete: "))
            todos.pop(num)
            
        case 'exit':
            break