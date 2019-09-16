import time as t

t1=t.time()
print('1970.1.1 0~now:{}seconds'.format(int(t1)))

t2=t.gmtime()
print(t2)

print('\n UTC time')
print('{}y {}m {}d'.format(t2.tm_year,t2.tm_mon,t2.tm_mday))
print('{}hr {}min {}sec'.format(t2.tm_hour,t2.tm_min,t2.tm_sec))

t3=t.localtime()
print('\n local-This PC time')
print('{}y {}m {}d'.format(t3.tm_year,t3.tm_mon,t3.tm_mday))
print('{}hr {}min {}sec'.format(t3.tm_hour,t3.tm_min,t3.tm_sec))

if t2.tm_wday==0:
	w='Mon'
elif t2.tm_wday==1:
	w='Tue'
elif t2.tm_wday==2:
	w='Wed'
elif t2.tm_wday==3:
	w='Thu'
elif t2.tm_wday==4:
	w='Fri'
elif t2.tm_wday==5:
	w='Sat'
elif t2.tm_wday==6:
	w='Sun'
else:
	pass
print('\n It is {} today'.format(w))

print('\n{}y {}m {}d is {}th day.'.format(t2.tm_year,t2.tm_mon,t2.tm_mday,t2.tm_yday))
print('{}y only left {} days.'.format(t2.tm_year,365-t2.tm_yday))

for i in range(10):
	print(' . ',end=' ')
	t.sleep(1)
	
print('\n************************')

for i in range(10):
	print(' . ', end=' ')
	t.sleep(2)
	

