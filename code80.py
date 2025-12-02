from prettytable import PrettyTable
import matplotlib.pyplot as diagram

receipt = PrettyTable()
receipt.field_names = ['№','Продукт','Цена','Количество','Стоимость']

products = []
pay = []

for i in range(3):
  product = input('Укажите название продукта: ')
  price = int(input('Введите цену продукта: '))
  quantity = int(input('Укажите количество продукта: '))
  cost = price * quantity
  receipt.add_row([i+1, product, f'{price} руб.', f'{quantity} шт.', f'{cost} руб.'])
  products.append(product)
  pay.append(cost)

print(receipt)

diagram.bar(products, pay)
diagram.title('Стоимость покупок')
diagram.xlabel('Продукты')
diagram.ylabel('Стоимость (руб)')

diagram.show()

