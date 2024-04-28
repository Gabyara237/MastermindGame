import requests

# 4-digit integer array of the number to be guessed by the players
Num =[]

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
    #stores each digit of the number as an integer in the Num array.
    for digit in num:
        Num.append(int(digit))



def playerInput():
    print(f"You have {num_attempts} attempts")
    print ("Please enter a 4-digit number")
    return input()


    
welcome()
get_number()

while num_attempts>0:
    if(num_attempts==10):
        player_num= playerInput()
        num_attempts-=1
    else :
        print(f"You have {num_attempts} attempts and your previous results were:")
        num_attempts-=1





