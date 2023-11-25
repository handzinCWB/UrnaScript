import mysql.connector as db

def CreateCnt(host , user , password , name):
    return db.connect(host=host , user=user, password=password, database=name)

def CloseCnt(cnt):
    return cnt.close()