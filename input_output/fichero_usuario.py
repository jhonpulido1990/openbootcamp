#!/usr/bin/python3

def main():
    usuario = listarUsuario()
    print(usuario)

    for usuary in usuario:
        print(f"usuario: {usuary}")

def listarUsuario():
    f = open('/etc/passwd', 'r')
    datos = f.readlines()
    f.close()
    resultado = []

    for linea in datos:
        if linea[0] == '#':
            continue
        if linea[0] == '_':
            continue
        partes = linea.split(':')
        print(linea)
        print(partes[0])
        resultado.append(partes[0])
    return resultado

if __name__ == '__main__':
    main()
