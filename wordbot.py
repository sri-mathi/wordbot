from random import randint
def greet_random():
  greetings=["hi","hey","vanakam","hello","howdy","yo"]
  mm=" Buddy"
  return(greetings[randint(0,len(greetings))]+mm)
greeting=greet_random()
quit_msg=['bye','quit','exit','Thank you','end']
print(greet_random(),',',"I'm wordbot.I can display the synonyms and antonyms for a given word.")
while True:
  msg = input()
  if msg in quit_msg:
    break
  elif "bold" in msg:
      syn=['adventuresome', 'adventurous', 'audacious', 'daring', 'dashing', 'emboldened', 'enterprising', 'free-swinging']
      ant=['unadventurous', 'unenterprising']
      n=randint(0,len(syn))
      print("Synonyms: ",syn[n-1])
      n=randint(0,len(ant))
      print("Antonyms: ",ant[n-1])
  elif "calm" in msg:
      syn=['peaceful', 'placid', 'quiet', 'serene', 'still', 'stilly']
      ant=['agitated', 'angry', 'inclement', 'restless', 'rough', 'stormy']
      n=randint(0,len(syn))
      print("Synonyms: ",syn[n-1])
      n=randint(0,len(ant))
      print("Antonyms: ",ant[n-1])
  elif "decay" in msg:
      syn=['debilitation', 'decaying', 'declension', 'decline', 'degeneration', 'descent', 'deterioration']
      ant=['comeback', 'improvement', 'rally', 'recovery', 'recuperation','rehabilitation']
      n=randint(0,len(syn))
      print("Synonyms: ",syn[n-1])
      n=randint(0,len(ant))
      print("Antonyms: ",ant[n-1])
  else:
    print("Sorry,Some Error")
