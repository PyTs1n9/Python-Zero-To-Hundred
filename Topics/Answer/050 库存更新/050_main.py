"""050 库存更新。"""


def update_stock(stock, operations):
    """按顺序更新库存，拒绝会让库存为负的操作。"""
    final_stock = stock.copy()
    rejected = []
    for index, (product, change) in enumerate(operations):
        old_amount = final_stock.get(product, 0)
        if old_amount + change < 0:
            rejected.append(index)
        else:
            final_stock[product] = old_amount + change
    return final_stock, rejected


if __name__ == "__main__":
    operations = [("pen", -2), ("book", 3), ("pen", -4)]
    print(update_stock({"pen": 5}, operations))
