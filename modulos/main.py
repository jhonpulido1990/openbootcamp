#!/usr/bin/python3

from operaciones import suma

def main():
    mp = suma.Multiplicador()
    print(mp.multiplica(2, 3))
    print(suma.suma(2, 3))

if __name__ == '__main__':
    main()
