import sys

def main():
    sortedList = []
    try:
        sortedList = list(map(int, sys.argv[1:]))
        sortedList.sort()
        print(sortedList)
    except ValueError:
        print("Blad podanych parametrow!")
    return sortedList

if __name__ == '__main__':
    main()
