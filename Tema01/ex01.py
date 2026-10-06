import pathlib
import numpy as np

def read_csv(path: pathlib.Path) -> list[float]:
    with open(path) as fin:
        return [token.strip() for token in fin.readline().split(',')]

studs = read_csv(pathlib.Path('list.csv'))
print([studs[stud_id] for stud_id in np.random.choice(len(studs),3,replace=False)])
