import sys
from pathlib import Path

if __name__ == '__main__':
    try:
        sciezka = Path(sys.argv[2])
        rozszerzenie = sys.argv[1]
        for path in sciezka.glob(f'*.{rozszerzenie}'):
            print(path.name)
    except:
        print("Blad sciezki lub rozszerzenia")
