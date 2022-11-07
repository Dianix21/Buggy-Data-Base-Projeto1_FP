def teste_corrigir_palavra():
    total_score = 100
    fun_name = corrigir_palavra


    corrigir_palavra('sMEjJeqcCQmStvVeFTtfVvVBbJjvgdDNOBbAaLlNaAnoHJrRjzZeEFfsSyYYyoOxQquUXbBvVqQhBkKbnGsxXtwWMmeAapEePzZvVbBUu')
    # teste

    corrigir_palavra('TtfdDBbjJuhHPSspnZyYtiITzJxAXxaXjdaCcJjyYgEeGmentosewWEdaoOprnNoOZyYQqeElLzohHgrbBcMmCMmamMmaciIQMmqnTtAajJNUuamMohlgGLPpuUH')
    # fundamentosdaprogramacao

    corrigir_palavra('FNnYyuOonDNnddFfgGsSaEemDdVOmMoDdvyGgYCcyOoYsSentohXKkxHsPpVvDatTPrUuRrogrnNamaCcIiYGHoOhgeEHhWwycCXxzZdDJzZjceEAaaqQyYodpPD')
    # FundamentosDaProgramacao

    corrigir_palavra('yYsupGgwWeEPPpNneENnFfRtTrYypfaAdDFerlLoOcaAascCSzeEZIjJFfiFVKkvflrKkRifTtragXxvVZxQHhsSdDqXgqQGnkZzKNlLzImMuUiyYnaANdDXfFxjJhHcCnNirDdRtTlKkUuilLsPptHnNhiGgbBcowVvWyYesSspkEeKqQcJjCtTiaITIitQqiPOoplGglLLlxUuXMmDdLVvdDXxlidSsoxXscCo')
    # supercalifragilisticoespialidoso

    return


def teste_eh_anagrama():
    total_score = 50
    fun_name = eh_anagrama

    eh_anagrama('amoro', 'aroma')
    # False

    eh_anagrama('Amor', 'Roma')
    # True

    eh_anagrama('poder', 'Pedro')
    # True

    eh_anagrama('QuidEstVeritas', 'EstVirQuiAdest')
    # True

    return


def teste_corrigir_doc():
    total_score = 150
    fun_name = corrigir_doc

    corrigir_doc(5)
    # corrigir_doc: argumento invalido

    corrigir_doc(())
    # corrigir_doc: argumento invalido

    corrigir_doc(['a', 'b', 'c'])
    # corrigir_doc: argumento invalido

    corrigir_doc('1234567')
    # corrigir_doc: argumento invalido

    corrigir_doc('Fundamentos da Programacao.')
    # corrigir_doc: argumento invalido

    corrigir_doc('Fundamentos da Programacao')
    # Fundamentos da Programacao

    corrigir_doc('Fundamentos da Programacao e Programacao com objetos')
    # Fundamentos da Programacao e Programacao com objetos

    corrigir_doc('Fundamentos da Programacao e programacao com objetos')
    # Fundamentos da Programacao e programacao com objetos

    corrigir_doc('Programacao com objetos e bojetos')
    # Programacao com objetos e

    doc = 'FuKknfbBFdamvVEIicCeetTntUJjuos DddBfFbrRQKkquUlLNnajJ NnzZPnNrBbbBdDogDvVdrwoOWamTtaSfFscwkKWaouUtbBTKQqk'
    corrigir_doc(doc)
    # Fundamentos da Programacao

    doc = 'ProgtBbTrajJmagGcaGgo FfZqQzcmYyQSsqMomPZzUuERraAJjep JjFfqQobjKkuUkKetQqSspPCcAaEeovVTtSvVtTvVss eMmlxqQXOoIiLLlOo XxbhHodDWwjejJtwWoOos'
    corrigir_doc(doc)
    # Programacao com objetos e

    doc = 'ErgGAaxXrRhVvHsSUuJjapPnN WwNnXxgGXxlLMmYyla sgGAauOyEeYoTtmsSoOwkKWaGg CtTcpiIPZJcCjzShHkKsBbmuzVvzZkKdBbDZGgYyszZa sNnjoOJbBTtouvenXxCTtcidDr HGguUYyhdBaAbPpKkeZzlCc univeZUubYRvVryBzKkiIrLlNnsMmLnNlo IiFfaAlOoVuUjJAavPpiIaMmdHhDBbgG ixXiIPpnmacutlLTzZlrRadIia cXtTxayYyYlyiIYumnuUiAaaSsdEejJa DdbiIryYiLjJloJjfFSsBbAWwayYyYsCcpGgGgPgGaaA uUdDIhHiwWyPTtpBbhvVHIiYUvwWVuCcy sLlCQqFfPphHHhLlcoDdgGxXPpFfIibBbriTJjaAtaQqsS drRDmadDrBseESbizZonTtFfUucCeta LoOlmhHonhHbaABeHoOhtaRiIrrMmiuDdUwWaLEeljJZz dEesSWwlLQqHLllLhWHhaAwcCaneJjsNnDdaEeNn dhHBbAaewVvWGg awxXWdaBbkKZznSses'
    corrigir_doc(doc)
    # Era la suma souvenir del la inmaculada briosa y marioneta danesa de

    return


def teste_obter_posicao():
    total_score = 50
    fun_name = obter_posicao

    obter_posicao('C', 1)
    # 1

    obter_posicao('B', 2)
    # 5

    obter_posicao('E', 3)
    # 2

    obter_posicao('D', 4)
    # 5

    obter_posicao('C', 6)
    # 3

    obter_posicao('B', 7)
    # 7

    obter_posicao('E', 8)
    # 7

    obter_posicao('D', 9)
    # 9

    return


def teste_obter_digito():
    total_score = 50
    fun_name = obter_digito

    obter_digito('DDCEDEB', 3)
    # 5

    obter_digito('DDCEDEB', 8)
    # 8

    obter_digito('DDCEDEB', 9)
    # 8

    obter_digito('DBDEBCBEBD', 5)
    # 8

    return


def teste_obter_pin():
    total_score = 100
    fun_name = obter_pin

    obter_pin(25)
    # obter_pin: argumento invalido

    t = 'CEE'
    obter_pin(t)
    # obter_pin: argumento invalido

    t = ['CEE', 'DDBBB', 'ECDBE', 'CCCCB']
    obter_pin(t)
    # obter_pin: argumento invalido

    t = ('CEE', 'DDBBBA', 'ECDBE', 'CCCCB')
    obter_pin(t)
    # obter_pin: argumento invalido

    t = ('CEE', 'DDBBB', '', 'CCCCB')
    obter_pin(t)
    # obter_pin: argumento invalido

    t = ('DDBBB', 'ECDBE', 'CCCCB')
    obter_pin(t)
    # obter_pin: argumento invalido

    t = ('BCCDBDCE', 'BDEEC', 'EDCCEBB', 'EECCDBEBC')
    obter_pin(t)
    # (2, 1, 7, 4)

    t = ('DBCDEE', 'DDDDE', 'DCE', 'BB', 'EDDD', 'BD')
    obter_pin(t)
    # (4, 5, 2, 8, 9, 9)

    t = ('BDD', 'BBBEE', 'BCCBEE', 'EDCCDB', 'EDECD', 'DDCED', 'CB', 'BCE', 'DCB', 'CEBCEB')
    obter_pin(t)
    # (9, 7, 4, 6, 3, 3, 6, 5, 6, 4)

    return


def teste_eh_entrada():

    total_score = 150
    fun_name = eh_entrada

    eh_entrada(True)
    # False

    eh_entrada(['a-b-c-d-e-f-g-h', '[abcde]', (950, 300)])
    # False

    eh_entrada(('a-b-c-d-e-f-g-h', '[abcde]'))
    # False

    eh_entrada(('a-b-c-d-e-f-g-h', '[abcde]', (950, 300), 'ola'))
    # False

    eh_entrada(('ERRADO', '[abcde]', (950, 300)))
    # False

    eh_entrada(('errado2', '[abcde]', (950, 300)))
    # False

    eh_entrada(('ainda errado', '[abcde]', (950, 300)))
    # False

    eh_entrada(('ainda-errado', 25, (950, 300)))
    # False

    eh_entrada(('ainda-errado', '[12345]', (950, 300)))
    # False

    eh_entrada(('ainda-errado', 'abcde', (950, 300)))
    # False

    eh_entrada(('ainda-errado', '[abcde]', (950,)))
    # False

    eh_entrada(('ainda-errado', '[abcde]', 950))
    # False

    eh_entrada(('ainda-errado', '[abcde]', (950, 'a')))
    # False

    eh_entrada(('ainda-errado', '[abcde]', (950, -30)))
    # False

    eh_entrada(('agora-sim', '[abcde]', (2, 3, 7, 200)))
    # True

    eh_entrada(('esta-entrada-e-correta', '[abzxy]', (20, 2, 1979)))
    # True

    return

def teste_validar_cifra():
    total_score = 200
    fun_name = validar_cifra

    t = 'xxyyaabbcdcdeex'
    validar_cifra(t, '[abcde]')
    # False

    t = 'fundamentos-da-programacao'
    not validar_cifra(t, '[aodmn]')
    # False

    t = 'xxyyaabbcdcdee'
    validar_cifra(t, '[abcde]')
    # True

    t = 'lorem-ipsum-dolor-sit-amet-consectetur-adipiscing-elit-sed-do-eiusmod-tempor-incididunt-ut-labore-et-dolore-magna-aliqua-ut-enim-ad-minim-veniam-quis-nostrud-exercitation-ullamco-laboris-nisi-ut-aliquip-ex-ea-commodo-consequat-duis-aute-irure-dolor-in-reprehenderit-in-voluptate-velit-esse-cillum-dolore-eu-fugiat-nulla-pariatur-excepteur-sint-occaecat-cupidatat-non-proident-sunt-in-culpa-qui-officia-deserunt-mollit-anim-id-est-laborum'
    validar_cifra(t, '[ietao]')
    # True

    return


def teste_filtrar_bdb():
    total_score = 100
    fun_name = filtrar_bdb


    filtrar_bdb(True)
    # filtrar_bdb: argumento invalido

    filtrar_bdb([100])
    # filtrar_bdb: argumento invalido

    filtrar_bdb([(),()])
    # filtrar_bdb: argumento invalido

    bdb = [('fundamentos-da-programacao', '[aodmn]', (1, 2)), ('programar-e-fixe', '[raefh]', (3, 4, 5)), ('entrada-sem-erros', '[erasd]', (52, 404))]
    filtrar_bdb(bdb)
    # [('programar-e-fixe', '[raefh]', (3, 4, 5))]

    bdb = [('beautiful-is-better-than-ugly', '[teuab]', (1,2)), ('explicit-is-better-than-implicit', '[itecl]', (3,4)), ('simple-is-better-than-complex', '[etilm]', (5,6)), ('complex-is-better-than-complicated', '[etcai]', (7,8))]
    filtrar_bdb(bdb)
    # []

    bdb = [('beautiful-is-better-than-ugly', '[etuab]', (1, 2)), ('explicit-is-better-than-implicit', '[tiecl]', (3, 4)), ('simple-is-better-than-complex', '[etiml]', (5, 6)), ('complex-is-better-than-complicated', '[etcia]', (7, 8))]
    filtrar_bdb(bdb)
    # [('beautiful-is-better-than-ugly', '[etuab]', (1, 2)), ('explicit-is-better-than-implicit', '[tiecl]', (3, 4)), ('simple-is-better-than-complex', '[etiml]', (5, 6)), ('complex-is-better-than-complicated', '[etcia]', (7, 8))]

    return




def teste_obter_num_seguranca():
    total_score = 100
    fun_name = obter_num_seguranca

    s = (777, 707, 901)
    obter_num_seguranca(s)
    # 70

    s = (4929, 19786, 6046, 18239, 17005, 17656, 11057, 14014, 11739, 17495)
    obter_num_seguranca(s)
    # 161

    s = (1390, 1558, 483, 1748, 1879, 1930, 1501, 41, 1175, 502)
    obter_num_seguranca(s)
    # 19

    s = (79, 1289, 589, 144, 1230, 275, 1016, 1200, 1933, 1383, 446, 795, 277, 1941, 1190, 441, 1788, 583, 1653, 1551, 56, 1286, 251, 1365, 723, 1501, 644, 1964, 404, 1631, 732, 252, 677, 1625, 902, 422, 131, 288, 136, 1387, 31, 1368, 20, 619, 1027, 475, 1256, 435, 1237, 387, 156, 385, 1013, 967, 1208, 1868, 386, 900, 675, 1191, 1627, 1437, 704, 1900, 591, 1145, 1275, 1296, 707, 1494, 1002, 1421, 99, 1774, 1334, 1283, 290, 548, 1127, 1199, 1515, 595, 297, 1339, 1700, 1748, 1390, 201, 216, 274, 266, 379, 1108, 98, 759, 682, 1336, 933)
    obter_num_seguranca(s)
    # 1


    return


def teste_decifrar_texto():
    total_score = 100
    fun_name = decifrar_texto

    decifrar_texto('bfaudoyod-q-yiuha-rwjs', 793)
    # programar e muito fixe

    decifrar_texto('uztpmdype-bn-wxomzk-mcti-pzgr', 526)
    # beautiful is better than ugly

    decifrar_texto('vqgezvzm-bj-sxkmvk-myte-zfgezvzm', 1152)
    # explicit is better than implicit

    decifrar_texto('fxzeyt-xf-otgirg-iupa-pdzeytk', 9060)
    # simple is better than complex

    return


def teste_decifrar_bdb():
    total_score = 100
    fun_name = decifrar_bdb

    bdb = (('bfaudoyod-q-yiuha-rwjs', '[adouy]', (2, 795, 3223, 4316)), ('lctlgukvzwy-ji-xxwmzgugkgw', '[abxyz]', (2388, 367, 5999)), ('nyccjoj-vfrex-ncalml', '[xxxxx]', (50, 404)))
    decifrar_bdb(bdb)
    # decifrar_bdb: argumento invalido

    bdb = [('bfaudoyod-q-yiuha-rwjs', '[adouy]', (2, 795, 3223, 4316))]
    decifrar_bdb(bdb)
    # ['programar e muito fixe']

    bdb = [('qvplizula-xj-stkivg-iype-lvcn', '[ilvpa]', (762, 2586, 310)), ('avljeaer-go-xcprap-rdyj-ekljeaer', '[earjl]', (929, 2915, 380)), ('zrtysn-rz-inacla-coju-jxtysne', '[nacjr]', (3354, 33, 805, 1859)), ('dtp-kav-whivv-sx-pzmy-phl', '[pvhad]', (1706, 1048, 380, 4385))]
    decifrar_bdb(bdb)
    # ['beautiful is better than ugly', 'explicit is better than implicit', 'simple is better than complex', 'may the force be with you']

    return


def teste_eh_utilizador():
    total_score = 100
    fun_name = eh_utilizador

    eh_utilizador(56.7)
    # False

    not eh_utilizador(('name', 'pass', 'rule'))
    # True

    eh_utilizador({'name': 'bruce', 'surname': 'wayne', 'pass': 'mynameisbatman', 'rule': {'vals': (2, 8), 'char': 'm'}})
    # False

    eh_utilizador({'pass': 'mynameisbatman', 'rule': {'vals': (2, 8), 'char': 'm'}})
    # False

    eh_utilizador({'name': '', 'pass': 'mynameisbatman', 'rule': {'vals': (2, 8), 'char': 'm'}})
    # False

    not eh_utilizador({'name': 'bruce.wayne', 'pass': True, 'rule': {'vals': (2, 8), 'char': 'm'}})
    # True

    not eh_utilizador({'name': 56, 'pass': 'mynameisbatman', 'rule': {'vals': (2, 8), 'char': 'm'}})
    # True

    eh_utilizador({'name': 'bruce.wayne', 'pass': 'mynameisbatman', 'rule': {}})
    # False

    not eh_utilizador({'name': 'bruce.wayne', 'pass': 'mynameisbatman', 'rule': {'vals': (-2, 8), 'char': 'm'}})
    # True

    not eh_utilizador({'name': 'bruce.wayne', 'pass': 'mynameisbatman', 'rule': {'vals': (2, 1), 'char': 'm'}})
    # True

    eh_utilizador({'name': 'bruce.wayne', 'pass': 'mynameisbatman', 'rule': {'vals': (2, 8), 'char': 'ma'}})
    # False

    eh_utilizador({'name': 'bruce.wayne', 'pass': 'mynameisbatman', 'rule': {'vals': (2, 8), 'char': 'm'}})
    # True


    return


def teste_eh_senha_valida():
    total_score = 150
    fun_name = eh_senha_valida

    eh_senha_valida('aaaaa', {'vals': (1, 5), 'char': 'a'})
    # True

    eh_senha_valida('aaaaaa', {'vals': (1, 5), 'char': 'a'})
    # False

    eh_senha_valida('aaaaa', {'vals': (2, 5), 'char': 'd'})
    # False

    eh_senha_valida('ddddei', {'vals': (2, 5), 'char': 'd'})
    # False

    eh_senha_valida('addddei', {'vals': (2, 5), 'char': 'd'})
    # True

    eh_senha_valida('adedidodei', {'vals': (2, 5), 'char': 'd'})
    # False

    eh_senha_valida('ajejidojeii', {'vals': (3, 3), 'char': 'j'})
    # True

    eh_senha_valida('aXaxaaa', {'vals': (2, 5), 'char': 'X'})
    # False

    eh_senha_valida('..adedidodei', {'vals': (2, 5), 'char': 'd'})
    # True

    eh_senha_valida('fundamentosdaprogramacao21-22', {'vals': (2, 5), 'char': 'n'})
    # True

    return


def teste_filtrar_senhas():
    total_score = 100
    fun_name = filtrar_senhas

    filtrar_senhas(3.1416)
    # filtrar_senhas: argumento invalido

    filtrar_senhas(['nothing'])
    # filtrar_senhas: argumento invalido

    bdb = [{'name': 'bruce.wayne', 'pass': 'mynameisbatman', 'rule': {'vals': (1, 3), 'char': 'm'}}, {'name': 'peter.parker', 'pass': 'sppidie', 'rule': {'vals': (1, 4), 'char': 'p'}}, {'name': 'clark.kent', 'pass': 'notsure', 'rule': {'vals': (2, 9), 'char': 'c'}}]
    filtrar_senhas(bdb)
    # ['bruce.wayne', 'clark.kent']

    bdb = [{'name': 'bruce.wayne', 'pass': 'XXmynameisbatman', 'rule': {'vals': (1, 3), 'char': 'm'}}, {'name': 'peter.parker', 'pass': 'spidie', 'rule': {'vals': (1, 4), 'char': 'p'}}, {'name': 'clark.kent', 'pass': 'notsure', 'rule': {'vals': (2, 9), 'char': 'c'}}]
    filtrar_senhas(bdb)
    # ['clark.kent', 'peter.parker']

    return
