todos.append(todo)
            file=open('todos.txt','w')
            file.writelines(todos)
            file.close()