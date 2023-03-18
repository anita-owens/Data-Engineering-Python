import random
import os
from datetime import date
from datetime import datetime

def env_vars(request):
    return os.environ.get('FOO', 'Specified environment variable is not set.')

def hello_pubsub(event, context):
  names = ["Alice", "Bob", "Charlie", "Debra", "Peter", "Cora", "Robert", "Violet"]
  today = date.today()
  dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

  def ChooseTwice(items):
      a = random.choice(items)
      b = random.choice(items)
      return a, b

  (one, two) = ChooseTwice(names)
  if one == two:
    print("%s is happy!" % one, dt)
  else:
    print("%s likes %s!" % (one, two), dt)