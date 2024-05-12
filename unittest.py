#Raise keyerror
"""instrument_catalog = {
  'Marimba': 1999,
  'Kora': 499,
  'Flute': 899
}

def print_instrument_price(instrument):
  if instrument in instrument_catalog:
    print('The price of a ' + instrument + ' is ' + str(instrument_catalog[instrument]))
  else:
    raise KeyError(instrument + "is not found in instrument catalog!")

print_instrument_price('Marimba')
print_instrument_price('Flute')
print_instrument_price('Piano')"""

# try/except zerodivision error
staff = {
  'Austin': {
      'floor managers': 1,
      'sales associates': 5
  },
  'Melbourne': {
      'floor managers': 0,
      'sales associates': 8
  },
  'Beijing': {
      'floor managers': 2,
      'sales associates': 5
  },
}

"""def print_staff_report(location, staff_dict):
  managers = staff_dict['floor managers']
  sales_people = staff_dict['sales associates']
  ratio = sales_people / managers
  print('Instrument World ' + location + ' has:')
  print(str(sales_people) + ' sales employees')
  print(str(managers) + ' floor managers')
  print('The ratio of sales people to managers is ' + str(ratio))
  print()

for location, staff in staff.items():
  try:
    print_staff_report(location, staff)
  except ZeroDivisionError as e:
    print("Could not print sales report for " + location)
    print(e)
    print("\n")"""

#multiple exceptions
"""instrument_prices = {
  'Banjo': 200,
  'Cello': 1000,
  'Flute': 100,
}

def display_discounted_price(instrument, discount):
    full_price = instrument_prices[instrument]
    discount_percentage = discount / 100
    discounted_price = full_price - (full_price*discount_percentage)
    print("The instruments discountprice is: " + str(discounted_price))

instrument = "Banjo"
discount = 20

try:
    display_discounted_price(instrument,discount)
except KeyError:
    print("An invalid instrument was entered!")
except TypeError:
    print("Discount percentage must be a number!")
#generic exception as backup if no other specific exception gets caught
except Exception:
    print("Hit an exception other than KeyError and TypeError!")"""

#else
"""customer_rewards = {
  'Zoltan': 82570,
  'Guadalupe': 29850,
  'Mario': 17849
}

def display_rewards_account(customer):
    try:
        rewards_number = customer_rewards[customer]
    except KeyError:
        print("Customer was not found in rewards program!")
    else:
        print("Rewards account number is "+str(rewards_number))

customer = "Mario"
display_rewards_account(customer)"""

#finally
# add database to seperate file to run properly
"""instruments = {
    'Kora': {
        'Family': 'Strings',
        'Origin': 'West Africa',
    },
    'Didgeridoo': {
        'Family': 'Wind',
        'Origin': 'Northern Australia',
    },
    'Guitar': {
        'Family': 'Strings',
        'Origin': 'Spain',
    }
}

def connect_to_database():
    print('Establishing connection to instrument database server...')

def disconnect_from_database():
    print('Destroying connection to instrument database server...')

def get_instrument_info(instrument):
    return instruments[instrument]

def display_instrument_info(instrument):
    info = get_instrument_info(instrument)
    print('Instrument: ' + instrument)
    print('Family: ' + info['Family'])
    print('Origin: ' + info['Origin'])

instrument = "Kora"
database.connect_to_database()

try:
    database.display_instrument_info(instrument)
except KeyError:
    print("instrument doesn't exist")
else:
    print(instrument)
finally:
    database.disconnect_from_database()"""

#user-defined exceptions
inventory = {
  'Piano': 3,
  'Lute': 1,
  'Sitar': 2
}

class InventoryError(Exception):
    def __init__(self,supply):
        self.supply = supply

    def __str__(self):
        return "Availabe supply is only: "+str(self.supply)

def submit_order(instrument,quantity):
    supply = inventory[instrument]
    if quantity>supply:
        raise InventoryError(supply)
    else:
        inventory[instrument] -= quantity
        print("Successfully placed order. Remaining supply: "+ str(inventory[instrument]))

instrument = "Piano"
quantity = 9
submit_order(instrument,quantity)








