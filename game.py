import requests

############################  Global variables ######################################

# Variable where the number to be guessed is stored
random_number = []

# Variable storing if a player has won
winner = False

# Boolean variable storing the status of all hits 
all_correct=False

#Variable that stores the number of attempts of a player. 
num_attempts=0

# List containing all the attempts of a player
attempts=[]

max_attempts=0

############################  Functions ######################################

def reset():
    global random_number,winner,all_correct,num_attempts,attempts
    random_number = []
    winner = False
    all_correct=False 
    num_attempts=0
    attempts=[]


#Function that displays the welcome to the game 
def welcome():
    welcome="""
    **************************************
    *                                    *
    *    Welcome to Mastermind Game!     *
    *         By Gabriela Araujo         *
    *                                    * 
    **************************************\n
    """
    reset()
    print(welcome)

def displayMenu():
    menu="""
    ***********************************************
    *                  MENU                       *
    ***********************************************
    *          Please select an option            *
    *                                             *
    * 1. Play                                     *
    * 2. Game Instructions                        *
    * 3. Top 10 best players                      *
    * 4. Exit                                     *
    *                                             *
    ***********************************************
    """
    print (menu)

# Function that displays a congratulatory message when the player matches all 4 numbers. 
def you_won(name,players):
    you_won=f"""
    ***********************************************
    *                                             *
    *              {name} you won!                *
    *                                             *
    *             Congratulations!                *
    *       You guessed the 4 digit number        *
    *         on attempt number {max_attempts-int(players[name]['player_attempts'])+1}!!               *
    *                                             *
    ***********************************************\n
    """
    print(you_won)

# Function that displays a congratulatory message when the player matches all 4 numbers. 
def game_over():
    game_over="""
    *******************************************
    *******************************************
    *                                         *
    *               GAME OVER!                *
    *                                         *
    *******************************************
    *******************************************\n
    """
    print(game_over)

#Function that obtains the 4-digit number randomly 
def get_number(difficulty_level):

    global random_number
    #The variable is reset each time it is called only save the 4 digits of the random number to be guessed.
    random_number = []
    if difficulty_level=='1':
        #request to get 4 digit random number from an api
        resp = requests.get('https://www.random.org/integers/?num=4&min=0&max=5&col=4&base=10&format=plain&rnd=new')
    
    elif difficulty_level=='2':
        resp= requests.get('https://www.random.org/integers/?num=4&min=0&max=7&col=4&base=10&format=plain&rnd=new')
    
    else:
        resp= requests.get('https://www.random.org/integers/?num=4&min=0&max=9&col=4&base=10&format=plain&rnd=new')
     
    #Variable that stores the response of the request and eliminates blanks
    num = ''.join(resp.text.split())
    #
    for digit in num:
        random_number.append(digit)
    print(random_number)

# Function that allows the player to enter a 4-digit number. 
def playerInput():
    print ("Please enter a 4-digit number")
    return input()

# Function that validates that the input data are numbers and that they are 4 digits long.
def validate_input(n):
    if (len(n)!=4 or not n.isdigit()):
      print ("Please enter only 4-digit numbers")
      return False
    else:
        return True

# Function that stores the result of the player's attempts.
def add_attempts(name,players,result):

    players[name]['attempt_history'].append({"Attempt": result})

# Function that shows the player his previous attempts and their results.  
def display_previous_attempts(name,players):
    for result in players[name]['attempt_history']:
        print(result['Attempt'])
        
# Function that evaluates the number of correct numbers and correct positions to create the results.
def result(name,players,n, correct_number_count, correct_position_count):
    global winner

    if correct_number_count==0:
        result= f"Number '{n}'. Result: All are incorrect"
        print(result)
        
        add_attempts(name,players,result )
    elif correct_position_count!=4:
        result= f"Number '{n}'. Result: {correct_number_count} correct number and {correct_position_count} correct position.\n"
        print(result)

        # Function call that stores the result of the player's attempts.
        add_attempts(name,players,result )
    else:
        you_won(name,players)
        reset()
        winner=True

# Function that evaluates the number entered by the player with respect to the random number.
def evaluate_player_number(name,players,player_number,number):

    position_digit=-1
    correct_number_count=0
    correct_position_count=0
    digits_evaluated={}

    print(number)
    for digit in player_number:
        position_digit+=1
        if digit in number:
            if digit not in digits_evaluated:
                #Cuento las veces que aparece
                count_appearances=number.count(digit)
                #Guardo en el registro las veces que aparece
                digits_evaluated[digit]=count_appearances-1
                correct_number_count +=1
                if position_digit==number.index(digit):
                    number[position_digit]='10'
                    correct_position_count +=1

            elif digit in digits_evaluated:
                if digits_evaluated[digit]>0:
                    correct_number_count +=1
                    digits_evaluated[digit] -=1
                    if position_digit==number.index(digit):
                        number[position_digit]='10'
                        correct_position_count +=1
                else:
                    if position_digit==number.index(digit):
                        number[position_digit]='10'
                        correct_position_count +=1

    
    result(name,players,player_number,correct_number_count,correct_position_count)
        

##############################  Extension  #################################

#Funtion that display message with instructions to the players
def display_instructions():
    instructions="""
    ***********************************************************************
    *                                                                     *
    *                           Instructions                              *
    *                                                                     *
    *  Mastermind is a guessing game where you must decipher a 4-digit    *
    *  number to achieve victory.With each attempt you make to guess the  *
    *  number, you will receive a feeback to help you perfect your next   *
    *  attempt. The game continues until you guess the correct code or    *
    *  exhaust all your attempts.                                         * 
    *                                                                     *
    *                   Now let's PLAY and GOOD LUCK !                    *
    *                                                                     *
    ***********************************************************************
    """
    print (instructions)


# Function that displays menu for player to choose number of players
def display_Number_of_players_menu():
    menu="""
    ***********************************************
    *                 Game Options                *
    ***********************************************
    *        Select the number of players         *
    *                                             *
    * 1. One player                               *
    * 2. Two players                              *        
    * 3. Three players                            * 
    * 2. Four players                             * 
    *                                             *
    ***********************************************
    """
    print (menu)


# Function that displays menu for player to choose difficulty level
def display_difficulty_level_menu():
    menu="""
    ***********************************************
    *                 Game Options                *
    ***********************************************
    *          Select difficulty level            *
    *                                             *
    * 1. Easy                                     *
    *     Number of digits: 4 digits              *
    *     Number range: digits from 0 to 5 only.  *
    *     Available attempts: 12 attempts.        *
    * 2. Medium                                   *
    *     Number of digits: 4 digits              *
    *     Number range: digits from 0 to 7 only.  *
    *     Available attempts: 10 attempts.        *      
    * 3. Difficult                                * 
    *     Number of digits: 4 digits              *
    *     Number range: digits from 0 to 9 only.  *
    *     Available attempts: 8 attempts.         *
    *                                             *
    ***********************************************
    """
    print (menu)
def best_player():
    return 0

# Function that validates the player's input, ensuring that it is a valid number. 
def validate_number_of_players_input():
    while True:
        option=input()
        if option.isdigit():
            op=int(option)
            if 1<=op<=4:
                return option
            else:
                print(" Please enter a valid option, the number must be in the range of 1 to 4.")
        else:
            print(" Please enter a valid option, a number from 1 to 4.  ")

# Function that validates the player's input, ensuring that it is a valid number. 
def validate_difficulty_level_input():
    while True:
        option=input()
        if option.isdigit():
            op = int(option)
            if 1<=op<=3:
                return option
            else:
                print(" Please enter a valid option, the number must be in the range of 1 to 3.")
        else:
            print(" Please enter a valid option, a number from 1 to 3.")

# Menu that shows the options of the game, these options are part of the project extensions 
def game_options():

    display_Number_of_players_menu()
    number_of_players=validate_number_of_players_input()
    display_difficulty_level_menu()
    difficulty_level=validate_difficulty_level_input()
    return difficulty_level, number_of_players

# Function that requests player names and stores them in a list
def request_player_names(number_of_players):
    players=[]
    for i in range(int(number_of_players)):
       player=input(f"Enter the name of the player number {i+1}:\n")
       players.append(player)
    return players


def initialize_player_attempts(player_names,difficulty_level):
    global num_attempts

    if difficulty_level=='1':
        players= {name:{'attempt_history':[],'player_attempts':12} for name in player_names}
        num_attempts=12

    elif difficulty_level=='2':
        players={name:{'attempt_history':[],'player_attempts':10} for name in player_names}
        num_attempts=10

    else:
        players={name:{'attempts_history':[],'player_attempts':8}for name in player_names}
        num_attempts=8

    return players

############################  Game logic  ######################################
    
def game():
    global num_attempts
    global winner 
    global all_correct
    global attempts
    global max_attempts
    
    difficulty_level,number_of_players=game_options()
    player_names=request_player_names(number_of_players)
    #Inicializamos los intentos de cada jugador segun el nivel de dificultad seleccionado:
    players=initialize_player_attempts(player_names,difficulty_level)
    get_number(difficulty_level)

    max_attempts=num_attempts

    while num_attempts>0:
    
        for name, inf in players.items():
            
            #Verifying that there is no winner
            if winner:
                break

            print (f"\n\n****             It's {name}'s turn to play             ****\n\n" )    
            
            if(inf['player_attempts']==max_attempts):
                print(f"{name}, you have {inf['player_attempts']} attempts.")
                player_num= playerInput()
                if validate_input(player_num):
                    number=random_number.copy()
                    evaluate_player_number(name,players,player_num,number)
                else:
                    player_num= input()
                    while validate_input(player_num)==False:
                        player_num= input()
                    
                    number=random_number.copy()
                    evaluate_player_number(name,players,player_num,number)
                num_attempts-=1
                inf['player_attempts'] -= 1
            else :
                print(f"{name}, you have {inf['player_attempts']} attempts.\nYour previous attempts were:\n")
                display_previous_attempts(name,players)
                player_num= playerInput()
                if validate_input(player_num):
                    number=random_number.copy()
                    evaluate_player_number(name,players,player_num, number)
                else:
                    player_num= input()
                
                    while validate_input(player_num)==False:
                        player_num= input()
                    number=random_number.copy()
                    evaluate_player_number(name,players,player_num,number)
                num_attempts-=1
                inf['player_attempts'] -= 1
        
        if num_attempts==0 and not winner:
            reset()
            game_over()
        elif winner:
            reset()


def menu_game():
    while True:
        displayMenu()
        option=input()
        if option=="1":
            game()
        elif option=="2":
            display_instructions()
        elif option== "3":
            best_player()
        elif option== "4":
            break
        else:
            print("Invalid option. Please choose a valid option.") 

welcome()
menu_game()