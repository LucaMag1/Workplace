"""tables = {1:{"name":"Luca","vip_status":False},2:{}, 3:{}, 4:{}}

def assign_table(table_number,name, vip_status=False):
    tables[table_number]["name"]=name
    tables[table_number]["vip_status"]=vip_status
    tables[table_number]["order"]=""

def assign_order(table_number,*order_items):
    tables[table_number]["order"]=order_items
    for items in order_items:
        print(items)

assign_table(3, "Max",True)
assign_order(3,"Burger","Chips")

print(tables)"""










































