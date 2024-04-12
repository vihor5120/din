from iot_package.sensors import Sensors
import time

# Za ovaj zadatak koristite Simulator koji
# se nalazi u mapi "simulator" - simulator.py.
# Također, kako bi čitali podatke sa senzora potrebno je
# koristiti klasu `Sensors` koja je već uključena u ovoj datoteci.

# Napišite skriptu koja svake sekunde (1s) sa senzora pročita
# temperaturu i vlagu.
# Na temelju pročitanih vrijednosti skripta treba na
# zaslon (display) ispisati pripadajuću poruku.
# Idealna temperatura je u rasponu od 18-24,
# a idealna vlaga u rasponu od 40-60.
# Ako su temperatura i vlaga u idealnom rasponu treba na zaslon ispisati:
#   - "IDEALNO".
# Ako je temperatura izvan raspona treba ispisati:
#   - "GRIJEM" ako je ispod ili "HLADIM" ako je iznad.
# Ako je vlaga izvan raspona treba ispisati:
#   - "OVLAZUJEM" ako je ispod ili "SUSIM" ako je iznad.
# Ako su i temperatura i vlaga izvan raspona potrebno je ispisati obje poruke.



# Inicijalizacija senzora
sensor = Sensors()

# Idealni rasponi za temperaturu i vlagu
ideal_temperature_range = (18, 24)
ideal_humidity_range = (40, 60)

# Glavni petlja
while True:
    # Čitanje podataka sa senzora
    temperature = sensor.read_temperature()
    humidity = sensor.read_humidity()

    # Provjera temperatura
    if temperature < ideal_temperature_range[0]:
        print("GRIJEM")
    elif temperature > ideal_temperature_range[1]:
        print("HLADIM")
    else:
        print("IDEALNO")

    # Provjera vlage
    if humidity < ideal_humidity_range[0]:
        print("OVLAZUJEM")
    elif humidity > ideal_humidity_range[1]:
        print("SUSIM")
    else:
        print("IDEALNO")

    # Čekanje prije sljedeće iteracije
    time.sleep(1)