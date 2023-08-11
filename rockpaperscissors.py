# For this project, you and your partner(s) will work to create a program that has a "player" and a "computer" adversary. The computer should randomly choose its decision based on a list of actions it can take ("Rock", "Paper" or "Scissors"). The player should then have a chance to input their decision. 

# Note: Below, like every project, are the base requirements. We encourage you to challenge yourself as much as you are comfortable with. If this project is challenging enough, that's fine, but if you get done with the base requirements fairly quickly, expand upon this! Challenge yourself! 

# If the player and computer choose the same decision then display ("Game Tied"), 


# If the player chooses "Rock" and the computer chooses "Paper" display ("You lose"), 
# If the player chooses "Scissors" and the computer chooses "Rock" display ("You Lose")  and 
# If the player chooses "Paper" and the computer chooses "Scissors" then display ("You lose") 
# -- Vice versa for other decisions.

# Continue to ask the player for their input until they say "I quit", at which time the game will then end and display ("Thank you for playing").


# This project would usually be a pair programming project. However, for the size our class we will have groups of 2-3. This means, that one person(The driver) will code the project while the other people(The navigators)will brainstorm and guide to a working solution.
# Each of you should share/switch these roles every 30mins-1hr (-- Or you may elect to switch "drivers" after creating specific methods of the class).

# The Initial Driver needs to Make sure to:
# create a local folder for the project, create a github repository, commit the inital files, share the link

# Both navigators should then:
# fork the code, clone it and begin.

# The current driver MUST share their screen so the navigators can help brainstorm to a working solution.

# When code has been updated, you will need to pull down the changes.

# Here's an article on doing so -- https://stackoverflow.com/questions/3903817/pull-new-updates-from-original-github-repository-into-forked-github-repository


# In this project, you will need to use the random module to enable to computer to make a random decision. Full documentation on the use of this function is attached in a link to this assignment.

# Once completed, commit your code to github and submit your github link to this assignment.

import random


actions = ["rock", "paper", "scissors"]
playing = True

while playing:
    user = input("Chose an action (rock, paper, or scissors) or (I quit) to end game: ")
    computer = random.choice(actions)

    if user == computer:
        print("Computer: ", computer)
        print("Game Tied")
    elif user == "rock" and computer == "paper":
        print("Computer: ", computer)
        print("You Lose")
    elif user == "scissors" and computer == "rock":
        print("Computer: ", computer)
        print("You Lose")
    elif user == "paper" and computer == "scissors":
        print("Computer: ", computer)
        print("You Lose")
    elif user == "I quit":
        print("Thank you for playing!")
        playing = False
    else:
        print("Computer: ", computer)
        print("You Win!")
