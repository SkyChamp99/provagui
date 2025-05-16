import mymysql.connector

class GestTipo:
    __connDb= None
    def __init__(self) :
        self.__connDb = mysql.connector.connect(
              host="localhost",
                user="root",
                password="root",
                database ="db25_prova"
                )

    def createTipo(self,tipo,sede,costo):
        inssql ="INSERT INTO `db25_prova`.`t_tipo` (`tipo`, `costo`, `sede`) VALUES (%s, %s,%s);"  
        inscur=self.__connDb.cursor(prepared=True)
        tupla=(tipo,costo,sede)
        inscur.execute(inssql,tupla)
        self.__connDb.commit()
        print("inserito:" ,inscur.lastrowid )
        return   inscur.lastrowid  

    #selezione tipi visita
    def selAllTipo(self):
        frasesql="select * from t_tipo order by tipo;"
        cursel=self.__connDb.cursor()
        cursel.execute(frasesql)
        eltuple=cursel.fetchall()
        return eltuple
        #[(1,"visita ortopedica","ivrea",50),     ...]

    