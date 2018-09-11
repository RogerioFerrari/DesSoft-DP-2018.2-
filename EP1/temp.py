# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import json 
cardapio = dict()
comanda = dict()

try:
   with open('cardapio.txt','r') as cardapio:
    cardapio = json.loads(cardapio.read())

except: FileNotFoundError




loop1 = True
while loop1:
    print()
    print()
    print ('Comanda eletrônica'.upper())
    print('0 - Sair')
    print('1 - Cardápio')
    print('2 - Comanda')
    print()
    escolha1 = input('Faça sua escolha: ')
    loop2 = True
    while loop2:
        if escolha1=='0':
            print('\nAté mais!')
            loop1 = False
            break        
        if escolha1=='1':
            print()
            print('0 - Voltar')
            print('1 - Imprimir Cardápio')
            print('2 - Adicionar item ao cardápio')
            print('3 - Remover item do cardápio')
            print('4 - Alterar preço de algum item')
            print()
            escolha11 = input('Faça sua escolha: ')
            while True:
                if escolha11=='0':
                    loop2 = False
                    break
            
                if escolha11=='1':
                    print('\nCardápio:')
                    if len(cardapio)==0:
                        print('\nO cardápio está vazio!\nPor favor, adicione algum produto')
                        break
                    else:
                        for produto,preco in cardapio.items():
                            print('{0} (R${1:.2f})'.format(produto, preco))
                        break
                if escolha11=='2':
                    nome_produto = input('\nNome do produto: ')
                    preco_produto = float(input('Preço do produto: '))
                    cardapio[nome_produto]=preco_produto
                    print('\nNovo item adicionado ao cardápio:\n{0} (R${1:.2f})'.format(nome_produto, cardapio[nome_produto]))
                    break
                if escolha11=='3':
                    nome_produto = input('\nNome do produto a ser removido: ')
                    if nome_produto not in cardapio:
                        print('\nEste produto não está no cardápio')
                        break
                    else:
                        cardapio.pop(nome_produto)
                        if len(cardapio)!=0:
                            print("\n'{0}' foi removido do cardápio".format(nome_produto))
                            break
                        else:
                            print('\nO cardápio está vazio agora.\nPor favor, adicione algum produto')
                            break
                if escolha11=='4':
                    nome_produto = input('\nNome do produto: ')
                    if nome_produto not in cardapio:
                        print('\nEste produto não está no cardápio')
                        break
                    else:
                        preco = float(input('\nNovo preço do produto: '))
                        cardapio[nome_produto]=preco
                        print("\n'{0}' Novo preço: R${1:.2f}".format(nome_produto, cardapio[nome_produto]))
                        break
                
        if escolha1=='2':
            if len(cardapio)==0:
                print('\nO cardápio está vazio.\nAdicione algum produto ao cardápio para utilizar a comanda')
                break
            else:
                print()
                print('0 - Voltar')
                print('1 - Adicionar item à comanda')
                print('2 - Remover item da comanda')
                print('3 - Imprimir comanda')
                escolha12 = input('Faça sua escolha: ')
                if escolha12=='0':
                    break
            
                if escolha12=='1':
                    nome_produto = input('\nProduto a adicionar: ')
                    if nome_produto not in cardapio:
                        print('\nEste item não está no cardápio')        
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
    
                if escolha12=='2':
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
                if escolha12=='3':
                    if len(comanda)==0:
                        print('\nA comanda está vazia')
                    else:
                        print('\nComanda'.upper())
                        for chave, valor in comanda.items():
                            print("'{0}' (pedidos -> {1})".format(chave, valor))
                            
                            
            
atualizacao = json.dumps(cardapio, sort_keys = True)
with open('cardapio.txt','w') as cardapio: 
    cardapio.write(atualizacao)
    
atualizacao2 = json.dumps(comanda, sort_keys = True) 
with open('comanda.txt','w') as comanda: 
    comanda.write(atualizacao)
                
        