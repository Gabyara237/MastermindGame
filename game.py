import requests


random_number = []


#
all_correct=False

#
num_attempts=10

attempts=[]

#Function that displays the welcome to the game 
def welcome():
    print("**************************************")
    print("*    Welcome to Mastermind Game!   *")
    print("*         By Gabriela Araujo       *")
    print("**************************************\n")
 
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


def playerInput():
    print(f"You have {num_attempts} attempts")
    print ("Please enter a 4-digit number")
    return input()


def validate_input(n):
    if (len(n)!=4 or not player_num.isdigit()):
      print ("Please enter only 4-digit numbers")
      return False
    else:
        return True

def result():

    return 0
    
def evaluate_player_number(n,number):

    position_digit=-1
    correct_number_count=0
    correct_position=0
     
    print(number)
    for digit in n:
        position_digit+=1
        print (position_digit)
        if digit in number:
            correct_number_count +=1
            if position_digit==number.index(digit):
                print(f"{position_digit} y {number.index(digit)}")
                number[position_digit]='10'
                correct_position +=1
    
    result(correct_number_count,correct_position)
        





    
welcome()
get_number()

while num_attempts>0:
    if(num_attempts==10):
        player_num= playerInput()
        if validate_input(player_num):
            number=random_number
            evaluate_player_number(player_num, number)
        else:
            player_num= input()
            while validate_input(player_num)==False:
                player_num= input()
            evaluate_player_number(player_num)
        num_attempts-=1

    else :
        print(f"You have {num_attempts} attempts and your previous results were:")
        num_attempts-=1





