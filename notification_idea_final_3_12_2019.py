import time
import http.client, urllib
import win32com.client
import random

push_token = "a86uzrsupvke834n922nj6y2o9tg7x"
push_user = "u98y6m35pg5zhnfaptbkf4d35q4tmv"
reg = 5179
payment = 89393
online_klienti = random.randint(10, 40)
timeout = 0.5
iteracija = 0

while True:
    jaunas_reg = random.randint(0, 2)
    jauni_payments = random.randint(0, 6)
    jauni_klienti = random.randint(-10, 10)
    e_pasti = random.randint(0, 2)
    if iteracija is 0:
        titleprint='Statistika'
        messageprint='Pēdējā reģistrācija: ' + str(reg) + '\nPēdējais maksājums: ' + str(payment) + '\nOnline klienti: ' + str(online_klienti) + '\nNelasīti e-pasti: ' + str(e_pasti)
    else:
        if jauni_klienti >= 0:
            vm = ' (pieaugums par '
        else:
            vm = ' (sarukums par '
        reg = reg + jaunas_reg
        payment = payment + jauni_payments
        online_klienti = online_klienti + jauni_klienti
        titleprint='Pēdejo ' + str(timeout) + ' minūšu statistika'
        messageprint='Jaunas reģistrācijas: ' + str(jaunas_reg) + '\nJauni maksājumi: ' + str(jauni_payments) + '\nOnline klienti: ' + str(online_klienti) + vm + str(abs(jauni_klienti)) + ")" + '\nNelasīti e-pasti: ' + str(e_pasti)
    
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
        urllib.parse.urlencode({
            "token": push_token,
            "user": push_user,
            "title": titleprint,
            "message": messageprint,
    }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()

    iteracija = iteracija + 1
    time.sleep(timeout*60)
