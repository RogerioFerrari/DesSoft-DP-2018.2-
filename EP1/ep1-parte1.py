#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 19:55:45 2018

@author: roger
"""

cardapio = {'banana':2, 'maçã':3}
comanda = {}
while True:
    print()
    print()
    print ('Comanda eletrônica'.upper())
    print('0 - Sair')
    print('1 - Imprimir Cardápio')
    print('2 - Adicionar Item à comanda')
    print('3 - Remover Item da comanda')
    print('4 - Imprimir Comanda')
    escolha = input('Faça sua escolha: ')
    if escolha=='0':
        print('\nAté mais')
        break
    if escolha=='1':
        print('\nCardápio:\n')
        for produto,preco in cardapio.items():
            print('{0} (R${1:.2f})'.format(produto, preco))
    if escolha=='2':
        nome_produto = input('\nProduto a adicionar: ')
        if nome_produto not in cardapio:
            print('\nO item não está no cardápio')        
        else:
            while True:
                quantidade_produto = int(input('\nQuantidade a adicionar: '))
                if quantidade_produto<0:
                    print('\nA quantidade não pode ser negativa')
                else:
                    if nome_produto in comanda:
                        comanda[nome_produto]+=quantidade_produto
                        print('\nQuantidade atual de {0}: {1}'.format(nome_produto, comanda[nome_produto]))
                        break
                    else:
                        comanda[nome_produto]=quantidade_produto
                        print('\nQuantidade atual de {0}: {1}'.format(nome_produto, quantidade_produto))
                        break
    if escolha=='3':
        nome_produto = input('\nProduto a remover: ')
        if nome_produto not in comanda:
            print("\nO item '{0}' não está na comanda".format(nome_produto))
        else:
            loop = True
            while loop:         
                while True:                    
                    quantidade_produto = int(input('\nQuantidade a remover: '))
                    if quantidade_produto<0:
                        print("\nDigite sem o sinal de menos (-)")
                        break
                    if quantidade_produto >comanda[nome_produto]:
                        print('\nNão é possível remover mais do que a quantidade presente na comanda')
                        break
                    else:
                        comanda[nome_produto]-=quantidade_produto
                        if comanda[nome_produto]==0:
                            print('\nQuantidade atual de {0}: {1}'.format(nome_produto, comanda[nome_produto]))
                            print("\nRemovendo da comanda...".format(nome_produto))
                            comanda.pop(nome_produto)
                            loop = False
                            break
                        else:
                            print('\nQuantidade atual de {0}: {1}'.format(nome_produto, comanda[nome_produto]))
                            loop = False
                            break
    if escolha=='4':
        for chave, valor in comanda.items():
            print('\n{0}: {1}'.format(chave, valor))
            
                
        
