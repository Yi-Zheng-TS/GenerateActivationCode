import random
import datetime
import collections

def getcode():
    now_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    rand_num = random.randint(100, 1000)
    code = str(now_time) + str(rand_num)
    return code

codes = collections.defaultdict(int)
i = 0

while i < 200:
    code = getcode()
    code = sorted(code, reverse = True)
    code = ''.join(code)
    if len(code) != 17:
        break
    if code not in codes.keys():
        codes[code] += 1
        i += 1

for num in codes:
    print(num, end = '\n')