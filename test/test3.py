from werkzeug import Local 
import threading
import time

class A:
    b=1

my_obj=Local()
my_obj.b=1
def worker():
    my_obj.b=2
    print('in new thread b is :' +str(my_obj.b))

new_t=threading.Thread(target=worker, name='sub_thread')

new_t.start()

time.sleep(1)

print('in main thread b is:' +str(my_obj.b))