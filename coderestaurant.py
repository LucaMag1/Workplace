"""tables = {1:{"name":"Luca","vip_status":True,"order":"juice, pancake"},2:{},3:{}}

def assign_table(table_number,name,vip_status=False,*order_items):
    tables[table_number]["name"] = name
    tables[table_number]["vip_status"] = vip_status
    tables[table_number]["order"] = ""

assign_table(2,"Leclerc",False)
print(tables)

def assign_order(table_number,*order_items):
    tables[table_number]["order"] = order_items
    for item in order_items:
        return(item)

assign_order(2,"meat","fries","pasta")
print(tables)"""

tables = {1:{},2:{},3:{}}

def assign_table(table_number, name, vip_status=False,**order):
    tables[table_number]["name"]=name
    tables[table_number]["vip_status"]=vip_status
    tables[table_number]["order"]={}

assign_table(2,"Luca",True)
print(tables)

for table_number,info in tables.items():
    print("Table",table_number)

    for key in info:
        print(key+":",info[key])

def assign_order(table_number,**order_items):
    global food, drinks
    food = order_items.get("food")
    drinks = order_items.get("drinks")
    tables[table_number]["order"]["food"]=food
    tables[table_number]["order"]["drinks"]=drinks

assign_order(2,food= "burger, bacon",drinks="water, juice")
print(tables)

























































