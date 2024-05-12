import itertools
cat_toys = [("laser",1.99),("fountain",5.99),("scratcher",10.99),("catnip",15.99)]

cat_toy_iterator = iter(cat_toys)
print(next(cat_toy_iterator))
print(next(cat_toy_iterator))
print(next(cat_toy_iterator))
print(next(cat_toy_iterator))

#####

import itertools

collars = ["Red-S","Red-M", "Blue-XS", "Green-L", "Green-XL", "Yellow-M"]

collar_combo_iterator = itertools.combinations(collars,3)
for collar in collar_combo_iterator:
  print(collar)

####

import itertools

great_dane_foods = [2439176, 3174521, 3560031]
min_pin_pup_foods = [6821904, 3302083]
pawsome_pup_foods = [9664865]

all_skus_iterator = itertools.chain(great_dane_foods,min_pin_pup_foods,pawsome_pup_foods)

for dog_food in all_skus_iterator:
  print(dog_food)

####

import itertools

max_capacity = 1000
num_bags = 0

for i in itertools.count(start=13.5, step=13.5):
    if i >= max_capacity:
        break
    num_bags += 1
print(num_bags)

#####

import itertools
cat_toys = [("laser",1.99),("fountain",5.99),("scratcher",10.99),("catnip",15.99)]

max_money = 15
options = []

toy_combos = itertools.combinations(cat_toys,2)
for combo in toy_combos:
    toy1 = combo[0]
    cost_of_toy1 = toy1[1]
    toy2 = combo[1]
    cost_of_toy2 = toy2[1]
    if cost_of_toy1 + cost_of_toy2 <= max_money:
        options.append(combo)
print(options)

######

#yield
def class_standing_generator():
  yield "Freshman"
  yield "Sophomore"
  yield "Junior"
  yield "Senior"

class_standings = class_standing_generator()

for classes in class_standings:
  print(classes)




















