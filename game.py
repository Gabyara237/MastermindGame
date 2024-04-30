import requests

############################  Global variables ######################################

# Variable where the number to be guessed is stored
random_number = []

# Variable storing if a player has won
winner = False

# Boolean variable storing the status of all hits 
all_correct=False

#Variable that stores the number of attempts of a player. 
num_attempts=10

# List containing all the attempts of a player
attempts=[]


############################  Functions ######################################


def reset():
    global random_number,winner,all_correct,num_attempts,attempts
    random_number = []
    winner = False
    all_correct=False 
    num_attempts=10
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
def you_won():
    you_won="""
    *******************************************
    *                                         *
    *      You won! Congratulations!          *
    *   You guessed the 4 digit number!!      *
    *                                         *
    *******************************************\n
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
def get_number():
    global random_number
    #The variable is reset each time it is called only save the 4 digits of the random number to be guessed.
    random_number = []

    #request to get 4 digit random number 
    resp = requests.get('https://www.random.org/integers/?num=4&min=0&max=7&col=4&base=10&format=plain&rnd=new') 
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
def add_attempts(result):
    attempts.append({"Attempt": result})

# Function that shows the player his previous attempts and their results.  
def display_previous_attempts():
    for result in attempts:
        for clave, valor in result.items():
            print(f"{clave}: {valor}")
            print()  

# Function that evaluates the number of correct numbers and correct positions to create the results.
def result(n, correct_number_count, correct_position_count):
    global winner

    if correct_number_count==0:
        result= f"Number '{n}'. Result: All are incorrect"
        print(result)
        add_attempts(result )
    elif correct_position_count!=4:
        result= f"Number '{n}'. Result: {correct_number_count} correct number and {correct_position_count} correct position.\n"
        print(result)
        # Function call that stores the result of the player's attempts.
        add_attempts(result )
    else:
        you_won()
        reset()
        winner=True

# Function that evaluates the number entered by the player with respect to the random number.
def evaluate_player_number(n,number):

    position_digit=-1
    correct_number_count=0
    correct_position_count=0
    digits_evaluated={}
    

    print(number)
    for digit in n:
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

    
    result(n,correct_number_count,correct_position_count)
        

##############################  Extension  #################################

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

def best_player():
    return 0

############################  Game logic  ######################################
    
def game():
    global num_attempts
    global winner 
    global all_correct
    global attempts
    get_number()
    
    print(num_attempts)
    while num_attempts>0:
        #Verifying that there is no winner
        if winner:
            reset()
            break
        
        if(num_attempts==10):
            print(f"You have {num_attempts} attempts.")
            player_num= playerInput()
            if validate_input(player_num):
                number=random_number.copy()
                evaluate_player_number(player_num,number)
            else:
                player_num= input()
                while validate_input(player_num)==False:
                    player_num= input()
                
                number=random_number.copy()
                evaluate_player_number(player_num,number)
            num_attempts-=1
        else :
            print(f"You have {num_attempts} attempts.\nYour previous attempts were:\n")
            display_previous_attempts()
            player_num= playerInput()
            if validate_input(player_num):
                number=random_number.copy()
                evaluate_player_number(player_num, number)
            else:
                player_num= input()
            
                while validate_input(player_num)==False:
                    player_num= input()
                number=random_number.copy()
                evaluate_player_number(player_num,number)
            num_attempts-=1


    if num_attempts==0 and not winner:
        reset()
        game_over()



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