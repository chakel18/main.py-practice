"""
Food
Ella Chakravarty

Store menu items and their prices as a dictionary

"""
#Display menu items and their prices
menu_dict = {'Hot Dog':1.50,'Slice of Pizza':1.99, 'Whole Pizza':9.95, 'Chicken Bake':3.99, 'Soft Drink':0.69, 'Ice Cream Sundae':2.49}
print('Menu')
print(f'Hot Dog  $ {menu_dict['Hot Dog']:.2f}')
print('Slice of Pizza  $' ,menu_dict ['Slice of Pizza'] )
print('Whole Pizza  $' ,menu_dict ['Whole Pizza'] )
print('Chicken Bake  $' ,menu_dict ['Chicken Bake'] )
print('Soft Drink  $',menu_dict ['Soft Drink'] )
print('Ice Cream Sundae  $' ,menu_dict ['Ice Cream Sundae'])

#Obtain user imput/order
num_hot_dogs = int(input('Please enter the number of Hot Dogs:'))
num_slices = int(input('Please enter the number of Pizza Slices:'))
num_pizzas = int(input('Please enter the number of Whole Pizzas:'))
num_chicken = int(input('Please enter the number of chicken Bakes:'))
num_drinks = int(input('Please enter the number of soft drinks:'))
num_sundaes = int(input('Please enter the number of Ice Cream Sundaes:'))

#Calculate price based on input
total_cost = (num_hot_dogs * menu_dict ['Hot Dog']) + (num_slices * menu_dict ['Slice of Pizza']) + (num_pizzas * menu_dict ['Whole Pizza']) + (num_chicken * menu_dict ['Chicken Bake']) + (num_drinks * menu_dict ['Soft Drink']) + (num_sundaes * menu_dict ['Ice Cream Sundae'])
print('The total cost of the order is $',total_cost)