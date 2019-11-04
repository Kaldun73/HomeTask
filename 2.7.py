#7. Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.
#Пример:
#{
#“название”: [“компьютер”, “принтер”, “сканер”],
#“цена”: [20000, 6000, 2000],
#“количество”: [5, 2, 7],
#“ед”: [“шт.”]
#}

goods_list = []
for i in range(0, int(input("Input amount of different goods"))):
    goods = (i + 1, {'name': input("Input name"), 'price': input("Input price"), 'amount': input("Input amount")})
    goods_list.append(goods)
    i =+ 1
print(goods_list)

#goods_list = [
#    (1, {'name': 'PC', 'price': '1000', 'amount': '5'}),
#    (2, {'name': 'laptop', 'price': '600', 'amount': '10'})
#]

name_list = []
price_list = []
amount_list = []

for i in range(0 , len(goods_list)):
    goods_dict = {}
    goods_dict.update(goods_list[i][1])
    name_list.append(goods_dict['name'])
    price_list.append(goods_dict['price'])
    amount_list.append(goods_dict['amount'])

goods = {
    "name": name_list,
    "price": price_list,
    "amount": amount_list,
    "variety": len(goods_list)
}

print(goods)


