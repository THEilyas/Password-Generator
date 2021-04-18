#Modules
import random
#Variables
tf = random.random()
 #Password Character lenght
pcl = 1
 #Number of repetitons of the cycle
nr = 0
 #password
password = ""
 #Natural Numbers
numb = "1","2","3","4","5","6","7","8","9","0"
 #Letters
lett = "q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"
#Take Password Character lenght
pcl = int(input("Please write the number of characters to be:"))
pcl = pcl/2
#Loop 
while(True):
   if(nr == pcl):
      print(password)
      break
   #True or false
   tf = random.random()
   #Password Character lenght
   if(tf <= 0.5):
    password = numb[random.randrange(0,9)] + lett[random.randrange(0,25)] + password
   else:
    password = numb[random.randrange(0,9)] + lett[random.randrange(0,25)].upper() + password
   nr = nr + 1
