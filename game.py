import requests

# 4-digit integer array of the number to be guessed by the players
Num =[]

#Function that obtains the 4-digit number randomly 
def Getnumber():

    #request to get 4 digit random number 
    resp = requests.get('https://www.random.org/integers/?num=4&min=0&max=7&col=4&base=10&format=plain&rnd=new')
   
   #Variable that stores the response of the request and eliminates blanks
    num = ''.join(resp.text.split())

    #stores each digit of the number as an integer in the Num array.
    for digit in num:
        Num.append(int(digit))
    

Getnumber()




