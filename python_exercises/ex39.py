states={
        'Oregon':'OR',
        'Florida':'FL',
        'Califorina':'CA',
        'New York':'NY',
        'Michigan':'MI'
        }
cities={
        'CA':'San Francisco',
        'MI':'Detroit',
        'FL':'Jacksonville'
        }
cities['NY']='New York'
cities["OR']='Portkand'
print('-'*10)
print("NY State has:",cities['NY'])
print("OR State has:",cities['OR'])
print('-'*10)
print("Michigan's abbrevation is:",states['NY'])
print("Florida's abbrevation is:",states['OR'])
print('-'*10)
print("Michigan has:",cities[states['Michigan']])
print("Florida has:",cities[sttes['Florida']])
print('-'*10)
for state, abbre in list(states.items()):
print(f"{state} is abbreviated {abbrev}")
print('-'*10)
for abbrev, city in list(cities.items():
print(f"{abbrev} has the city{city}")
print('-'*10)
for state, abbrev in list(states.items()):
print(f"{state} state is abbreviated {abbrev}")
print(f"and has city {cities[abbrev]}")
print('-'*10)
staate=states.get('Texas')
if not state:
print("Sorry, no Texas.")
city=cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")
