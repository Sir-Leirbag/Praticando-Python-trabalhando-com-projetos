def seleciona_palavras(texto):
    palavras_longas = []
    for palavra in texto.split():
        if len(palavra) > 10:
            palavras_longas.append(palavra)
    return palavras_longas

texto = input('Digite um texto: ')

if seleciona_palavras(texto):
    print(f'Palavras longas encontradas: {', '.join(seleciona_palavras(texto))}')
else:
    print('Nenhuma palavra longa foi encontrada no texto.')