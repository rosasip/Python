

print("Welcome to the travel planner.\n")
places_visited= int(input("How many places are we visiting today?\n"))
visit_duration= int(input("How long do we have to visit today?\n"))

travel_location_time=0
for i in range(places_visited):
    travel_duration=int(input(f"How long does it take to travel to location#{i+1}?\n"))
    stay_duration=int(input(f"How long would you like to stay in location #{i+1}?\n"))
    travel_location_time=travel_location_time+travel_duration+stay_duration  
    
if travel_location_time<=visit_duration:
    print("This trip would take",travel_location_time,"minutes.")
    print("You are able to take this trip.")

else :
    print("This trip would take",travel_location_time,"minutes.")
    print("You are not able to take this trip in time.")
