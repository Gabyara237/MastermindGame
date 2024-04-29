import requests

############################  Global variables ######################################
random_number = []

winner = False

#
all_correct=False

#Variable that stores the number of attempts of a player. 
num_attempts=10

# List containing all the attempts of a player
attempts=[]


############################  Functions ######################################

#Function that displays the welcome to the game 
def welcome():
    print("**************************************")
    print("*    Welcome to Mastermind Game!   *")
    print("*         By Gabriela Araujo       *")
    print("**************************************\n")
 

# Function that displays a congratulatory message when the player matches all 4 numbers. 
def you_won():
    print("*******************************************")
    print("*      You won! Congratulations!          *")
    print("*   You guessed the 4 digit number!!      *")
    print("*****************************************\n")


#Function that obtains the 4-digit number randomly 
def get_number():

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
    if (len(n)!=4 or not player_num.isdigit()):
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
        winner=True

# Function that evaluates the number entered by the player with respect to the random number.
def evaluate_player_number(n,number):

    position_digit=-1
    correct_number_count=0
    correct_position_count=0
     
    print(number)
    for digit in n:
        position_digit+=1
        if digit in number:
            correct_number_count +=1
            if position_digit==number.index(digit):
                number[position_digit]='10'
                correct_position_count +=1

    
    result(n,correct_number_count,correct_position_count)
        




############################  Game logic  ######################################
    
welcome()
get_number()

while num_attempts>0:
    #Verifying that there is no winner
    if winner:
        break
    
    if(num_attempts==10):
        print(f"You have {num_attempts} attempts.")
        player_num= playerInput()
        if validate_input(player_num):
            number=random_number.copy()
            evaluate_player_number(player_num, number)
        else:
            player_num= input()
            while validate_input(player_num)==False:
                player_num= input()
                number=random_number.copy()
            evaluate_player_number(player_num, number)
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
            evaluate_player_number(player_num,number)
        num_attempts-=1





