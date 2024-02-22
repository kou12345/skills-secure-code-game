import code as c

num_items = 12
# 商品は12個
items = [c.Item(type='product', description='tv', amount=99999, quantity=num_items)]
for i in range(num_items):
    # 支払いは12個
    items.append(c.Item(type='payment', description='invoice_' + str(i), amount=99999, quantity=1))
print(f"len(items): {len(items)}") # 13

# 商品の前に支払いを置く
items = items[1:] + [items[0]]
order_1 = c.Order(id='1', items=items)

print(c.validorder(order_1))