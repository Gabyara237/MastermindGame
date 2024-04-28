import requests


random_number=0

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
    random_number=(int(num))



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

        

    
welcome()
get_number()

while num_attempts>0:
    if(num_attempts==10):
        player_num= playerInput()
        if validate_input(player_num):
            print("correct")
        else:
            player_num= input()
            while validate_input(player_num)==False:
                player_num= input()
        
        num_attempts-=1

    else :
        print(f"You have {num_attempts} attempts and your previous results were:")
        num_attempts-=1





