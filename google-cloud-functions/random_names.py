import random
import datetime

#def hello_pubsub(event, context): #Only if using PubSub
def hello_pubsub():
  names = ["Daisy", "Mary", "Charlie", "Debra", "Thomas", "Cora", "Robert", "Violet", 'Matthew', 'Richard', 'Bertie', 'Shrimpie']
  today = datetime.date.today()
  dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

  def ChooseTwice(items):
      a = random.choice(items)
      b = random.choice(items)
      return a, b

  (one, two) = ChooseTwice(names)
  if one == two:
    print("%s is happy!" % one, today)
  else:
    print("%s likes %s!" % (one, two), dt)
  return "Success at " + str(dt) 


hello_pubsub()