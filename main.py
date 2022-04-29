file = open('./goods.txt', 'r', encoding="utf-8")

data = file.read()\

goods_list = data.split('\n')

def get_goods_info(goods_list):
    result = {}
    expensive_goods = set()
    min_price = float('inf')
    min_count = float('inf')
    max_price = 0
    max_count = 0
    goods_count = 0
    price_sum = 0
    a = []
    b = []
    c = []
    d = []
    for good in goods_list:
        item = good.split(':')
        item_price = int(item[1])
        item_count = int(item[2])
        item_zorro = item[0]
        price_sum += item_price
        # print(item[1])
        if item_price <= min_price:
            min_price = item_price
            a.append(item_zorro),
            a.append(item_price)

        elif item_price >= max_price:
            max_price = item_price
            b.append(item_zorro),
            b.append(item_price)
        if item_count < min_count:
            min_count = item_count
            c.append(item_zorro)
            c.append(item_count)
        elif item_count > max_count:
            max_count = item_count
            d.append(item_zorro)
            d.append(item_count)
        goods_count += 1
    a1 = a[4:None]
    b1 = b[10:None]
    c1 = c[-2:None]
    d1 = d[-2:None]

    mean_price = round(price_sum / goods_count, 2)

    result['min_price'] = a1
    result['max_price'] = b1
    result['mean_price'] = mean_price
    result['min_count'] = min_count
    result['min_count1'] = c1
    result['max_count'] = max_count
    result['max_count1'] = d1
    return result

def print_goods_info(goods_list):

    goods_dict = get_goods_info(goods_list)

    print(f'Самый дорогой товар: {goods_dict["max_price"]}',
          f'Самый дешевый товар: {goods_dict["min_price"]}',
          f'Средняя цена товара: {goods_dict["mean_price"]}',
          f'Минимальное количество товара: {goods_dict["min_count"]}, товар: {goods_dict["min_count1"]}',
          f'Максимальное количество товара: {goods_dict["max_count"]}, товар: {goods_dict["max_count1"]}',
          sep='\n'
          )

print_goods_info(goods_list)