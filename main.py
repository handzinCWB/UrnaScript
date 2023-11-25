import func as f
import db
import mysql.connector



numtitulo = int(input('Qual seu numero do titulo: '))

op = int(input("""BOM DIA 
[1] - VOTAR PARA PRESIDENTE 
[2] - VOTAR PARA SENADOR 
[3] - VOTAR PARA GOVERNADOR

QUAL OPÇÃO VAI QUERER: """))

def insertvoto(cnt , type , value):
    cnt = db.CreateCnt("localhost", "root", "", "eleicoes")
    mouse = cnt.cursor()
    sql = ("INSERT INTO voto (type , value ) values (%s, %s)")
    type = op
    sqld = (type, value)
    mouse.execute(sql, sqld)
    mouse.close()
    cnt.commit()
if op == 1:
    cnt = db.CreateCnt("localhost", "root", "", "eleicoes")
    f.frasep()
    f.mostrap()
    selectp = int(input('Qual cadidato deseja votar: '))
    f.verifyp(selectp)
    print('você votou ' + str(selectp))
    f.fim()

    if op == 1:
        value = selectp
    insertvoto(cnt, op, value)
if op == 2:
    cnt = db.CreateCnt("localhost", "root", "", "eleicoes")
    f.frases()
    f.mostras()
    selects = int(input('Qual cadidato deseja votar: '))
    f.verifys(selects)
    print('você votou ' + str(selects))
    f.fim()

    if op == 2:
        value = selects
    insertvoto(cnt, op, value)
if op == 3:
    cnt = db.CreateCnt("localhost", "root", "", "eleicoes")
    f.fraseg()
    f.mostrag()
    selectg = int(input('Qual cadidato deseja votar: '))
    f.verifyg(selectg)
    print('você votou ' + str(selectg))
    f.fim()
    if op == 3:
        value = selectg
    insertvoto(cnt, op, value)