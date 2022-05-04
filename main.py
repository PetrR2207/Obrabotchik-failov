file = open('./goods.txt', 'r', encoding="utf-8")

data = file.read()\

goods_list = data.split('\n')

def get_goods_info(goods_list):
    result = {}
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
    e = []
    o = []
    f = []
    j = []

    for good in goods_list:
        item = good.split(':')
        item_price = int(item[1])
        item_count = int(item[2])
        price_sum += item_price
        if item_price <= min_price:
            min_price = item_price
            a.append(item_price)
        elif item_price >= max_price:
            max_price = item_price
            b.append(item_price)
        if item_count <= min_count:
            min_count = item_count
            e.append(item_count)
        elif item_count > max_count:
            max_count = item_count
            o.append(item_count)
        goods_count += 1
    mean_price = round(price_sum / goods_count, 2)
    bor = min(a)
    bar = max(b)
    ber = min(e)
    bir = max(o)


    for k in goods_list:
        item1 = k.split(':')
        item_zorro1 = item1[0]
        item_price1 = int(item1[1])
        item_count1 = int(item1[2])
        if item_price1 <= bor:
            bor = item_price1
            c.append(item_zorro1),
            c.append(item_price1)
        elif item_price1 >= bar:
            bar = item_price1
            d.append(item_zorro1),
            d.append(item_price1)
        if item_count1 <= ber:
            ber = item_count1
            f.append(item_zorro1),
            f.append(item_count1)
        elif item_count1 >= bir:
            bir = item_count1
            j.append(item_zorro1),
            j.append(item_count1)



    result['min_price'] = c
    result['max_price'] = d
    result['min_count'] = f
    result['max_count'] = j
    result['mean_price'] = mean_price

    return result

def print_goods_info(goods_list):

    goods_dict = get_goods_info(goods_list)

    print(f'Самый дешевый товар: {goods_dict["min_price"]}',
          f'Самый дорогой товар: {goods_dict["max_price"]}',
          f'Товар с минимальным количеством: {goods_dict["min_count"]}',
          f'Товар с максимальным количеством: {goods_dict["max_count"]}',
          f'Средняя цена товара: {goods_dict["mean_price"]}',
          sep='\n'
          )

print_goods_info(goods_list)
