def ler(diretorio, arquivo):
    txt = open(diretorio + '/' + arquivo)
    return list(txt.read())


def ler_linhas(diretorio, arquivo):
    txt = open(diretorio + '/' + arquivo)
    return list(txt.readlines())