def seleciona_palavras(texto):
    palavras_longas = []
    for palavra in texto.split():
        if len(palavra) > 10:
            palavras_longas.append(palavra)
    return palavras_longas

texto = input('Digite um texto: ')
palavras_longas = seleciona_palavras(texto)

if palavras_longas:
    print(f"Palavras longas encontradas: {', '.join(palavras_longas)}")
else:
    print('Nenhuma palavra longa foi encontrada no texto.')
