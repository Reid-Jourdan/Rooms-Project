class Room:
    def __init__(self, name, description = "An Empty Room"):
        #every room has a name, exits, locations for the exits,
        #item, item desciptions, and grabbbales
        self.name = name
        self.description = description
        self.exits = []
        self.exitLocations = []
        self.items = []
        self.itemDescriptions = []
        self.grabbables = []
    
    #name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

    #room desciption
    @property
    def description(self):
        return self._description
    @description.setter
    def description(self, newDecription):
        self._description = newDecription
    
    #exits
    @property
    def exits(self):
        return self._exits
    @exits.setter
    def exits(self, exits):
        self._exits = exits
    
    #exit locations
    @property
    def exitLocations(self):
        return self._exitLocations
    @exitLocations.setter
    def exitLocations(self, newName):
        self._exitLocations = newName
    
    #items
    @property
    def items(self):
        return self._items
    @items.setter
    def items(self, items):
        self._items = items
    
    #item desciptions
    @property
    def itemDescriptions(self):
        return self._itemDescriptions
    @itemDescriptions.setter
    def itemDescriptions(self, itemDescriptions):
        self._itemDescriptions = itemDescriptions
    
    #grabbables
    @property
    def grabbables(self):
        return self._grabbables
    @grabbables.setter
    def grabbables(self, grabbables):
        self._grabbables = grabbables

    #add to the lists
    def addExit(self, exit, room):
        self.exits.append(exit)
        self.exitLocations.append(room)

    def addItem(self, item, desciption):
        self.items.append(item)
        self.itemDescriptions.append(desciption)

    def addGrabbable(self, item):
        self.grabbables.append(item)

    def delGrabbable(self, item):
        self.grabbables.remove(item)

    #room desciptions
    def __str__(self):
        s = f"This is the {self.name}.\n"
        s+= self.description
        s+= f"\nYou see: "
        for i in self.items:
            s += i + " "
        s += "\n"
        s += "Exits: "
        for e in self.exits:
            s += e + " "
        s += "\n"
        return s
    
##################################################
#HELPER FUNCTIONS
def createRooms():
    global currentRoom

    #make 4 rooms
    whiteR = Room("White Room", "An empty room that has a mat at the door.")
    blueR = Room("Blue Room", "A room painted a shade of blue with picture of the same man hanging all over.")
    redR = Room("Red Room", "A crimson stained room with a bucket in the corner.")
    greenR = Room("Green Room", "The room has green wall paper and there is a locked closet door.")
    yellowR = Room("Yellow Room", "The walls are a sickening yellow and there is a shelf with lots of junk on it.")
    closet = Room("Closet", "Through the darkness there is a statue of man name Ankunda Kiremire")

    ##add exits to rooms
    whiteR.addExit("east", blueR)

    blueR.addExit("east", redR)
    blueR.addExit("west", whiteR)

    redR.addExit("west", blueR)
    redR.addExit("south", greenR)

    greenR.addExit("north", redR)
    greenR.addExit("west", closet)
    greenR.addExit("north", yellowR)

    yellowR.addExit("north", greenR)

    closet.addExit("east", greenR)

    #add grabbables and items to r1
    whiteR.addItem("Rug", "It says \"GOODBYE\" insead of welcome and there is a slight bulge under it resembling a key")
    whiteR.addGrabbable("key")

    blueR.addGrabbable("Fake_Key", "It is a strange looking key that doesnt seem like it will ever fit in a lock")

    redR.addItem("Blood_Bucket", "It has murky red liquid inside and a faint shimmer of gold a the bottom")

    greenR.addItem("Closet_Door", "It has three normal looking locks on it requiring 3 seperate keys")
    
    currentRoom = whiteR
    
def death():
    print("You are dead")


######################### MAIN #########################
inventory = []
createRooms()

while(True):
    status = f"{currentRoom}\nYou are carrying: {inventory}"

    if(currentRoom == None):
        death()
        break
    
    print("="*40)
    print(status)

    action = input("What to do? ").lower().strip()

    if(action in ["quit", "bye", "exit", "leave"]):
        break

    response = "I don't understand. Try \"verb noun\". \nValid verbs are \"go\", \"look\", and \"take\""
    #parse what they typed
    words = action.split()

    if(len(words) == 2):
        verb = words[0]
        noun = words[1]

        #what happens if it is go
        if (verb == "go"):
            response = "invalid exit"
            #check all exits
            for i in range(len(currentRoom.exits)):
                if(noun == currentRoom.exits[i]):
                    #change location
                    currentRoom = currentRoom.exitLocations[i]
                    response = "Room Changed"
                    break
        
        #if verb is look
        if (verb == "look"):
            response = "I don't see that item"

            #check items
            for i in range(len(currentRoom.items)):
                if noun == currentRoom.items[i]:
                    #give the correct response(desciption)
                    response = currentRoom.itemDescriptions[i]
                    break
        
        #if verb is take
        if (verb == "take"):
            response = "I don't see that item"
            #check room
            for grabbable in currentRoom.grabbables:

                if noun == grabbable:
                    #add to inventory
                    inventory.append(grabbable)
                    #remove from room
                    currentRoom.delGrabbable(grabbable)
                    response = "Item grabbed"
                    break
    
    print(f"\n{response}")


"""
add currency(vbucks)
more rooms

"""
#hello