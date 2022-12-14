class MyList(list):
    def __init__(self, *ar):
        print('Работает магический метод __init__')
        self.ls = ar[~0]
        super().__init__(*ar)

    def __getitem__(self, item):
        print('Работает магический метод __getitem__')
        return self.ls[item]

    def __setitem__(self, key, value):
        print('Работает магический метод __setitem__')
        super().__setitem__(key, value)

    def __str__(self):
        print('Работает магический метод __str__')
        return super().__str__()

    def __len__(self):
        print('Работает магический метод __len__')
        return super().__len__()
