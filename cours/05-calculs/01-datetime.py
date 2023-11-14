import datetime

# Créer une date.
ma_date = datetime.date(2023, 1, 1)
print(f"Date spécifique {ma_date}")

# Date du jour.
print(datetime.date.today())

# Créer une heure
mon_heure = datetime.time(12, 30, 10)
print(mon_heure)

# Affichage
date_formatee = ma_date.strftime("%d/%m/%Y")
print(date_formatee)

ma_datetime = datetime.datetime(2023, 2, 14, 23, 30, 11)
ma_datetime_formatee = ma_datetime.strftime("%d/%m/%Y %H:%M:%S")
print(ma_datetime_formatee)

# timedelta
maintenant = datetime.datetime.today()
avant = maintenant - datetime.timedelta(weeks=1, days=1, minutes=45, seconds=11, milliseconds=500)

# Intervalle de temps
intervalle = maintenant - avant
# print(intervalle.days)
# print(intervalle.seconds)
# print(intervalle.microseconds)
print(intervalle.total_seconds())