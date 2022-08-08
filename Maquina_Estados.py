def abrirarquivo(nomearquivo):
    conteudo = []
    with open(nomearquivo, "r") as k:
        for linha in k:
            conteudo.append(linha.replace ('\n', '')) 
    return conteudo


def primeiraletra(frase):
    for letra in range(len(frase)):
        if frase [letra] == 'a':
            return recebeA(frase)
        elif frase [letra] == 'b':
            return recebeB(frase [letra], frase[letra +1: letra +3])


def recebeA(frase):
    for letra in range(len(frase)):
        if frase [letra] == 'a':
            if recebeB(frase [letra], frase[letra +1: letra +3]):
                pass
            else:
                return False
    return True


def recebeB(primeiraletra ,frase):
    if frase == 'bb' and primeiraletra == 'a':
        return True
    else:
        return False


if __name__ == "__main__":
    arquivos = ['Maquina_estado.txt','Maquina_estado2.txt','Maquina_estado3.txt']
    for arquivo in arquivos:
        print('Inicio de Leitura do Arquivo: {}'.format(arquivo))
        a = abrirarquivo(arquivo)
        parada = int(a [0])
        for elemento in range(parada):
            p = '{}: pertence'.format (a [elemento +1])
            np = '{}: não pertence'.format (a [elemento +1])
            print(p) if primeiraletra(a [elemento +1]) else print(np)