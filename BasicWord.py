from random import choice
from utils import json_responce


class BasicWord():
    __default_words = '''[{
    "word": "питон",
     "subwords":  [
         "пони", "тон", "ион", "опт", "пот", "тип", "топ", "пион", "понт"
     ]},
    {
      "word": "набор",
      "subwords":  [
          "бар", "бон", "бор", "раб", "бра", "боа", "нора", "роба", "барон"
     ]},
    {
			"word": "строка",
			"subwords": [
         "акр", "акт", "кот", "рак", "орк", "оса", "сок", "ток", "тор", "кора", 
         "коса", "сота", "торс", "роса", "скат"
     ]
}]'''

    def __init__(self):
        self.wrd_ict: dict[str, str] = choice(json_responce(self.__default_words))
        self.word = self.wrd_ict['word'].upper()
        self.subwords = [x.upper() for x in self.wrd_ict['subwords']]
        self.begin_count = self.get_count()

    def is_correct(self, version: str) -> bool:
        return version in self.subwords

    def get_count(self) -> int:
        return len(self.subwords)

    def delete_word(self, x: str) -> None:
        try:
            self.subwords.remove(x)
        except:
            return False

    def __repr__(self):
        return f'{self.word}: {self.subwords}'

    @classmethod
    def change_default_words(cls, new):
        cls.__default_words = new

    @classmethod
    def get_default_words(cls):
        return cls.__default_words
