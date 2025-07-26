# multi threading - Used to perform multiple tasks concurrently
#                   Good for I/O bound tasks like reading files or fetching data from Api
#                   threading.Thread(target=myfunction)

import threading
import time

def walkcat(first):
    print(f"Walking a {first}..")
    time.sleep(8)
    print(f"Done walking the {first}.")

def takeouttrash():
    print("Taking out the trash..")
    time.sleep(3)
    print("Done taking out the trash.")

def dohomework():
    print("Doing homework..")
    time.sleep(5)
    print("Done with homework.")


chore1 = threading.Thread(target=walkcat,args=("fluffy",))
chore1.start()

chore2 = threading.Thread(target=takeouttrash)
chore2.start()

chore3 = threading.Thread(target=dohomework)
chore3.start()

chore1.join()
chore2.join()
chore3.join()
print("All chores are done!")