escolhe_bloco=int(input("Você Deseja Encriptar(0) ou Decriptar(1) uma palavra? "))
if escolhe_bloco==0:
    v=[]
    while True:
        try:
            alfabeto='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            palavra=input('Insira palavra a ser Encriptada: ')
            palavra=''.join(palavra.replace(' ','').upper())
            shift=int(input('Insira a semente: '))
            while shift>26:
                shift=int(input('Insira semente entre 1 e 25'))
            def encripta(k):
                return alfabeto[-k:]+alfabeto[:-k]
            alfabeto_selecionado=encripta(shift)
            for i in palavra:
                v.append(alfabeto[alfabeto_selecionado.index(i)])
            print(''.join(v))
        except ValueError:
            print('Valor Inválido,Tente Outro.')
        else:
            break
else:
    u=[]
    alfabeto='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    palavra=input('Insira a palavra a ser Decodificada ')
    palavra=''.join(palavra.replace(' ','').upper())
    pergunta=input('Você sabe a semente? S/N ')
    while pergunta!='S' and pergunta!='N':
        pergunta=input('Resposta Inválida.Insira S->(Sim) ou N->(Não): ')
    if pergunta=='S':
        semente=int(input('Qual é? '))
        novo_alfa=alfabeto[-semente:]+alfabeto[:-semente]
        for i in palavra:
            u.append(novo_alfa[alfabeto.index(i)])
        print(''.join(u))
    
    else:
        for i in range(0,25):
            novo_alfa=alfabeto[-i:]+alfabeto[:-i]
            for el in palavra:
                u.append(novo_alfa[alfabeto.index(el)])
        print('Todas as possibilidades:')
        x=len(palavra)
        y=0
        while x!=len(palavra)*25:
            sub=''.join(u[y:x])
            x+=len(palavra)
            y+=len(palavra)
            print(sub)
