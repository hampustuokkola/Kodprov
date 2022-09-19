
import re

class Room():
    def __init__(self, roomsize = None, vacuums = []):
        self.roomsize = roomsize
        self.vacuums = vacuums
        
class Vacuum(Room):
    def __init__(self,position = None, direction = None, room = None):
        self.position = position
        self.direction = direction
        self.room = room


    def drive(self, commandlist):
        commandinput = list(commandlist)
        #Looping until all commands are finished or break
        while(len(commandinput) > 0):
            print("Commands left to run: ", end="")
            print(commandinput, end = "\n\n")

            command = commandinput.pop(0)
            #Getting required values by splitting at x
            currentwidth = int(self.position.split("x")[0])
            currentheight = int(self.position.split("x")[1])
            roomwidth = int(self.room.roomsize.split("x")[0])
            roomheight = int(self.room.roomsize.split("x")[1])


            print("Current position is: " + self.position)
            print("Current direction is: " + self.direction)
            print("Executing command: " + command)

            #A "Python" switch case, can also use match case per Python v. 3.10
            #Checking commands w, s, a, d and acting depending on direction faced
            if command == "w":
                if self.direction == "n":
                    self.position = str(currentwidth)+"x"+str(currentheight + 1)
                    print("New position is: " + self.position)
                    #Could also make check instead to only permit movement inside the specified map
                    if currentheight + 1 > roomheight:
                        print("Drove outside of permitted room map at: " + str(currentwidth)+"x"+str(currentheight))
                        break

                elif self.direction == "e":
                    self.position = str(currentwidth + 1)+"x"+str(currentheight)
                    print("New position is: " + self.position)
                    #Could also make check instead to only permit movement inside the specified map
                    if currentwidth + 1 > roomwidth:
                        print("Drove outside of permitted room map at: " + str(currentwidth)+"x"+str(currentheight))
                        break

                elif self.direction == "s":
                    self.position = str(currentwidth)+"x"+str(currentheight - 1)
                    print("New position is: " + self.position)
                    #Could also make check instead to only permit movement inside the specified map
                    if currentheight - 1 <= 0:
                        print("Drove outside of permitted room map at: " + str(currentwidth)+"x"+str(currentheight))
                        break

                elif self.direction == "w":
                    self.position = str(currentwidth - 1)+"x"+str(currentheight)
                    print("New position is: " + self.position)
                    #Could also make check instead to only permit movement inside the specified map
                    if currentwidth - 1 <= 0:
                        print("Drove outside of permitted room map at: " + str(currentwidth)+"x"+str(currentheight))
                        break
                else: 
                    print("Not valid")

            elif command == "s":
                if self.direction == "n":
                    currentheight = currentheight - 1
                    self.position = str(currentwidth)+"x"+str(currentheight)
                    print("New position is: " + self.position)
                    #Could also make check instead to only permit movement inside the specified map
                    if currentheight - 1 <= 0:
                        print("Drove outside of permitted room map at: " + str(currentwidth)+"x"+str(currentheight))
                        break

                elif self.direction == "e":
                    currentwidth = currentwidth - 1
                    self.position = str(currentwidth)+"x"+str(currentheight)
                    print("New position is: " + self.position)
                    #Could also make check instead to only permit movement inside the specified map
                    if currentwidth - 1 <= 0:
                        print("Drove outside of permitted room map at: " + str(currentwidth)+"x"+str(currentheight))
                        break

                elif self.direction == "s":
                    currentheight = currentheight + 1
                    self.position = str(currentwidth)+"x"+str(currentheight)
                    print("New position is: " + self.position)
                    #Could also make check instead to only permit movement inside the specified map
                    if currentheight + 1 > roomheight:
                        print("Drove outside of permitted room map at: " + str(currentwidth)+"x"+str(currentheight))
                        break

                elif self.direction == "w":
                    self.position = str(currentwidth + 1)+"x"+str(currentheight)
                    print("New position is: " + self.position)
                    #Could also make check instead to only permit movement inside the specified map
                    if currentwidth + 1 > roomwidth:
                        print("Drove outside of permitted room map at: " + str(currentwidth)+"x"+str(currentheight))
                        break
                else: 
                    print("Not valid")


            elif command == "a":
                if self.direction == "n":
                    self.direction = "w"
                    print("New direction is: " + self.direction)

                elif self.direction == "e":
                    self.direction = "n"
                    print("New direction is: " + self.direction)

                elif self.direction == "s":
                    self.direction = "e"
                    print("New direction is: " + self.direction)

                elif self.direction == "w":
                    self.direction = "s"
                    print("New direction is: " + self.direction)
                else: 
                    print("Not valid")


            elif command == "d":
                if self.direction == "n":
                    self.direction = "e"
                    print("New direction is: " + self.direction)

                elif self.direction == "e":
                    self.direction = "s"
                    print("New direction is: " + self.direction)

                elif self.direction == "s":
                    self.direction = "w"
                    print("New direction is: " + self.direction)

                elif self.direction == "w":
                    self.direction = "n"
                    print("New direction is: " + self.direction)
                else: 
                    print("Not valid")
            else:
                print("Command: " + command + "not valid, skipping")

        

def run():
    print("Välkommen till kodprov \"robotdammsugare\" gjord utav Hampus Tuokkola 20/9-22")
    while 1:
        roomsize = input("How big is the room? Ex \"2x2\". \n ~ ").lower()
        if not re.match("^[\d*x\d*]+$", roomsize):
            print("Error, format not accepted. Please try again.")
        else:
            break;
    
    room1 = Room(roomsize)
    
    while 1:
        startposition = input("Where is the vacuum placed? Ex \"1x3\". \n ~ ").lower()
        if not re.match("^[\d*x\d*]+$", startposition):
            print("Error, format not accepted. Please try again.")
        else:
            if ((int(startposition.split("x")[0]) > int(roomsize.split("x")[0]) or int(startposition.split("x")[0]) <= 0)  or (int(startposition.split("x")[1]) > int(roomsize.split("x")[1]) or  int(startposition.split("x")[1]) <= 0)):
                print("Error, the vacuum needs to be inside the room.")
            else:
                break

    while 1:
        startdirection = input("Which direction is the vacuum faced? Ex \"n\". \n ~ ").lower()
        if not re.match("^[w|e|n|s]+$", startdirection):
            print("Error, format not accepted. Please try again.")
        else:
            break

    vacuum1 = Vacuum(startposition , startdirection, room1)
    room1.vacuums.append(vacuum1)

    while 1:
        commandinput = input("Please input desired commands? Ex \"wwswwsadwasdw\" \n ~ ").lower()
        if not re.match("^[w*|s*|d*|a*]+$", commandinput):
            print("Error, format not accepted. Please try again \n ~")
        else:
            break

    vacuum1.drive(commandinput)

run()