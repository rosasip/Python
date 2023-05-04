#Rosa Siprien
#COP 2500c
#02-24-23
#Challenge 3

SU_February_Events=["Mamma Mia","Disco Daydream","Valentine's Bingo","Pride & Prejudice","Trivia Knight"]

cb2=["Student Health Services","Healthy Knights","GBM Meeting","Tutoring Help Wanted","Career Fair"]

CAPS= ["Well-being workshop","PAWS Events","LETGo & Play Workshop","NEDA Week","Support Groups"]





master_list_1= cb2 + SU_February_Events + CAPS
print(master_list_1)


master_list_2= []
for i in range(len(cb2)):
    master_list_2.append(cb2[i])
    master_list_2.append(SU_February_Events[i])
    master_list_2.append(CAPS[i])
print(master_list_2)

master_list_3 = master_list_1.copy()
master_list_3.sort()
print(master_list_3)
