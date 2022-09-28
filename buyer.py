user = [1, 1, 2, 5, 5, 5]
shop = []
products = {'кофе': 3, 'колбаса': 5, 'хлеб': 4, 'кефир': 5, 'квас': 2, 'салфетки': 1, 'протеин': 5}
buy_products = []
summ = 0

print("-" * 31)
print("Денег у покупателя:", *user, "руб.")
print("Денег в кассе:", *shop, "руб.")
print("Продукты:", *products.keys())
print("-" * 31)

while True:
    def result():
        print("-" * 31)
        print("Денег у покупателя:", *user, "руб.")
        print("В кассе:", *shop, "руб.")
        print("Вы купили:", *buy_products)
        print("Продукты:", *products)
        print("-" * 31)


    product = input("Выбери товар из тех, что есть в магазине: ")
    if product == "стоп":
        result()
        break
    elif product in products:
        print(f"{product} есть, с вас {products[product]} руб.")
        if products[product] in user:
            user.remove(products[product])
            shop.append(products[product])
            del products[product]
            buy_products.append(product)

            result()
        elif max(user) < products[product]:
            print("У вас не хватает денег на эту покупку.")

        else:
            for us in user:

                if us <= products[product]:
                    summ += us
                    us = summ

            for us in user:
                if us > products[product]:
                    change = us - products[product]
                    if shop != change:
                        print("Нет монет на сдачу...")
                        break
                    else:
                        shop.remove(change)
                        shop.append(products[product])
                        user.remove(us)
                        user.append(change)
                        del products[product]
                        buy_products.append(product)
                        result()
                        break



    else:
        print('Такого продукта нет')

print("Ждём вас снова!")