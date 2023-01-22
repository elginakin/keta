import random
from datetime import datetime
#from corelocation import CLLocationManager, kCLLocationAccuracyBest # TODO: eventually? 

def adjust(eta, distance, keywords):
    # Assign a random delay based on the distance
    delay = distance * random.uniform(0.1, 1.0)
    
    # Check the time of day
    now = datetime.now()
    if now.hour >= 6 and now.hour < 12:
        delay *= 0.5 # mornings are assumed to have less delay
    elif now.hour >= 12 and now.hour < 18:
        delay *= 1 # afternoon is normal
    else:
        delay *= 1.5 # evening is assumed to have more delay
        
    # Add extra delay for certain keywords
    if "traffic" in keywords: #a fairness 
        delay += random.uniform(5, 30)
    if "probably" in keywords:
        delay += random.uniform(15, 60)
    if "might" in keywords:
        delay += random.uniform(15, 60)
        
    # Return the "funny" estimate
    return eta + delay

provided_eta = int(input("Enter the provided time given by K \n in hours: "))
provided_distance = int(input("In K's provided estimation, What is the approximate distance (in any unit of measure you see fit)  \n (numerical value): "))
provided_keywords = input("Provide any keywords used in the explination such as 'probobly' or 'might'. \n Any words will do:")

keta = adjust(provided_eta, provided_distance, provided_keywords)

print("K will arrive in", keta, " minutes") 

'''
TODO: 
    - randomize reporting units? 

'''
