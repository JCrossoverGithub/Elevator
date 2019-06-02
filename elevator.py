# =============================================================================
# Elevator.py               Simulates an elevator
# =============================================================================
import time
import os

#  Floors = list of all the floor names
#  Current = what floor the elevator is on

print(' ')

floors = 10


print(' ')


#floorcurrent = open("floornum.txt", "w+")

#print(floors[current])


#  Create floor number holder file if doesn't exist
#  Default floor set to 0 (lobby)

if not os.path.exists('floornum.txt'):
    tt = open("floornum.txt", "w")
    tt.write("0")
    tt.close()


#  Get current floor
floortemp = open("floornum.txt", "r")

floor_current = floortemp.read()
floor_current = int(floor_current) 

floortemp.close()

print('Current Floor: ' + str(floor_current))

floor_want = int(input("Select the floor: "))  # User input to select their floor


def going_up():
    
    floor_now = floor_current

    while floor_now < floor_want:
        floor_now += 1
        if floor_now == floor_want:
            time.sleep(1.5)
            print('Floor ' + str(floor_now))
        else:
            time.sleep(1.5)
            print('Floor ' + str(floor_now) + '..')

        
    
def going_down():
    
    floor_now = floor_current

    while floor_now > floor_want:
        floor_now -= 1
        if floor_now == floor_want:
            time.sleep(1.5)
            print('Floor ' + str(floor_now))
        else:          
            time.sleep(1.5)
            print('Floor ' + str(floor_now) + '..')


elevator = True
def main():
    
    while elevator == True:

        
        if floor_want > floors or floor_want < 0:
            print("There is no floor " + str(floor_want) + "...")
            break
        
        if (floor_want) > (floor_current):
            print(' ')
            print("Going Up..")
            going_up()
        
        if (floor_want) < (floor_current):
            print(' ')
            print("Going Down..")
            going_down()
        
        if (floor_want) == (floor_current):
            print(' ')
            print('Floor ' + str(floor_want))
        
            
        floortemp2 = open("floornum.txt", "w")
        floortemp2.write(str(floor_want))
        floortemp2.close()
        
        break



main()



