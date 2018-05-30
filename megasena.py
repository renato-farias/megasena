#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

if len(sys.argv) <= 6:
    print 'Por favor execute comando passando o numeros sorteados.'
    print 'Ex.: %s XX XX XX XX XX XX' % str(sys.argv[0])
    sys.exit(0)

resultado = [
    str(sys.argv[1]),
    str(sys.argv[2]),
    str(sys.argv[3]),
    str(sys.argv[4]),
    str(sys.argv[5]),
    str(sys.argv[6])
]

jogos = []

try:
    apostas = open('apostas.txt', 'rb')
except:
    print 'Por favor crie um arquivo chamado apostas.txt e adicione as apostas uma por linha'
    print 'com um dos seguintes formatos:'
    print '    XX XX XX XX XX XX'
    print '    XX-XX-XX-XX-XX-XX'
    print '    XX,XX,XX,XX,XX,XX'
    sys.exit(0)

for aposta in apostas:
    aposta = aposta.strip()
    for sep in [',', '-', ' ']:
        _bet = aposta.split(sep)
        if len(_bet) == 6:
            jogos.append(_bet)

jogos_premiados = 0
n_jogo = 1

for jogo in jogos:
    acertos = 0
    for numero in jogo:
        if numero in resultado:
            acertos += 1
    if acertos == 4:
        jogos_premiados += 1
        print 'Fizemos a QUADRA no jogo %s (Jogo%s)' % (str(jogo), str(n_jogo))
    elif acertos == 5:
        jogos_premiados += 1
        print 'Fizemos a QUINA no jogo %s (Jogo%s)' % (str(jogo), str(n_jogo))
    elif acertos == 6:
        jogos_premiados += 1
        print 'CARALHOOOOOOOOO, Fizemos a SENA no jogo %s (Jogo%s)' % (str(jogo), str(n_jogo))
    n_jogo += 1


print '%s estão jogos premiados' % str(jogos_premiados)
