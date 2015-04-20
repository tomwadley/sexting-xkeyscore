import random


class Contact:
  def __init__(self, name, telno, email):
    self.name = name
    self.telno = telno
    self.email = email

contacts = [
  Contact("Test Name", "07414060544", "test@testname.com"), 
  Contact("Jane Doe", "07416666433", "jane@janedoe.com"),
  Contact("John Smith", "07489898433", "john@johsmith.com"),
]


alpha_lower_A = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "l", "m", "n", "o", "p", "r", "s", "t", "u", "w", "y"]
alpha_lower_B = ["j", "k", "q", "v", "x", "z"]
alpha_upper_A = []
alpha_upper_B = []
 
for c in alpha_lower_A:
  alpha_upper_A.append(c.upper())
  
for c in alpha_lower_B:
  alpha_upper_B.append(c.upper())
  
initial_stop = "Tooting"
current_stop = initial_stop 

message = "This is my fist Message to XKeyscore. x A 123 :-)"


def process_alpha_A(direction, char, char_val):
  print direction + " " + char + " A "
  choice = random.randint(0, len(contacts)-1)
  contact = contacts[choice]
  contact_val = 0
  for c in contact.email:
    n = ord(c)
    contact_val = contact_val+n 
  contact_val = contact_val % len(alpha_lower_A)
  print "the value of Contact's Email is " + str(contact_val) + " and taget is " + str(char_val)
  
  
def process_alpha_B(direction, char):
  print direction + " " + char + " B "

for i in message:
  
  if i == " ":
    choice = random.randint(0, 1)
    if choice == 0:
      print "Tweet."
    else:
      print "Post a Facebook status update."
  
  elif i in alpha_lower_A:
    char_val = alpha_lower_A.index(i)
    process_alpha_A("OUT", i, char_val)
        
  elif i in alpha_lower_B:
    process_alpha_B("OUT", i)
    
  elif i in alpha_upper_A:
    char_val = alpha_upper_A.index(i)
    process_alpha_A("IN", i, char_val)
    
  elif i in alpha_upper_B:
    process_alpha_B("IN", i)
      
  else:
    print "boo " + i
    
    
