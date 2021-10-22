from stations_challenge import *

paris = SubwayStation(station_name = 'Baguette Ave', 
    location= "Baguette Avenue & Fromage Street", 
    lines = ['Bread', 'Cheese'])

london = SubwayStation(station_name='Trafalgar St', 
    location='Trafalgar St and Grosvenor Terrace', 
    lines = ['Covent Garden', 'Excelsior', 'Picacadilly', 'Waterloo'])

barcelona = BusStation(station_name = 'Las Ramblas', 
    location = 'Las Ramblas and Plaza de Catalunya', 
    routes = ['La Boqueria', 'Gopal', 'Vegetalia'])

paris.show_info()
london.show_info()
barcelona.show_info()