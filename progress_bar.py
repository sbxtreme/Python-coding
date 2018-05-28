import time
import sys
import time

start=time.time()
total = 9 # Number of iterations/seconds for which program will execute
bar_length = 36  # should be less than 100
for i in range(total+1):
    time.sleep(1)
    percent = 100.0*i/total
    sys.stdout.write('\r')
    sys.stdout.write("Completed: [{:{}}] {:>3}%"
                     .format('#'*int(percent/(100.0/bar_length)),
                             bar_length, int(percent)))
sys.stdout.flush()
end=time.time()
print("\n",int(end-start),'seconds')