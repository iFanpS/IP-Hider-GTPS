#Inspired by KIPASGT
import time
import random
import threading

print("Ok we set up it....")
time.sleep(5)

def banner():
    banner1 = """
    =====================
    GTPS-IP-Host-Hider
    For your server IP
    =====================
    """
    print(banner1)

def threadings():
    for y in range(1,450):
        t = threading.Thread(target=utama)
        t.start()
        
def utama():
    ip = str(random.randint(1,255)) + '.' + str(random.randint(1,255)) + '.' + str(random.randint(1,355)) + '.' + str(random.randint(1,255))
    jangka = ''
    antarjangka = random.randint(1,30)
    for i in range(antarjangka):
        jangka += '****'
    test = open('hosts.txt', 'a+')
    test.write(jangka + ip + "growtopia1.com\n" + jangka + ip + "growtopia2.com\n" + jangka)
    test.close()

if __name__ == "__main__":
    banner()
    time.sleep(2)
    threadings()
    print("Your file has created")
