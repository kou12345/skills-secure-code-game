'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple
from decimal import Decimal

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

def validorder(order: Order):
    net = Decimal('0')
    total_products_amount = Decimal('0')
    total_payments_amount = Decimal('0')
    payment_upper_limit = Decimal('10000')  # 上限値を$10,000とする

    for item in order.items:
        item_amount = Decimal(str(item.amount))
        item_quantity = Decimal(str(item.quantity))
        if item.type == 'payment':
            total_payments_amount += item_amount
        elif item.type == 'product':
            total_products_amount += item_amount * item_quantity
        else:
            return "Invalid item type: %s" % item.type

    # 商品の合計金額と支払いの合計金額の差を計算
    net = total_payments_amount - total_products_amount
    print(f"total_payments_amount: {total_payments_amount}")
    print(f"total_products_amount: {total_products_amount}")

    # 商品の合計金額が上限を超えているか確認
    if total_products_amount > payment_upper_limit:
        return "Total amount payable for an order exceeded"

    if net != 0:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net)
    else:
        return "Order ID: %s - Full payment received!" % order.id