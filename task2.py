from dataclasses import dataclass


@dataclass
class ReadItems:
    file: str
    mode: str

    def __enter__(self):
        res = []
        with open(self.file, self.mode) as ff:
            for i, j in enumerate(ff):
                j = j.replace('\n', '').split(',')
                if not i:
                    keys = j
                    continue
                res.append(dict(zip(keys, j)))
        return res

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
