import threading
import time

request=None

def worker():
    request=Reuqest()
    print('i m a thread')
    t = threading.current_thread()
    time.sleep(8)
    print(t.getName())


new_t =threading.Thread(target=worker,name='Sep_Thread')
new_t.start()
new_t =threading.Thread(target=worker,name='Sep_Thread')
new_t.start()
new_t =threading.Thread(target=worker,name='Sep_Thread')
new_t.start()

request

t=threading.current_thread()
print(t.getName())
new_t.join()