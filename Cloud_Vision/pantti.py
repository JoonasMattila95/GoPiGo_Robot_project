import re

class pantti(object):
    pantti_summa = 0
    pantti_maara = 0
    def __init__(self, pantti_summa, pantti_maara):
        self.pantti_summa = pantti_summa
        self.pantti_maara = pantti_maara 


    def pantti_tarkastus(self, input_text):
        
        if input_text == "Pantti":
            self.pantti_maara += 1
            print(input_text)
                                   
        if input_text == "0,15":
            self.pantti_summa += 0.15
            print(input_text)
        
        elif input_text == "0,20":
            self.pantti_summa += 0.20
            print(input_text)
            

       # elif input_text == "Pant":
        #    self.pantti_maara += 1
         #   print(input_text)
            
    def pantti_tiedot(self):
        print(self.pantti_summa)
        print(self.pantti_maara)

        

