# =============================================================================
# Elevator.py               Simulates an elevator
# =============================================================================
import time

#  Floors = list of all the floor names
#  Current = what floor the elevator is on

print(' ')
floors = ['Lobby (0)','One','Two','Three']  # PRINT FLOOR NAMES AS "FLOOR ONE" "FLOOR TWO" "FLOOR 3" ETC
print('Floors:' + str(floors))
#image = Image.open('image.jpg')
#image.show()
print(' ')


#floorcurrent = open("floornum.txt", "w+")

#print(floors[current])


#  Create floor number holder file if doesn't exist
#  Default floor set to 0 (lobby)

#if not os.path.exists():
    

#floor_file = open("floornum.txt", "w+")
#floor_file.close()



#  Get current floor
floortemp = open("floornum.txt", "r")

floor_current = floortemp.read()
floor_current = int(floor_current)

floortemp.close()

print('Current Floor: ' + str(floor_current))

floor_want = int(input("Select the floor: "))  # User input to select their floor


def going_up():
    
    floor_now = floor_current
    velocity = 2.5

    while floor_now < floor_want:
        floor_now += 1
        if floor_now == floor_want:
            time.sleep(2.5)
            print('Floor ' + str(floor_now))
        else:
            #velocity -= 0.2
            time.sleep(velocity)
            print('Floor ' + str(floor_now) + '..')

        
    
def going_down():
    
    floor_now = floor_current
    velocity = 2.5

    while floor_now > floor_want:
        floor_now -= 1
        if floor_now == floor_want:
            time.sleep(2.5)
            print('Floor ' + str(floor_now))
        else:
            #velocity -= 0.2            
            time.sleep(velocity)
            print('Floor ' + str(floor_now) + '..')


elevator = True
def main():
    while elevator == True:
#        floorname = floors[0]
        
        floorcount = len(floors) - 1  # How many floors there are
        
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



