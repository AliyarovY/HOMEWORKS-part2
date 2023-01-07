from time import sleep
from DD.BasicWord import BasicWord
from DD.Player import Player
from utils import correction


def main():
    player = Player(input('Ввведите имя игрока\n'))
    wd = BasicWord()

    def over(pl: Player):
        cnt = pl.n_used()
        print(f'Игра завершена. {pl.name}, вы угадали {cnt} {correction("слово слова слов".split(), cnt)}!\n')
        sleep(1)
        exit('(программа завершена)')

    print(f'''
    Привет, {player.name}
    Составьте {wd.get_count()} слов из слова {wd.word}
    Слова должны быть не короче {(mn := min(len(x) for x in wd.subwords))} {correction('слова слов слов'.split(), mn)}
    Чтобы закончить игру, угадайте все слова или напишите "stop"
    Программа: Поехали, ваше первое слово?\n''')

    for _ in iter(bool, 111):
        version = input().upper().strip()

        if version in ('STOP', 'СТОП'):
            over(player)

        if version == 'STAT':
            print(f'угадано : {player.n_used()}\nосталось : {wd.get_count()}\nвсего слов {wd.begin_count}\n')
            continue

        if wd.is_correct(version):
            player.add(version)
            wd.delete_word(version)
            print('верно\n')
            if player.n_used() == wd.begin_count:
                over(player)
        else:
            print('неверно\n')


if __name__ == '__main__':
    main()
