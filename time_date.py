# import time
# import datetime
#
# print("Running Time and Date module...")
# print(time.gmtime(0))       #always works in etc
# # print(time.localtime())     #to see local time
# # print(time.time())
# # print(time.localtime(time.time()))
# time_here = time.localtime()
# print(time_here)
# '''these are two ways of accessing the elements can be written in either way
#     will result the same, tuple is used tho access the elements, can be called by their location or by
#     their name'''
# print("YEAR: ",time_here[0], time_here.tm_year)
# print("MONTH: ",time_here[1], time_here.tm_mon)
# print("DAY: ",time_here[2], time_here.tm_mday)

import time
from time import perf_counter as my_timer
'''instead of using time we can use perf_counter or monotonic for more precise value
    for process_time it gives even more precise value.'''
import random
'''Recodring when the enter was pressed'''
input("Press Enter to start")     #starts the time calculation.
wait_time=random.randint(1, 3)    #waits for a random time before it starts the process.
time.sleep(wait_time)
start_time=my_timer()   #it stores the current time when it wakes up.
input("Press Enter to stop")   #when u press enter after this line, it records the time diff. between them in  seconds
print("\n")
end_time=my_timer()             #end the timer calculation.
print("Started at "+time.strftime("%X", time.localtime(start_time)))  #print the start time, strftime is string format ime that is made more readable bu using tuple.
print("Stopped at "+time.strftime("%X", time.localtime(end_time)))    #print the end time, strftime same as the above line.
print("Your reaction time was {} seconds".format(end_time - start_time)) #print the reaction time

'''Refer Documentation for complete properties'''
