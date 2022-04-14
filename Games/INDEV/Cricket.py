# Cricket Game
import random

#Introduction an Instruction
print(''' ~~~~~~~~~~ Game of Cricket ~~~~~~~~~~\nInstructions:\n\t1. You have to select any random number from 1 to 6.\n\t2. The computer will also select a number.\n\t3. While batting, if the number selected by you and computer is different, then your number will add to your runs.\n\tIf the number selected by you and computer is same, then you will lose your wicket.\n\t4. While bowling,if the number selected by you and computer is different,then the computer's number will add to its runs.\n\tIf the number selected by you and computer is same, then the computer will lose its wicket.\n\t5. Each player will get 10 wickets and overs depend on the type you chose for batting and bowling.\n\t\ta.Super Over: You get 1 over (6 Balls) and 3 wickets\n\t\tb.100 Ball Cricket: You get 100 balls (16 overs 4 balls)\n\t\tc.T20: You get 20 overs (120 balls)\n\t\td.ODI: You get 50 overs (300 balls)\n\t\te.Test Match: You get 90 overs(540 balls)\n\t6. The inning will end after either the three wickets fell or the overs end.\n\t7. The player with maximum runs wins.\n\t8. Press Enter/Return to start. ''')
input()

def ball(game):# to get the number of balls
    if game == 'a': balls = 6
    elif game == 'b': balls = 100
    elif game == 'c': balls = 120
    elif game == 'd': balls = 300
    elif game == 'e': balls = 540
    else: balls = 120
    return balls

def wicket(game):#to get the number of wickets
    if game == 'a': wickets = 3
    else: wickets = 10
    return wickets

print('\n---------- Choose Game -----------')
game = input('Enter Game(a,b,c,d,e): ').lower
iball = ball(game)#to count initial balls
iwicket = wicket(game)#to count initial wickets

print('\n---------- Start Game ----------')

# Toss 

print('\nHere comes the Toss')
toss = (input('Choose (h)eads or (t)ails: ')).lower() 
random_toss = random.randint(1,2)# In random_toss (1 = Heads) and (2 = Tails)
random_opt = random.randint(1,2)# In random_opt (1 = bat) and (2 = ball) 
user_opt = None
com_opt = None

if random_toss == toss:
    u_result = 'w'
    print('\nYou won the toss')
    user_opt = (input('Choose bat or ball: ')).lower()
elif random_toss != toss:
    u_result = 'l'
    print('\nYou lost the toss')
    if random_opt == 1:
        com_opt = 'bat'
    else: com_opt = 'ball'
if u_result == 'w':
    if user_opt == 'bat':
        Bat_first = 'You'
        Ball_first = 'Computer'
    else:
        Ball_first = 'You'
        Bat_first = 'Computer'
else:
    if com_opt == 'bat':
        Bat_first = 'Computer'
        Ball_first = 'You'
    else:
        Ball_first = 'Computer'
        Bat_first = 'You'

print('Press Enter/Return for First Inning')
input() 

# First Inning
while True:
    print('\n---------- First Inning Begins ----------')
    runs_1 = 0
    wickets_1 = wicket(game)#to count running wickets in first inning
    balls_1 = ball(game)#to count running balls in first inning

    while wickets_1 != 0 or balls_1 != 0 :
        u_choice = int(input('\nChoose any number from 1 to 6: '))
        c_choice = random.randint(1,6)    
        if u_choice < 1 or u_choice > 6 or type(u_choice) == "<class 'str'>": print('\nPlease choose a value from 1 to 6.')
        else:
            print('Your choice: ',u_choice,'\nComputer\'s choice: ',c_choice)
            if u_choice == c_choice: wickets_1 -= 1
            else:
                if Bat_first == 'You': runs_1 += u_choice
                else: runs_1 += c_choice
            print('\nScore =',runs_1,'/',wickets_1,'\nBalls remaining: ', balls_1)
            balls_1 -= 1
            if balls_1%6 == 0 and game != 'b':
                print('End of Over. Press Enter/Return to continue')
                input()
            elif balls_1%6 == 4 and game == 'b':
                print('End of Over. Press Enter/Return to continue')
                input()
    print('\n---------- End of Inning ----------')
    print('\nFinal Score: \nRuns =',runs_1, '\nwickets =',iwicket-wickets_1,'\n',Ball_first,'needs',runs_1 + 1,'runs to win.\n','Press Enter/Return to begin Second Inning')
    input()
    # Second Inning 
    runs_2 = 0# to count the running runs in second inning
    wickets_2 = wicket(game)# to count the running wickets in second inning
    balls_2 = ball(game)# to count the running balls in second inning
    print('\n---------- Second Inning Begins ----------')
    while wickets_2 != 0 or balls_2 != 0 or runs_2 < runs_1 + 1:
        u_choice = int(input('\nChoose any number from 1 to 6: '))
        c_choice = random.randint(1,6)
        if u_choice < 1 or u_choice > 6 or type(u_choice) == "<class 'str'>": print('\nPlease choose a value from 1 to 6.')
        else:
            print('Your choice: ',u_choice,'\nComputer\'s choice: ',c_choice)        
            if u_choice == c_choice: wickets_2 -= 1
            else:
                if Ball_first == 'You': runs_2 += u_choice
                else: runs_2 += c_choice
            if game != 'e':
                print('\nScore =',runs_2,'/',wickets_2,'\nTo win:',runs_1 - runs_2 + 1,'runs needed from',iball - balls_2,'balls.')
            else: print('\nScore =',runs_2,'/',wickets_2,)
            balls_2 -= 1
            if balls_2%6 == 0 and game != 'b':
                print('End of Over. Press Enter/Return to continue')
                input()
            if balls_2%6==4 and game == 'b':
                print('End of Over. Press Enter/Return to continue')
                input()
            if game == 'e':
                #Third Inning begins
                print('\n---------- Third Inning Begins ----------')
                wickets_3 = wicket(game)
                balls_3 = ball(game)
                while wickets_3 != 0 or balls_3 != 0:
                    u_choice = int(input('\nChoose any number from 1 to 6: '))
                    c_choice = random.randint(1,6)
                    if u_choice < 1 or u_choice > 6 or type(u_choice) == "<class 'str'>": print('\nPlease choose a value from 1 to 6.')
                    else:
                        print('Your Choice: ', u_choice, '\nComputer\'s Choice: ', c_choice)
                        if u_choice == c_choice: wickets_3 -= 1
                        else:
                            if Bat_first == 'You': runs_1 += u_choice
                            else: runs_1 += c_choice
                        
                
    print('\n---------- End of Inning ----------','\nFinal Score:\n','Runs =',runs_2,'\nwickets =',wickets_2,'\nPress Enter/Return to view results'), input() 
    # Result of Match 
    print('\n~~~~~~~~~~ Result ~~~~~~~~~~')
    if runs_1 > runs_2:    
        if Bat_first == 'You': print('\nCongratulations! You won the Match by',runs_1 - runs_2,'runs.')
        else: print('\nBetter luck next time! The Computer won the Match by',runs_1 - runs_2,'runs.')
    elif runs_2 > runs_1:
        if Ball_first == 'You': print('\nCongratulations! You won the Match by',iwicket - wickets_2,'wickets.')
        else: print('\nBetter luck next time! The Computer won the Match by',iwicket - wickets_2,'wickets.')
            
    else:
        tiebreaker = input('The Match is a Tie.','\nNo one Wins.\nWant a tie breaker?(y/n): ')
        if tiebreaker == 'y':
            game = 'a'
            continue
        else:
            rematch = input('Want a rematch?(y/n): ')
            if rematch == 'y' : continue
            else: quit()
