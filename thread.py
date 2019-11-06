import threading
import time

def worker(message):
    for i in range(0, 5):
        print(message)
        time.sleep(1)

t = threading.Thread(target=worker, args = ("thread sendo executada",))
t.start()

for x in range(0, 10):
    print(x)
    time.sleep(1)

while t.isAlive():
    print("aguardando thread")
    time.sleep(5)

print("A thread morreu")
print("Finalizando programa")