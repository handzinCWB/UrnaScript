from peewee import *

db = MySQLDatabase('eleicoes', user='root', password='', host='localhost', port=3390)

class BaseModel(Model):
    class Meta:
        primary_key = False
        database = db
class votos(BaseModel):
    tipo = SmallIntegerField()
    voto = SmallIntegerField()

class eleitores(BaseModel):
    titulo = SmallIntegerField()
    qvts = SmallIntegerField()

db.connect()