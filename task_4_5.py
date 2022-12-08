import datetime


class Task:
    def __init__(self, content):
        self.content = content
        self.date = ' (coздано ' + str(datetime.datetime.now()).split('.')[0] + ')'

    def __setattr__(self, key, value):
        assert isinstance(value, str)
        object.__setattr__(self, key, value)

    def __hash__(self):
        return hash(self.content)

    def __eq__(self, other):
        return hash(self.content) == hash(other.content)

    def __str__(self):
        return self.content + self.date

    def __bool__(self):
        return bool(self.content)

    def __repr__(self):
        return self.content + self.date


class ToDoList:
    def __init__(self):
        self.tasks = []
        self.i = -1

    def __str__(self):
        return str(self.tasks)

    def __setitem__(self, key, value):
        self.tasks += (key >= len(self.tasks)) * [None] * (key - len(self.tasks) + 1)
        self.tasks[key] = value

    def __delitem__(self, key):
        del self.tasks[key]

    def __iter__(self):
        return self

    def __len__(self):
        return len(self.tasks)

    def __next__(self):
        if self.i + 1 < len(self.tasks):
            self.i += 1
            return self.tasks[self.i]
        else:
            raise StopIteration
