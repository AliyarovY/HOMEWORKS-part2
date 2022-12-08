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
