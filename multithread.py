import threading
import time
def display():
    for i in range(1,10):
        print(f"{threading.current_thread().name}  {i}")
t1=threading.Thread(target=display,name="T1")
t2=threading.Thread(target=display,name="T1")
t3=threading.Thread(target=display,name="T1")
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print("Finished")
