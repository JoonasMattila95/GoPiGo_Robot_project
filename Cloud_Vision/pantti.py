import re
import MySQLdb
class pantti(object):
    
    pantti_summa = 0
    pantti_maara = 0

    
    def __init__(self, pantti_summa, pantti_maara):
        self.pantti_summa = pantti_summa
        self.pantti_maara = pantti_maara
        global db
        global cur
        db = MySQLdb.connect(host="localhost", user="test_user", passwd="test_password", db="panttibotti")
        cur = db.cursor()


    def pantti_tarkastus(self, input_text):
        
        if input_text == "Pantti":
            self.pantti_maara = 1
            print(input_text)
                                   
        if input_text == "0,15":
            self.pantti_summa = 0.15
            print(input_text)
        
        elif input_text == "0,20":
            self.pantti_summa = 0.20
            print(input_text)
            
    def getpantti(self):
        cur.execute("""SELECT * FROM panttitieto""")
        for row in cur.fetchall() :
            pantti = str(row[0])
            lukumaara = str(row[1])
            print(pantti +" "+ lukumaara)       

    def insertpantti(self):
        if self.pantti_summa != 0 and self.pantti_maara != 0:
            cur.execute("""INSERT INTO panttitieto(pantti,lukumaara) VALUES (%s,%s)""",(self.pantti_summa,self.pantti_maara))
            db.commit()
            pantti_summa = 0
            pantti_maara = 0
            return True
        #db.close()
            
    def pantti_tiedot(self):
        print(self.pantti_summa)
        print(self.pantti_maara)

        

