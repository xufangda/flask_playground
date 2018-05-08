from werkzeug.local import LocalStack
import threading

s=LocalStack()

s.push(1)
print('in main thread after push, top is '+ str(s.top))

def worker():
    print('in new thread after push top is'+ str(s.top))
    s.push(2)
    print('in new thread after new push top is'+ str(s.top))
    
new_t=threading.Thread(target=worker)
new_t.start()
s.push(3)
print('finally, in main thread top is '+str(s.top))
