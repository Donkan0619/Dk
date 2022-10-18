import random
import sys
import time 
def mengetik (s):
  for c in s + '\n':
       sys.stdout.write(c)
       sys.stdout.flush()

       time.sle(random.random()*0.3)

