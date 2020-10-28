import sys
from pathlib import Path

def listSubFilDir(sciezka,separator):
    separator = separator.replace("-", " ")
    separator = separator + '|---'
    print(f'{separator}{sciezka.name}')
    for path in sciezka.glob('*'):
        listSubFilDir(Path(path), separator)

def listStrFilDir(sciezka):
    print(f'{sciezka}')
    separator = '----'
    for path in sciezka.glob('*'):
        listSubFilDir(Path(path),separator)

if __name__ == '__main__':
    try:
        listStrFilDir(Path(sys.argv[1]))
    except:
        print('Blad sciezki')