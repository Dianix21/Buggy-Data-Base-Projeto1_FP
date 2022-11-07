"""Projeto realizado por: Diana Goulao ist1102531
este projeto tem como grande objetivo descodificar uma base de dados que se encontra encriptada e corrompida, para isso procedece a 5 etapas:
    Etapa 1 - correcao da documentacao
    Etapa 2 - descoberta do PIN
    Etapa 3 - verificacao de dados
    Etapa 4 - desencriptacao de dados
    Etapa 5 - depuracao de senhas"""


def corrigir_palavra(surto):
    """corrigir_doc: cad. caracteres ---> cad. caracteres
    esta funcao recebe uma string e devolve a string corrigida, onde sao retirados surtos de letras (pares minuscula/maiuscula)"""

    i = 0
    while i < len(surto) - 1:
        # para cada caracter da string recebida verifica se esse caracter e o seguinte formam um par minuscula/maiuscula apagando esse par se se verifica a igualdade
        if ((ord(surto[i]) == ord(surto[i + 1]) - 32) or (ord(surto[i]) == ord(surto[i + 1]) + 32)):
            surto = surto[:i] + surto[i + 2:]
            i = 0
        else:
            i += 1

    return surto


def eh_anagrama(palavra1, palavra2):
    """eh_anagrama: cad. caracteres x cad. caracteres ---> booleano
    esta funcao recebe duas palavras e retorna o valor logico da sua igualdade, verifica se sao anagramas"""

    # se o somatorio dos numeros correspondentes na tabela de ASCII for igual para duas palavras essas sao anagramas
    return sum([ord(x) for x in palavra1.lower()]) == sum([ord(x) for x in palavra2.lower()])


def corrigir_doc(doc):
    """corrigir_doc: cad. caracteres ---> cad. caracteres
    recebe uma string e devolve-a com os surtos de letras e anagramas retirados, com recurso as funcoes acima definidas"""

    # validacao dos argumentos
    if not (type(doc) == str and len(doc) >= 1):
        raise ValueError("corrigir_doc: argumento invalido")
    if not all(97 <= ord(doc[i]) <= 122 or 65 <= ord(doc[i]) <= 90 or ord(doc[i]) == 32 for i in range(len(doc)-1)): #garantir que so sao permitidas letras minusculas/maiusculas e espacos
        raise ValueError("corrigir_doc: argumento invalido")
    if any(ord(doc[i]) == 32 and ord(doc[i+1]) == 32 for i in range(len(doc)-1)): # verificar se exitem dois espacos seguidos
        raise ValueError("corrigir_doc: argumento invalido")
    doc = corrigir_palavra(doc)
    lista_palavras = doc.split()
    for i in range(len(lista_palavras)):  # indice que precorrera da esquerda para a direita
        # indice que precorrera a lista ao contrario de modo a que quando um anagrama e retirado nao haja alteracao de indices
        for j in range(len(lista_palavras)-1, i, -1):
            if lista_palavras[i].lower() != lista_palavras[j].lower():
                if eh_anagrama(lista_palavras[i], lista_palavras[j]):
                    del lista_palavras[j]

    return " ".join(lista_palavras)


def obter_posicao(direcao, pos_atual):
    """obter_posicao: cad. caracteres x inteiro ---> inteiro
    recebe um caracter correrspondente a um movimento e a posicao inicial e devolve o digito final depois do movimento"""

    if direcao == "C":
        if (pos_atual == 1 or pos_atual == 2 or pos_atual == 3):
            pos_final = pos_atual
        else:
            pos_final = pos_atual-3
    elif direcao == "B":
        if (pos_atual == 7 or pos_atual == 8 or pos_atual == 9):
            pos_final = pos_atual
        else:
            pos_final = pos_atual+3
    elif direcao == "E":
        if (pos_atual == 1 or pos_atual == 4 or pos_atual == 7):
            pos_final = pos_atual
        else:
            pos_final = pos_atual-1
    else:
        if (pos_atual == 3 or pos_atual == 6 or pos_atual == 9):
            pos_final = pos_atual
        else:
            pos_final = pos_atual+1

    return pos_final


def obter_digito(direcoes, pos_atual):
    """obter_digito: cad. caracteres x inteiro ---> inteiro
    recebe uma sequencia de movimentos e a posicao inicial e devolve a posicao final depois de executar os movimentos"""

    pos = pos_atual
    for l in direcoes:
        pos = obter_posicao(l, pos)

    return pos


def obter_pin(tuplo):
    """obter_pin: tuplo ---> tuplo
    recebe um tuplo com varias sequencias de movimentos e devolve o pin final, cada digito do pin e dado por uma das
    sequencias de movimentos sendo o que o primeiro comeca no 5 e os restantes no digito resultante do movimento anterior"""

    if not (type(tuplo) == tuple and 4 <= len(tuplo) <= 10 and all(len(x) > 1 for x in tuplo)):
        raise ValueError("obter_pin: argumento invalido")
    
    for i in range(len(tuplo)-1):
        if not all(tuplo[i][c] in ("C", "E", "B", "D") for c in range(len(tuplo[i]))):
            raise ValueError("obter_pin: argumento invalido")

    tuplo_pin = ()
    pos = 5
    for sequencia in tuplo:
        tuplo_pin = tuplo_pin + (obter_digito(sequencia, pos),)
        for l in sequencia:
            pos = obter_posicao(l, pos)

    return tuplo_pin
    

def eh_entrada(entrada):
    """eh_entrada: universal ---> booleano
    esta funcao recebe um argumento e devolve se corresponde a uma entrada da BDB conforme descrito"""

    # verificar entrada
    if not (type(entrada) == tuple and len(entrada) == 3):
        return False

    # verificar cifra
    if not (type(entrada[0]) == str and len(entrada[0]) >= 1 and all(97 <= ord(entrada[0][i]) <= 122 or (ord(entrada[0][i]) == 45 and ord(entrada[0][i+1]) != 45) for i in range(len(entrada[0])-1)) and ord(entrada[0][0]) != 45 and ord(entrada[0][len(entrada[0])-1]) != 45): 
        return False
    
    #for i in range(len(entrada[0])-1):
    if any(48 <= ord(entrada[0][i]) <= 57 for i in range(len(entrada[0])-1)):
        return False

    # verificar checksum
    if not (type(entrada[1]) == str and len(entrada[1]) == 7 and entrada[1][1:6].islower() and ord(entrada[1][0]) == 91 and ord(entrada[1][6]) == 93):

        return False

    # verificar tuplo
    if not(type(entrada[2]) == tuple and len(entrada[2]) >= 2 and all(type(n) == int for n in entrada[2]) and all(n >= 0 for n in entrada[2])):

        return False

    return True


def bubblesort(d):
    """bubblesort: dicionario ---> lista
    esta funcao recebe um dicionario e devolve uma lista ordenada por ordem crescente das chaves do dicionario"""

    chaves = list(d.keys())
    valores = list(d.values())
    changed = True
    size = len(d) - 1
    while changed:
        changed = False
        for i in range(size):
            if valores[i] > valores[i+1] or (valores[i] == valores[i+1] and chaves[i+1] > chaves[i]):
                valores[i], valores[i+1] = valores[i+1], valores[i]
                chaves[i], chaves[i+1] = chaves[i+1], chaves[i]
                changed = True
        size = size - 1
    return chaves


def validar_cifra(cifra, checksum):
    """validar_cifra: cad. carateres × cad. carateres ---> booleano
    esta funcao recebe uma cifra e um checksum e devolve o valor logico da sua igualdade, depois da correcao da cifra"""

    d = {}
    for c in cifra:
        if c == "-":
            continue
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    cifraordenada = bubblesort(d)
    cifraordenada.reverse()
    return("["+"".join(cifraordenada[:5])+"]") == checksum


def filtrar_bdb(lst):
    """filtrar_bdb: lista ---> lista
    esta funcao recebe uma lista de entradas e devolve a lista das entradas que nao sao validas"""

    if not (type(lst) == list and len(lst) >= 1 and all(eh_entrada(entrada) for entrada in lst)):
        raise ValueError("filtrar_bdb: argumento invalido")
    listafinal = []
    for entrada in lst:
        if not validar_cifra(entrada[0], entrada[1]):
            listafinal += [entrada]

    return listafinal


def obter_num_seguranca(tuplo):
    """obter_num _seguranca: tuplo ---> inteiro
    recebe um tuplo de inteiros e retorna o inteiro correspondente a menor subtracao entre cada dois numeros"""

    sub_menor = abs(tuplo[0]-tuplo[len(tuplo)-1])
    for i in range(len(tuplo)):
        for j in range(len(tuplo)-1, i, -1):
            subtracao = abs(tuplo[i]-tuplo[j])
            if subtracao < sub_menor:
                sub_menor = subtracao

    return sub_menor


def decifrar_texto(entrada, num_seguranca):
    """decifrar_texto: cad. carateres × inteiro ---> cad. carateres
    esta funcao recebe um entrada e um numero de seguranca e devolve a string da cifra corrigida"""

    while num_seguranca > 26:
        num_seguranca -= 26
    lst = []
    for i in range(len(entrada)):
        n = 0
        if ord(entrada[i]) != 45:
            if i % 2 == 0:
                n = num_seguranca + 1
                resto = 122-ord(entrada[i])
                if resto > n:
                    letra_final = chr(ord(entrada[i])+n)
                elif abs(n-resto) == 0:
                    letra_final = chr(122)
                else:
                    alteracao = abs(n-resto)
                    letra_final = chr(96+alteracao)
                lst += letra_final
            else:
                n = num_seguranca-1
                resto = 122-ord(entrada[i])
                if resto > n:
                    letra_final = chr(ord(entrada[i])+n)
                elif abs(n-resto) == 0:
                    letra_final = chr(122)
                else:
                    alteracao = abs(n-resto)
                    letra_final = chr(96+alteracao)
                lst += letra_final
        else:
            lst += chr(32)

    return "".join(lst)


def decifrar_bdb(lst):
    """decifrar_bdb: lista ---> lista
    esta funcao recebe uma lista de entradas e devolve uma lista das cifras corrigidas"""

    if not (type(lst) == list and len(lst) >= 1 and all(eh_entrada(entrada) for entrada in lst)):
        raise ValueError("decifrar_bdb: argumento invalido")

    lstres = []
    for i in lst:
        lstres += [decifrar_texto(i[0], obter_num_seguranca(i[2]))]

    return lstres


def eh_utilizador(arg):
    """eh_utilizador: universal ---> booleano
    esta funcao recebe um argumento e devolve o valor logico correspondete a sua validade enquanto
    um dicionario que contem a informacao de utilizador relevante da BDB conforme descrito"""

    # validacao argumento
    if not (type(arg) == dict and len(arg) == 3):
        return False
        
    # validacao da informacao de utilizador relevante da BDB
    if not ("name" in arg and "pass" in arg and "rule" in arg):
        return False
    if not (type(arg["name"]) == str and type(arg["pass"]) == str and type(arg["rule"]) == dict):
        return False
    if not (len(arg["name"]) >= 1 and len(arg["pass"]) >= 1 and len(arg["rule"]) == 2):
        return False
    if not ("vals" in arg["rule"] and "char" in arg["rule"]):
        return False
    if not (type(arg["rule"]["vals"]) == tuple and len(arg["rule"]["vals"]) == 2 and arg["rule"]["vals"][0] > 0 and arg["rule"]["vals"][1] > 0 and arg["rule"]["vals"][0] <= arg["rule"]["vals"][1] and type(arg["rule"]["char"]) == str and len(arg["rule"]["char"]) == 1):
        return False
        
    return True


def eh_senha_valida(senha, regra_individual):
    """eh_senha_valida: cad. carateres × dicionario ---> booleano
    esta funcao recebe uma senha e uma regra individual, esta ultima num dicionario e devolve o valor logico da validade da senha"""

    # verificacao se cumpre as regras gerais
    vogais = 0
    repetidas = 0
    for c in senha:
        if c in ("a", "e", "i", "o", "u"):
            vogais += 1
    for i in range(len(senha)-1):
        if ord(senha[i]) == ord(senha[i + 1]):
            repetidas += 1
    # verificacao das regras particulares
    minimo = regra_individual["vals"][0]
    maximo = regra_individual["vals"][1]
    repeticao_char = 0
    for letra in senha:
        if letra == regra_individual["char"]:
            repeticao_char += 1
    return vogais >= 3 and repetidas >= 1 and minimo <= repeticao_char <= maximo


def filtrar_senhas(lst):
    """filtrar_senhas: lista ---> lista
    esta funcao recebe uma lista de dicionarios e devolve a lista ordenada alfabeticamente dos utilizadores com senhas erradas"""

    if not (type(lst) == list and len(lst) >= 1 and all(eh_utilizador(entrada) for entrada in lst)):
        raise ValueError("filtrar_senhas: argumento invalido")
    lst_users = []
    for entrada in lst:
        if not eh_senha_valida(entrada["pass"], entrada["rule"]):
            lst_users += [entrada["name"]]
    return sorted(lst_users)