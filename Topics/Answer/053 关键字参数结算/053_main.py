"""053 关键字参数结算。"""


def checkout(discount=1.0, **products):
    """把所有商品小计相加，再乘以折扣。"""
    original_total = sum(products.values())
    return round(original_total * discount, 2)


if __name__ == "__main__":
    print(checkout(discount=0.8, book=50, pen=10))
