# Python-SecretSantaAndItWorks (PSSAW)
A recreation of my previous SecretSantaAndAChanceOfError, but now with relatively few errors! I DO recommend this version for your personal Secret Santa games!

## Requirements
- Gmail username, password. This is the email address that your participants will get an email from.

- Yagmail This is a python library available at 
https://github.com/kootenpv/yagmail
Look at the installation section in yagmail's readme.

- At least three participants.

- Your participants' names and email addresses, so yagmail can send them
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

### For a TEST run WITHOUT yagmail: 
1) Create elves with pole.addElf("NAME","EMAIL") after creation of the pole variable. Around line 160.
2) from a command line/terminal, run main.py. You should see output similar to the below.
![noYagTestrun](https://puu.sh/yvK7m/71231124b3.png)
Note: If you uncomment the commented line in NPole.sealTheGifts, you can see output of who was given who as a match. FOR HONESTY, DO NOT USE THIS ON A REAL RUN.

### For a TEST run WITH yagmail:
1) Ask some of your participants to participate in a small test run. Need at least three people.
2) Make sure that the yagmail library is installed on your system.
3) Uncomment lines 1 and 5. These import and set up yagmail to be able to send emails. Be sure to input YOUR gmail username and password in the appropriate places on line 5.
3) Decide if you want to keep the CHEAT line in sealTheGifts commented. Uncommented, this could be used to confirm that the correct emails are going to the correct people.
4) Uncomment the line starting with yag.send in sendRudolf. A good idea is to edit the 2ND parameter (the subject line of the email) to tell your test participants that this is the TEST email.
5) Add your elves under the pole = NPole() line. Around line 160.
6) Set the number of runTests runs you would like to do. If none, comment the pole.runTests() line.
7) Save the script. From a command line/terminal run main.py.

### For a REAL run WITH yagmail:
1) Make sure that the yagmail library is installed on your system.
2) Uncomment line 1 and 5. These import and set up yagmail to be able to send emails. Be sure to input YOUR gmail username and password in the appropriate places on line 5.
3) Make sure that the "cheat" line in sealTheGifts IS commented.
 Create elves with pole.addElf("NAME","EMAIL") after creation of the pole variable. Around line 160.
4) Uncomment the line starting with yag.send in sendRudolf.
5) Add your elves under the pole = NPole() line. Around line 160.
6) Set the number of runTests runs you would like to do. If none, comment the pole.runTests() line.
7) Save the script. From a command line/terminal run main.py.