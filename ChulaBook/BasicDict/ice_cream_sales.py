n = int(input())

order_ice = {}
for _ in range(n):
    order_list = input().split()
    order_ice[order_list[0]] = int(order_list[1])

# print(order_ice)
m = int(input())

total_ice_sales = 0
name_ice_top = {}
for _ in range(m):
    order_amount = input().split()
    if order_amount[0] in order_ice:
        ice_name = order_amount[0]
        ice_amount = int(order_amount[1])
        ice_sale = ice_amount * order_ice[ice_name]
        total_ice_sales += ice_sale
        if ice_name not in name_ice_top:
            name_ice_top[ice_name] = ice_sale
        else:
            name_ice_top[ice_name] += ice_sale

name_ice_top = sorted(name_ice_top.items(), key=lambda item: item[1], reverse=True)
name_top = [name_ice_top[i][0] for i in range(1, len(name_ice_top)) if name_ice_top[i][1] == name_ice_top[0][1]]
name_top.insert(0, name_ice_top[0][0])
name_top = sorted(name_top)
if total_ice_sales != 0:
    print(f"Total ice cream sales: {total_ice_sales}")
    print(f"Top sales: {', '.join(name_top)}")
else:
    print("No ice cream sales")
    
    