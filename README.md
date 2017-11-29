# Python-SecretSantaAndItWorks (PSSAW)
A recreation of my previous SecretSantaAndAChanceOfError, but now with relatively few errors! I DO recommend this version for your personal Secret Santa games!

## Requirements
-Gmail username, password. This is the email address that your participants will get an email from.

-yagmail This is a python library available at 
https://github.com/kootenpv/yagmail
Look at the installation section in yagmail's readme.

-Your participants' names and email addresses, so yagmail can send them
their giftee's names.


## Quick Note
I recommend running at least TWO test runs. One without yagmail enabled, and one with yagmail enabled and using only a subset of your participants. This helps to make sure you know how PSSAW works, and hopefully exposes any potential issues before you try a real run.

## Usage
The main lines that perform a run are as follows. They must be done in performed in this order.
pole = NPole() # This creates an instance of the class that performs matching.

pole.addElf("NAME","EMAIL") # This creates an elf, a participant, for matching

pole.runTests(x) # This runs through the matching process x times, without sending emails.

pole.organizeProduction(y) # This shuffles the elves around y times. For honesty, this should always be random.

pole.sealTheGifts() # This matches elves up with each other.

pole.checkItTwice() # This performs checks and ensures that each elf has a match, isn't matched to itself, and that no elf has been matched twice.

pole.sendRudolf() # This looks at each elf and who they're matched with. It sends an email to that elf with their match's name.

### For a test run without yagmail: 
1) Create elves with pole.addElf("NAME","EMAIL") after creation of the pole variable. Around line 160.
2) from a command line/terminal, run main.py. You should see output similar to the below.
![noYagTestrun](https://puu.sh/yvK7m/71231124b3.png)

from a command line/terminal, run main.py
2)