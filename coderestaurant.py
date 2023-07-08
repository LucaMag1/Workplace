tables = {1:{"name":"Luca","vip_status":True,"order":"juice, pancake"},2:{},3:{}}

def assign_table(table_number,name,vip_status=False,*order_items):
    tables[table_number]["name"] = name
    tables[table_number]["vip_status"] = vip_status
    tables[table_number]["order"] = ""

print(tables)
assign_table(2,"Leclerc",False)
print(tables)

def assign_order(table_number,*order_items):
    tables[table_number]["order"] = order_items
    for item in order_items:
        return(item)

assign_order(2,"meat","fries","pasta")
print(tables)