#
#task1
word_dict = {}
word = input('Type a random sentence')

for i in word.split():
    if i not in word_dict.keys():
         word_dict[i] = 0
    word_dict[i] += 1
print(word_dict)


#task2
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

item = 0
price = 0
stockprice = 0
totalprice = 0
for element in stock:
    itemqty = stock[element]
    price = prices[element]
    totalprice = price * itemqty
    stockprice = stockprice + totalprice
    print(element,":",itemqty, '*', price, '=', totalprice.__int__())
print((f'Total price is {stockprice.__int__()}'))


#task3

i = list(range(11))
j = [num2 ** 2 for num2 in i]
ij_tuple = (i,j,)
print(f'{ij_tuple[0]}\n{ij_tuple[1]}')

# task4


day_num = {
    'mon': 1,
    'tue': 2,
    'wed': 3,
    'thu': 4,
    'fri': 5,
    'sat': 6,
    'sun': 7,
}
num_day = {}
for day in day_num.keys():
    num_day[day_num[day]] = day
print(num_day)
