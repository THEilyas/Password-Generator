#Modules
import time
import random
#Variables
 #boolean
rgt = random.getrandbits(1)
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
#Loop 
while(True):
   if(nr == pcl):
    break
   #True or false before (a ,a ) after (A,a)
   tf = random.getrandbits(1)
   # Lower case letter and numbers
   if(tf <= 0.5):
     #random a bool 1 or 0
     rgt = random.getrandbits(1)
     #If the bool we randomly picked is less than 0.5, do this.
     if(rgt <= 0.5):
       password = numb[random.randrange(0,9)] + password
     #If the bool we get randomly is greater than 0.5, do this
     elif(rgt >= 0.5):
        password = lett[random.randrange(0,25)] + password
   # Uppercase letter and numbers
   else:
      #random a bool 1 or 0
      rgt = random.getrandbits(1)
      #If the bool we randomly picked is less than 0.5, do this.
      if(rgt <= 0.5):
        password = numb[random.randrange(0,9)] + password
      #If the bool we get randomly is greater than 0.5, do this
      elif(rgt >= 0.5):
        password = lett[random.randrange(0,25)].upper() + password
   nr = nr + 1
#Decor
print("_" * pcl)
#Write consol the password
print(password)
#Decor
print("_" * pcl)
save = input("Save your password in the text document? \n yes/no :")
if(save == "yes"):
   #take date
   date = time.localtime()
   #create name
   file_name = str("YourPasswordIsHere ") + str(date.tm_year) + str(date.tm_mon) + str(date.tm_mday) + str(date.tm_min) + str(".txt")
   #open file
   file = open(file_name , "w")
   #Write file
   file.write(password)
   file.close()
else:
  input("Press enter for exit.")
#developer: ilyas YILDIZ
#STORM Studio Bilişim Teknolojileri ürünüdür.
