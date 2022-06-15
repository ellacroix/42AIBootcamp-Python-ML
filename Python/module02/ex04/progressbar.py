import os
import time
from timeit import default_timer as timer

def ft_progress(lst):
	start = timer()
	for i in lst:
		yield i
		os.system('cls' if os.name == 'nt' else 'clear')
		print("ETA: ", '{:.2f}'.format(timer()*((max(lst)+1))/(i+1)), 's ', '[', '{:3.0f}'.format(i/max(lst)*100), '%]', '[', ("{0}".format("=")*int((i/max(lst))*10)), '>'.ljust(11-(int(i/max(lst)*10))), '] ', i+1, "/", max(lst)+1, " | elapsed time ", '{:.2f}'.format(timer()), 's', sep = "")
		print("...")
		
listy = range(3333)
ret = 0
for elem in ft_progress(listy):
	ret += elem
	time.sleep(0.005)
print()
print(ret)