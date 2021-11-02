from stations_challenge import *

monclova_station= BusStation(station_name='Monclova Station', location = 'Zona Centro 25700', routes = ['Dallas' 'Corpus Cristi','Lorado'])

tyler_vernon_station= SubwayStation(station_name='Tyler/Vernon Station', location='1225 S Tyler St, Dallas, TX 75208', lines=['Red', 'Blue', 'Green', 'Orange'])

King_Cross_Station= SubwayStation(station_name='Kings Cross Station', location='Euston Rd', lines=['Red', 'Blue', 'Green', 'Orange'])

monclova_station.show_info()
tyler_vernon_station.show_info()
King_Cross_Station.show_info()

# 'Red', 'Blue', 'Green', 'Orange'