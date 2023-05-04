# Rosa Siprien
# prof.  Kyle Dencker
# Cop 2500
# Feb 16,2023

def knight_check(word):

     fight_song=["UCF","charge","onto","the","field","With","our","spirit","we’ll","never",
                 "yield","Black","and","gold","Charge","right","through","the","line",
                 "Victory", "is","our","cry","V-I-C-T-O-R-Y","Tonight","our","Knights","will","shine"]

     if word in fight_song:
         print("True")

     else:
        print("False")

word= str(input("What is the word?: \n"))
knight_check(word)

   
