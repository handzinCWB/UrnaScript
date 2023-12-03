from db import votos, eleitores
import func as f
from peewee import *

_numtitulo = int(input("Digite seu número do título: "))
eleitor = eleitores.get_or_none(titulo=_numtitulo)

if eleitor and eleitor.qvts < 3:
    op = int(input(f"""BOM DIA {_numtitulo}
    [1] - VOTAR PARA PRESIDENTE
    [2] - VOTAR PARA SENADOR
    [3] - VOTAR PARA GOVERNADOR
    
    QUAL OPÇÃO VAI QUERER: """))



    if op == 1:
        f.frasep()
        f.mostrap()
        selectp = int(input('Qual cadidato deseja votar: '))
        f.verifyp(selectp)
        f.fim()
        eleitores.update(qvts=eleitores.qvts + 1).where(eleitores.titulo == _numtitulo).execute()
        if op == 1:
            if selectp == 13:
                nome = f.nomes[0]
                print('você votou em ' + str(nome))
                tipo = 1
                voto = selectp
                voto_p = votos(tipo=tipo, voto=voto)
                voto_p.save()
            elif selectp == 22:
                nome = f.nomes[1]
                print('você votou em ' + str(nome))
                tipo = 1
                voto = selectp
                voto_p = votos(tipo=tipo, voto=voto)
                voto_p.save()
            else:
                x = False

    if op == 2:
        f.frases()
        f.mostras()
        selects = int(input('Qual cadidato deseja votar: '))
        f.verifyp(selects)
        f.fim()
        eleitores.update(qvts=eleitores.qvts + 1).where(eleitores.titulo == _numtitulo).execute()
        if op == 2:
            if selects == 10:
                nome = f.nomes[2]
                print('você votou em ' + str(nome))
                tipo = 2
                voto = selects
                voto_s = votos(tipo=tipo, voto=voto)
                voto_s.save()
            elif selects == 13:
                nome = f.nomes[3]
                print('você votou em ' + str(nome))
                tipo = 2
                voto = selects
                voto_s = votos(tipo=tipo, voto=voto)
                voto_s.save()
            else:
                x = False

    if op == 3:
        f.fraseg()
        f.mostrag()
        selectg = int(input('Qual cadidato deseja votar: '))
        f.verifyg(selectg)
        f.fim()
        eleitores.update(qvts=eleitores.qvts + 1).where(eleitores.titulo == _numtitulo).execute()
        if op == 3:
            if selectg == 10:
                nome = f.nomes[4]
                print('você votou em ' + str(nome))
                tipo = 3
                voto = selectg
                voto_g = votos(tipo=tipo, voto=voto)
                voto_g.save()
            elif selectg == 45:
                nome = f.nomes[5]
                print('você votou em ' + str(nome))
                tipo = 3
                voto = selectg
                voto_g = votos(tipo=tipo, voto=voto)
                voto_g.save()
            else:
                x = False
else:
    if eleitor:
        print("ñ passou :(")
    else:
        print("cpf inexistente")
        add = input(f.msgadd())
        if add == "sim" and add == "SIM":
            eleitores.create(titulo=_numtitulo, qvts=0)