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
    r1 = Room("White Room", "An empty room that has a mat at the door.")
    r2 = Room("Blue Room")
    r3 = Room("Red Room")
    r4 = Room("Room 4")

    ##add exits to r1
    r1.addExit("east", r2)
    r1.addExit("south", r3)

    #add grabbables and items to r1
    r1.addGrabbable("key")
    r1.addItem("desk", "it is wooden")
    r1.addItem("chair", "made of steel")

    r2.addExit("west", r1)
    r2.addExit("south", r4)
    r2.addItem("bed", "it is twin sized with some hair sitting on it")
    r2.addGrabbable("wig")
    r2.addItem("computer", "it has fortnite open")
    r2.addGrabbable("vbucks")


    r3.addExit("north", r1)
    r3.addExit("east", r4)
    r3.addItem("stove", "there are some pancakes on it")
    r3.addGrabbable("pancake")
    r3.addItem("pantry", "there is bologna in it")
    r3.addGrabbable("bologna")

    r4.addExit("west", r3)
    r4.addExit("north", r2)
    r4.addExit("south", None)
    r4.addItem("bath", "it is full of milk")
    r4.addGrabbable("milk")

    currentRoom = r1
    
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