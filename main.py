#import yagmail
import copy
import random
random.seed()
#yag = yagmail.SMTP([GMAIL],[PASSWORD])

#Shift each element to the right by one.
def arrayShift(arr2):
    temp = arr2[len(arr2)-1]
    for i in range(len(arr2)-2,-1,-1):
        arr2[i+1] = arr2[i]
    arr2[0] = temp
    return arr2

#Elves are the people in your secret santa! 
class Elf:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        
        self.myElf = None
    
    def __repr__(self):
        return("("+self.name+","+ self.email + ")\n")

#NPole is where all the holiday business happens!
class NPole:
    def __init__(self):
        
        self.elves = []
        self.picks = []
        self.numElves = 0
        
        self.hired = False #Have we hired all our elves?
        self.organized = False #Have we shuffled our matches
        self.sealed = False #Have we got the matches ready?
        self.checked = False#Have we checked our matches for uniqueness?

    #Adds a new Elf to the draw.
    def addElf(self, name, email):
        if (self.hired == False): #Prevent hiring of elves if we start organization
            print("Adding new Elf..."+name)
            elf = Elf(name, email)  # Create an Elf with the given name and email
            self.elves.append(elf)  # Add our new Elf to the roster
        
    #Shuffles the matches and prevents self-matching
    def organizeProduction(self,amt):
        self.hired = True #Prevent the addition of new Elves
        self.numElves = len(self.elves) #Record length of our roster for
                                        #future use without calculation
        print("Shuffling...")
        
        self.picks = copy.deepcopy(self.elves) #Copy our roster for matching
        if amt % (self.numElves-1) is 0: #This should prevent matching elfA to elfA.
            amt += 1    
		
        while((amt > 0) or (self.elves[0] == self.picks[0])):
            amt -= 1
            arrayShift(self.picks)
        self.organized = True
    
    #Links each elf to its match
    def sealTheGifts(self):
        print("Sealing the gifts...")
        if (self.organized == True):
            for i in range(0,self.numElves-1):
                self.elves[i].myElf = copy.deepcopy(self.picks[i])
                #print (self.elves[i])
                #print (self.picks[i])
                #print(self.elves[i].name+"="+self.elves[i].myElf.name)
            self.sealed = True
        
    #Makes double sure that each elf has a match, isn't matched to itself, and 
    #that nobody has been matched twice.
    def checkItTwice(self):
        print("Checking the list...")
        if (self.organized == True) and (self.sealed == True):
            
            for i in range(0,self.numElves-1):
                if (self.elves[i].name == self.elves[i].myElf.name):
                    print("An Elf is set to give themself a gift! Shuffling a little more...")
                    self.organized = False
                    self.sealed = False
                    self.organizeProduction(1)
                    self.sealTheGifts()
                    
                    if (self.checkItTwice()):
                        self.organized = True
                        self.sealed = True
                        self.checked = True
                        return True
                    else:
                        return self.checkItTwice()
                    
                #Check that each elf has a match. If they don't-- ABORT.
                if (self.elves[i].myElf == None):
                    
                    print("ELF "+self.elves[i].name+" HAS NOBODY TO SEND A GIFT TO. SHUTTING DOWN.")
                    self.checked = False
                    return False
                
                #Check each elf with each other elf to ensure they don't match with the same person
                for j in range(0,self.numElves-1):
                    #If they're not the same person
                    if not(self.elves[i].name == self.elves[j].name):
                        #and they have the same match-- ABORT.
                        if self.elves[i].myElf.name == self.elves[j].myElf.name:
                            print("AN ELF IS SET TO RECEIVE TWO GIFTS. SHUTTING DOWN.")
                            self.checked = False
                            return False
            self.checked = True
            return True
        
    #Requires Yagmail
    def sendRudolf(self,yag=None):
        if (self.organized == True) and (self.sealed == True) \
        and (self.checked == True):
            print("Sending emails...")
        
            
            if not(yag==None):
                print("Sending emails...")
                # Send the emails!
                #yag.send(self.elves[l_elf_one_index].email, "2017 Secret Santa [Sent by Program]", "Congratulations "+ str(self.elves[l_elf_one_index].name) + ", the person you will be getting a gift for has been randomly chosen! That person is " + str(self.elves[l_elf_two_index].name))
                print("Mail sent! Merry Christmas everyone!!")
            else:
                print("Mail not set up...")
                print("Mail not sent! Merry Christmas everyone!!")
            
            
        
    

    


pole = NPole()

# Add the Elves

#pole.addElf("[NAME]", "[EMAIL]")
pole.addElf("1", "1")
pole.addElf("2", "2")
pole.addElf("3", "3")
pole.addElf("4", "4")
pole.addElf("5", "5")
pole.addElf("6", "6")
pole.addElf("7", "7")
pole.addElf("8", "8")
pole.addElf("9", "9")
pole.addElf("10", "10")


pole.organizeProduction(random.randint(1,500))
pole.sealTheGifts()
pole.checkItTwice()
pole.sendRudolf()
print("DONE")
