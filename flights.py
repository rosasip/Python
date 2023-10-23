
# Input
print("Welcome to the flight calculator.\n")
baseCost= float(input("What is the base flight cost?\n"))
adultsNum= int(input("How many adults attending?\n"))
childrenNum= int(input("How many children are attending?\n"))
# Calc
children_price= (baseCost-(baseCost*0.10)) 
total_adult_cost=(adultsNum*baseCost)
total_children_cost=(children_price * childrenNum)
overall_total=(total_adult_cost + total_children_cost)
# Output
print("Receipt")
print(adultsNum,"Adults @ $","%.2f"%baseCost,"\t\t$","%.2f"%total_adult_cost)
print(childrenNum,"Children @ $","%.2f"%children_price,"\t\t$","%.2f"%total_children_cost)
print("total\t\t\t\t$","%.2f"%overall_total)















