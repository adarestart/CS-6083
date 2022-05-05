from datetime import datetime
from random import random, randint

now = datetime.now()
strnow = datetime.strftime(now,'%Y%m%d%H%M')
strnow = strnow + str(randint(1000,9999))
print(strnow)