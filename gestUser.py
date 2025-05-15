import mysql.connector

class GestUser:
    __connDb= None
    def __init__(self) :
        self.connDb = mysql.connector.connect(
              host="localhost",
                user="root",
                password="root",
                database ="db25_prova"
                )

    def createUser(self,cognome,nome,mail,password=""):
        inssql ="insert into t_user (firstname,lastname,mail,pwd) values (%s,%s,%s,%s)"  
        inscur=self.connDb.cursor(prepared=True)
        tupla=(nome,cognome,mail,password)
        inscur.execute(inssql,tupla)
        self.connDb.commit()
        print("inserito:" ,inscur.lastrowid )    
