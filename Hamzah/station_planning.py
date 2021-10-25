from stations_challenge import *

sub_station2 = SubwayStation(station_name = 'Malik al-Shabazz', location = 'Crenshaw Blvd and Manchester Ave', lines = ['S', 'A1', 'L', 'A2', 'M'])
sub_station2.show_info()

bus_station2 = BusStation(station_name = 'Rosa Parks', location = 'Centinela Ave and La Brea Blvd', routes = ['Purple', 'Blue', 'Green', 'Red'])
bus_station2.show_info()
bus_station2.open_station()
bus_station2.close_station()

sub_station3 = SubwayStation(station_name = 'Musa Richardson', location = 'Sepulveda Blvd and Artesia Blvd', lines = ['Testification', 'Prayer', 'Fasting', 'Charity', 'Pilgrimage'])
sub_station3.show_info()