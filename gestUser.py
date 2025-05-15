import mysql.connector

class GestUser:
    __connDb= None
    def __init__(self) :
        self.__connDb = mysql.connector.connect(
              host="localhost",
                user="root",
                password="root",
                database ="db25_prova"
                )

    def createUser(self,cognome,nome,mail,password=""):
        inssql ="insert into t_user (firstname,lastname,mail,pwd) values (%s,%s,%s,%s)"  
        inscur=self.__connDb.cursor(prepared=True)
        tupla=(nome,cognome,mail,password)
        inscur.execute(inssql,tupla)
        self.__connDb.commit()
        print("inserito:" ,inscur.lastrowid )    

    def selAllUser(self):
        frasesql="select * from t_user order by lastname,firstname;"
        cursel=self.__connDb.cursor()
        cursel.execute(frasesql)
        eltuple=cursel.fetchall()
        self.__connDb.commit()
        return eltuple
       