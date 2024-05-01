while True:
    useraction=input("Type Add or Show or edit or exit or complete: ").strip()
    match useraction:
        case 'add':
            todo=input("Enter the to do: ") +'\n'

            file=open('todos.txt','r')
            todos=file.readlines()
            file.close()

            todos.append(todo)
            file=open('todos.txt','w')
            file.writelines(todos)
            file.close()
        case 'show':
            file=open('todos.txt','r')
            todos=file.readline()
            file.close()
            
            for index,items in enumerate(todos):
                print(f"{index+1} - {items}")
                
        case 'edit':
            index_edit=int(input("Enter the item to edit: "))
            new=input(f"Enter the new item instead of '{todos[index_edit-1]}': ")
            todos[index_edit-1]=new

        case 'complete':
            num=int(input("Enter the todo to complete: "))
            todos.pop(num-1)
            
        case 'exit':
            break