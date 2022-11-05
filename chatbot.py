from random import randint
def greet_random():
  greetings=["hi","hey","vanakam","hello","howdy","yo"]
  mm=" Buddy"
  return(greetings[randint(0,len(greetings))]+mm)
quit_msg=['bye','quit','exit','Thank you','end']
print(greet_random(),',',"I'm chatbot.Let's perform a simple calculations")
while True:
  msg = input()
  if msg in quit_msg:
    break
  elif "add" in msg:
      split_msg=msg.split()
      p1 = int(split_msg[1])
      p2 = int(split_msg[2])
      print(p1+p2)
  elif "sub" in msg:
      split_msg=msg.split()
      p1 = int(split_msg[1])
      p2 = int(split_msg[2])
      print(p1-p2)
  elif "mul" in msg:
      split_msg=msg.split()
      p1 = int(split_msg[1])
      p2 = int(split_msg[2])
      print(p1*p2)
  elif "div" in msg:
      split_msg=msg.split()
      p1 = int(split_msg[1])
      p2 = int(split_msg[2])
      print(p1/p2)
  elif "sqr" in msg:
      split_msg=msg.split()
      p1 = int(split_msg[1])
      p2=2
      print(p1**p2)
    
