class TodoList():

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if not isinstance(task, str):
            return

        self.tasks.append(task)


todo_list = TodoList()
tsks = 'Купить лампочку,Поменять лампочку,Выкинуть лампочку'.split(',')
for j in tsks:
    todo_list.add_task(j)

