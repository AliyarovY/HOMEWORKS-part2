class Person:

    def __init__(self, fio: str, age: int, passport: str, weight: float):
        self.is_(age, 'a')
        self.is_(passport, 'p')
        self.is_(weight, 'w')

        self.__fio = fio
        self.__age = age
        self.__passport = passport
        self.__weight = weight

    @staticmethod
    def is_fio(fio):
        for j in ['isinstance(fio, str)', 'len(fio)', 'len(fio.split()) == 3',
                  'all(x.isalpha() for x in fio.lower() if x != " ")']:
            assert eval(j), 'Fio is not correct'

    @staticmethod
    def is_(obj, now):
        if now == 'a':
            assert isinstance(obj, int) and 14 <= obj < 150, 'Are you serious?'
        if now == 'w':
            assert isinstance(obj, float) and obj > 24, 'NONONO'
        if now == 'p':
            assert isinstance(obj, str) and len(obj.split()[0]) == 4 and len(obj.split()[1]) == 6, 'danm boy...'
            assert all(x.isdigit() for x in obj if x != ' '), 'most be numeric'

    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, val):
        self.is_fio(val)
        self.__fio = val

    @fio.deleter
    def fio(self):
        print('ok')
        del self.__fio

    def prp_analog(self, arg, action, val=None):
        if action == 'get':
            return self.__dict__[f'_Person__{arg}']
        if action == 'set':
            j = self.__dict__[f'_Person__{arg}']
            self.is_(j, arg[0])
            self.__dict__[f'_Person__{arg}'] = val
