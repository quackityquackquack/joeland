
print("You are a famous bounty hunter from the depths of Joeland.Your council elders have requested you for a special mission.") 
print("Your target? Taj Chhabra.")
print("You can type FILE to see information about your target:")
print()
choice = input("Enter FILE if you would like to see information about your target: ")
if choice == "FILE":
  print("Warning. This person is extremly dangerous. Practice caution around this individual.")
  print()
  print("Subject: Taj Chhabra")
  print()
  print("Classified Information.")
  print()
  import shrek
  print()
  print("Taj Chhabra is responsible for multiple conspiracies and is allegedly suspected to be the leader of the 'Peter Cooper Mafia Organization'.")
  print()
  
choice = input("Type START to begin your quest: ")
if choice == "START":
    print("Stepping out of the council elder's office doors, a few ideas come to mind. Do you want to...")
def start():
  print("Type A if you want to go to the tavern and search for information. Type B if you want to go to a recent crime scene linked with the 'Peter Cooper Mafia Organization.'Press C if you want to speak with the Council Elders.")
  choice = input()
  if choice == "A":
    print("You have arrived at the tavern. There are multiple people to try and talk to. Type A if you would like to talk to the old man. Type B if you would like to talk to Tim Cahill, the clinical finisher. Type C if you would like to talk to the talking donkey with dragon donkey hybrid kids.")
    choice = input()
    if choice == "A":
      print("You try to speak to the old man. The old man says 'Trust in the LORD with all your heart, and do not lean on your own understanding. In all your ways acknowledge Him, and He will make straight your paths. May the God of hope fill you with all joy and peace as you trust in Him, so that you may overflow with hope by the power of the Holy Spirit.' The old man is clearly deranged. Please go and talk to someone else by typing START")
      choice = input()
      if choice == "START":
        print (start())
    elif choice == "B":
      print("You try to ask Tim Cahill about the whereabouts of Taj Chhabra but instead of telling you the answer he says,'A journey is best measured in friends, not in miles.'Press START to go back.")
      choice = input()
      if choice == "START":
        print (start())
    elif choice == "C":
      print("You speak to the donkey and he says 'Yea I can tell you where he is, but only for a price. 300 Snelfus.' You reluctantly pay the price. The donkey says' Alright, follow.'The donkey takes you through a maze of back alley's leading to an old tall brick building. A rustic sign on the door reads,'Peter Cooper Mafia Organization.'")
      print()
      print("What do you want to do? Type A to walk around the building. Type B to walk in the door. Type C to go back.")
      choice = input()
      if choice == "A":
        print("You walk around the building and notice through the window a large meeting going on led by a man that has a haircut like an ogre. Is this Taj Chhabra? Type YES or type NO to go back to the beginning. ")
        choice = input()
        if choice == "YES":
         print("CONGRATULATIONS. YOU HAVE FOUND TAJ CHHABRA.YOU EXPERTLY FIRE A TRANQUILIZER DART AND HE FALLS BACK OUT OF THE WINDOW INTO YOUR ARMS. YOU BRING HIM BACK TO THE COUNCIL OF ELDERS WHERE HE WILL BE PUT ON TRIAL.")
        elif choice == "NO":
         print (start())
      elif choice == "B":
        print("You walk in the front door and stumble into a meeting of people with bad haircuts. They all pause and look at you. What do you do? Type A to demand Taj Chhabra. Type B to go back.")
        choice = input()
        if choice == ("A"):
          print("A man with an ogre like haircut raises his hand and simultaneously takes out a gun. You have been captured by the Peter Cooper Mafia Organization.You have failed your mission. Game Over.")
        elif choice == ("B"):
          print (start())
  elif choice == "B":
    print("You arrive to the crime scene. There is blood and a flyer on the ground. As you look around you see a scared girl hiding in a corner. Type A if you would like to examine the blood and the flyer. Type B if you would like to talk to the girl.")
    choice = input()
    if choice == "A":
      print("The flyer is completely irrelevant and the blood means nothing. Type START to try again. ")
      choice = input()
      if choice == "START":
        print (start())
    elif choice == "B":
      print("You ask the girl if she say anything and she says 'I heard a scary man say that he was going to a big mansion in the East Village.' You thank her and make your way towards the only mansion in the East Village, Peter Cooper Manor. It is a big white mansion with sprawling lawns and many nice cars parked outside. What would you like to do? Type A if you would like to sneak around the back and find an entrance. Type B if you would like to infiltrate the mansion through an open window on the fifth floor. Type C if you would like to knock on the door politely.")
    choice = input()
    if choice == "A":
      print("You slowly creep towards the back of the estate. Suddenly you hear loud barking and you see a 150 pound rottweiler sprinting towards you. What would you like to do? Type A if you want to fight the dog. Type B if you want to run. ")
      choice = input()
      if choice == "A":
        print("The dog mauls you to death. What were you thinking? Type START to try again.")
        choice = input()
        if choice == "START":
          print (start())
      elif choice =="B":
        print("The dog starts to catch up to you but just as it is about to attack you, it gets stopped by the chain it is on. You think to yourself 'Phew, thank goodness I was fast enough.' Unfortunately all the barking alerted the guards. You get shot. Did you really think it would be that easy? Type START to try again.")
        choice = input()
        if choice == "START":
          print (start())
    elif choice == "B":
        print("As you try and scale the side of the mansion, you lose your footing because there are no footholds in a wall. You fall five stories to the ground and break your back. What a dumb idea it was to climb up a sheer wall. Type START to try again.")
        choice = input()
        if choice == "START":
          print (start())
    elif choice == "C":
      print("You knock at the door politely and a big man in a suit answers. He asks 'HEY! How did you get in here?'. You think of a quick response and say 'I have a meeting with Taj Chhabra.' What a dumb excuse. Lucky for you, the guard is even dumber. He lets you inside the house. You go up to the fourth floor and into a room where the infamous Taj Chhabra is waiting. You can't believe your luck, rightfully so. What would you like to do? Type A to start a conversation and try and trick him. Type B to pull out your gun and arrest him.")
      choice = input()
      if choice == "A":
        print("He exclaims 'Who are you and how did you get in here?!' You can't think of an excuse so he shoots you. Why would you try and talk to him, just arrest him. Type START.")
        choice = input()
        if choice == "START":
          print (start()) 
      elif choice =="B":
        print("Taj Chhabra immediately surrenders because he is a coward. As you are walking out of the building, guards try to stop you but you threaten to kill Taj they all back down and you exit the building safely. You turn Taj Chhabra in and you are hailed as a hero. Great job!")
  elif choice =="C":
    print(" You try to talk to the council of elders. They turn you down and tell you they are too busy playing bingo at the retirement home. Type START to go back. ")
  choice = input()
  if choice == "START":
    print (start())
print (start())
   