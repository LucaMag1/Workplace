import itertools
guests = {}
def read_guestlist(file_name):
    global age
    text_file = open(file_name,"r")
    while True:
        line_data = text_file.readline().strip().split(",")
        if len(line_data) < 2:
            text_file.close()
            break
        name = line_data[0]
        age = int(line_data[1])
        guests[name] = age
        yield name

gen = read_guestlist("C:\\Guest_list.txt")
for i in range(1,11):
    print(next(gen))

guests["Jane"]=35

for name in gen:
    print(name)
print("\n")
over_21 = (name for name,age in guests.items() if age>=21)
for name in over_21:
    print(name)

print("\n")

def table1():
    for i in range(1,6):
        yield ("Chicken","Table 10","seat {}".format(i))

def table2():
    for i in range(1,6):
        yield ("Beef","Table 2","seat {}".format(i))

def table3():
    for i in range(1,6):
        yield ("Fish","Table 3","seat {}".format(i))

def all_tables():
    yield from table1()
    yield from table2()
    yield from table3()

assign_table = all_tables()
def table_assignment(guests):
    for name in guests:
        yield(name,next(assign_table))

guest_assignment = table_assignment(guests)
for person in guest_assignment:
    print(person)