
########### inizio codice standard   ###################################
########### inizio codice standard   ###################################
from PySide6.QtWidgets import QApplication, QMainWindow
import sys
#importo la classe tipo
from gestUser import GestUser
from gestTipo import GestTipo


#importo la classe generata da compilatore ui-> py
#dal file Ui_qtgui.py importo la classe Ui_MainWindow
#ora posso usare Ui_MainWindow

#!!!!!!!!!!!!!!cambiare nome classe from con file python qt compilato provagui.py!!!!!!!
from provagui_ui import Ui_MainWindow


#creo mia classe MainWindow che eredita le caratteristiche della classe
# QMainWindow finestra base con solo bordi e x in alto per chiudere
class MainWindow(QMainWindow):
    #nel costruttore inserisco tutto il codice per gestire 
    #la finestra e gli oggetti da caricare dentro
   
    def __init__(self, parent=None):
        #lancio il costruttore di base di QmainWindow con super (la classe da cui derivo)
        super(MainWindow, self).__init__()
        #creo un attributo mio chiamato user interface ui
        # in cui metto un oggetto di tipo finestra compilata da qt
        self.ui=Ui_MainWindow()
        #lancio il metodo setupUI fornito dal compilatore
        self.ui.setupUi(self)
        # aggancio ai pulsanti il click che lancia i relativi metodi
        self.ui.btnWelcome.clicked.connect(self.showMsg)
        self.ui.btnInsertTipo.clicked.connect(self.insnewtipo)
        self.ui.btnInsertUser.clicked.connect(self.insnewuser)
        self.ui.btnRefresh.clicked.connect(self.refresh)
        #metodo per iniziare con la combo gia' compilata
        self.refresh()
        
    def showMsg(self):
        #refresh di display
        #leggo text da oggetti su interfaccia
        newtx=self.ui.elLastname.text() + " " +self.ui.elFirstname.text()
        #stampo testo su proprieta' text di label
        self.ui.lblMsg.setText(newtx)

    def insnewtipo(self):
        #recupero dati da interfaccia 
        tipo= self.ui.elTipo.text()
        sede= self.ui.elSede.text()
        costo=self.ui.spCosto.value()
        costo=str(costo)
        #creo gestore tipi e gli faccio inseriro i dati presi da interfaccia in db
        gestt=GestTipo()
        newid=gestt.createTipo(tipo,sede,costo)
        newtx=f"nuovo idtipo = {newid}"
        self.ui.lblMsg.setText(newtx)
        self.refresh()
    

    def refresh(self):
        eltipi=gestoreTipi.selAllTipo()
        self.ui.cbUser.clear()
        for tupla in eltipi:
            self.ui.cbUser.addItem(tupla[1])

        elutenti=gestoreUtenti.selAllUser()
        self.ui.cbUser.clear()
        for tupla in elutenti:
            self.ui.cbUser.addItem(tupla[2] + " " + tupla[1])

        
    def insnewuser(self):
        #recupero dati da interfaccia 
        firstname= self.ui.elFirstname.text()
        lastname= self.ui.elLastname.text()
        mail=self.ui.elMail.text()
        pwd=self.ui.elPwd.text()
        
        #creo gestore tipi e gli faccio inseriro i dati presi da interfaccia in db
        gest=GestUser()
        newid=gest.createUser(lastname,firstname,mail,pwd)
        newtx=f"nuovo iduser = {newid}"
        self.ui.lblMsg.setText(newtx)
        self.refresh()
    
    
    


#lista tipi
eltipi=[]
#creo gestiore tipi
gestoreTipi=GestTipo()

#lista tipi
elutenti=[]
#creo gestiore tipi
gestoreUtenti=GestUser()







######## inizio codice standard###################################
#creazione applicazione da poi eseguire in windows
app = QApplication(sys.argv)
#creazione di oggetto window grafico con tutti gli elementi grafici dati da setupUi
window = MainWindow()
# rende visibile la finestra
window.show()
# lancia la reale esecuzione della finestra windows
# e quindi del programma python
app.exec()
######## fine codice standard###################################
