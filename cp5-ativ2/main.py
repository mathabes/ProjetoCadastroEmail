import os
def validar_letra_inicial(e) -> bool:
    letras = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
    if e[0].upper() in letras:
        return True
    else:
        return False

def validar_caractere_especial(e) -> bool:
    validacao = True
    caracteres_especiais = ('[!#$%^&*()_+}{=[\-<>?~/|],;:~`')
    for x in e:
            for y in caracteres_especiais:
                if x == y:
                    validacao = False
    return validacao

def validar_arroba(e) -> bool:
    e2 = e.replace('@', 'A', 1)
    if e2.find('@') == -1:
        return True
    else:
        return False
    
def validar_quant_pontos(e) -> bool:
    e2pontos = e.replace('.', 'A', 2)
    if e.find('.') == -1 or e2pontos.find('.') != -1:
        return False
    else:
        return True
    
def validar_posicao_pontos(e) -> bool:
    e_ponto1 = e.replace('.', 'A', 1)
    posicao_ponto = e.find('.')
    if posicao_ponto - e.find('@') == 1 or e_ponto1.find('.') - posicao_ponto == 1 or posicao_ponto + 1 == len(e):
        return False
    else:
        return True


os.system('cls')
with open('RM98502.txt', 'w+', encoding='utf-8') as arq:
    while True:
        email = input("Digite o e-mail: ")
        if validar_letra_inicial(email) and validar_caractere_especial(email) and validar_arroba(email) and validar_quant_pontos(email) and validar_posicao_pontos(email):
            print('Gravado com Sucesso!')
            arq.write(email)
            break
        else:
            print("E-mail inválido, digite outro correto!")