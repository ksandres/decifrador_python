print("ingrese el mensaje a desifrar")
mensaje= input()
print("Cuantas veces quiere mover la letra")
mover = int(input())

mensajecifrado= ""

for i in range(0, len(mensaje),1):
    letra = mensaje[i]
    minus= (letra >= 'a' and letra <= 'z')
    mayus= (letra >= 'A' and letra <= 'Z')
    if not (minus or mayus):
        mensajecifrado += letra
    else:
        ascii = ord(letra)
        baseascii = ord('a')
        if mayus:
            baseascii = ord('A')
        nuevoascii = (ascii - baseascii - mover) % 26 + baseascii
        nuevaletra = chr(nuevoascii)
        mensajecifrado += nuevaletra

    print(mensajecifrado)