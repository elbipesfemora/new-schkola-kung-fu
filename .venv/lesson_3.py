products = input('Введите список продуктов в формате «товар:количество» через запятую:')

separation_of_products = products.split(',')
product_list_generator = [prod.split(':') for prod in separation_of_products]
dictionary_from_the_list = dict(product_list_generator)

print(dictionary_from_the_list)