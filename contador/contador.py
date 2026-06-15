def limpar_texto(texto):
    texto = texto.lower()
    carcteres = ",.%*!|?;:\"'()[]{}"
    for char in carcteres:
        texto = texto.replace(char, "")
    return texto

def contar_palavras (frase):
    frase = limpar_texto(frase)
    if not frase.strip():
        return {}
    palavras = frase.split()
    contagem = {}
    for palavra in palavras:
        contagem[palavra] = contagem.get(palavra, 0) + 1
    return (contagem)
