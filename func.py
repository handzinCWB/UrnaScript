from db import eleitores
from peewee import *

def frasep():
    print('*' * 40)
    print('Você escolheu votar para presidente')
    print('*' * 40)
def frases():
    print('*' * 40)
    print('Você escolheu votar para senador')
    print('*' * 40)
def fraseg():
    print('*' * 40)
    print('Você escolheu votar para governador')
    print('*' * 40)
def mostrap():
    print("""PRESIDENTES ELEGIVEIS:
    [13] - LUIS INACIO LULA DA SILVA 
    [22] - JAIR MESSIAS BOLSONARO""")
def mostras():
    print("""SENADORES ELEGIVEIS:
    [10] - HAMILTON MOURÃO
    [13] - TERESA LEITÃO""")
def mostrag():
    print("""GOVERNADORES ELEGIVEIS:
    [10] - TARCÍSIO FREITAS 
    [45] - EDUARDO LEITE""")
def fim():
    print('*' * 40)
    print('               FIM    ')
    print('*' * 40)
def verifyp(x):
    if x >= 23 or x <= 12:
        print('Candidato inexistente')
        print('Voto anulado')
def verifys(x):
    if x >= 14 or x <= 9:
        print('Candidato inexistente')
        print('Voto anulado')
def verifyg(x):
    if x == 45:
        print('Voto correto')
    elif x == 10:
        print('Voto correto')
    else:
        print('Candidato inexistente')
        print('Voto anulado')
def msgadd():
    return "Deseja adicionar este titulo? "

nomes = [
    'LUIS INACIO LULA DA SILVA',
    'JAIR MESSIAS BOLSONARO',
    'HAMILTON MOURÃO',
    'TERESA LEITÃO',
    'TARCÍSIO FREITAS',
    'EDUARDO LEITE',
]