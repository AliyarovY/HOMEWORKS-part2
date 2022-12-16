import os
from dataclasses import dataclass


@dataclass
class ChangeDir:
    dir: str

    def __enter__(self):
        self.first_dir = os.getcwd()
        os.chdir(self.dir)

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.first_dir)
