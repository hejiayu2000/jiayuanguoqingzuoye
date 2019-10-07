time1 = input('What year were you born ?')
time2 = input('What month were you born ?')
time3 = input('What date were you born ?')
from datetime import datetime 
now = datetime.now()
time4 = datetime.now().strftime('%Y-%m-%d')
b = (time4[0:4])
str = b + time2 + time3
birth = time1 + '/'+ time2 + '/'+time3
import time
time5 = datetime.strptime(str,'%Y%m%d')
time6 = ((time5-now).days)
Time_1 = time6 + 366
time7 = time6 + 1
print('It looks like you were born in ',birth,'days')
if time6 >= 0 :
    print('It seems your birthday is in ',time7,'days')
else:
    print('It seems your birthday is in',Time_1)
print('Wish you have a nice birthday! ','\nDesigned by ncuhomer')
