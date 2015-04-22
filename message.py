import random


class Contact:
  def __init__(self, name, telno, email, fbname):
    self.name = name
    self.telno = telno
    self.email = email
    self.fbname = fbname

contacts = [
  Contact("Test Name", "07414060544", "test@testname.com", "testname"), 
  Contact("Jane Doe", "07416666433", "jane@janedoe.com", "janedoe"),
  Contact("John Smith", "07489898433", "john@johsmith.com", "johnsmith"),
]

user_details = ["My Name", "09090909090", "test@myname.com", "mytestname1"]
print "my name is "+ user_details[0]

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
  mediums = ["email", "sms", "fbmsg"]
  medium = mediums[random.randint(0, len(mediums)-1)]

  choice = random.randint(0, len(contacts)-1)
  contact = contacts[choice]
  contact_val = 0
  
  contact_str = contact.email
  if medium == "email":
    contact_str = contact.email
  elif medium == "sms":
    contact_str = contact.telno
  else:
    contact_str = contact.fbname
  
  for c in contact_str:
    n = ord(c)
    contact_val = contact_val+n 
  contact_val = contact_val % len(alpha_lower_A)
  
  if char_val < 10:
    first_half = True
  else:
    first_half = False
    char_val = char_val % 10
    
  contact_val = contact_val % 10
  
  if char_val < contact_val:
    length = char_val + 10 - contact_val
  else:
    length = char_val - contact_val
  
  output_alpha_A(medium, direction, contact.name, contact_str, first_half, length)

  
  
def output_alpha_A(medium, direction, contact_name, contact_str, first_half, length):
  medium_friendly = {'email': 'an email', 'sms': 'a text message', 'fbmsg': 'a Facebook message'}[medium]
  direction1_friendly = "send" if direction == "OUT" else "recieve"
  direction2_friendly = "to" if direction == "OUT" else "from"
  direction1_friendlyB = "send" if direction == "IN" else "recieve"
  direction2_friendlyB = "to" if direction == "IN" else "from"
  time_friendly = "even" if first_half else "odd"

  if medium == 'sms': 
    user_details_friendly = user_details[1] 
  elif medium == 'email':
    user_details_friendly = user_details[2] 
  else: 
    user_details_friendly = user_details[3]
  
  print "Please {0} {1} {2} {3} ({4}) on an {5} minute with a word count whose last digit is {6}".format(direction1_friendly, medium_friendly, direction2_friendly, contact_name, contact_str, time_friendly, length)

  if direction == "IN":
    print "Instruction for {0}: Please {1} {2} {3} {4} ({5}) on an {6} minute with a word count whose last digit is {7}" .format(contact_name, direction1_friendlyB, medium_friendly, direction2_friendlyB, user_details[0], user_details_friendly, time_friendly, length)
  
  
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
    
    
