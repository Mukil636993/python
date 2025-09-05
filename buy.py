money=500
shop_inventory=[
    {"name":"teddy","price":300,"favour":2,'for':'yoimiya','stock':3},
    {'name':'choclate','price':200,'favour':2,'for':'yuki','stock':3}
  ]
def shop():
  choosen_item=None
  global money
  global shop_inventory
  print("money:"+str(money))
  for i in shop_inventory:
    print(f'{i['name']} -${i['price']} > {i['for']}= favour increased by {i['favour']}\n ')

  player_gift_choice=input('Enter the gift name you want to buy:')
  for i in shop_inventory:
    if i['name'].lower()==player_gift_choice.lower():
      choosen_item=i
      break
  if choosen_item:
    if money >= choosen_item['price'] and choosen_item['stock']>0:
      i['stock']-=1
      print(f'\nYou buyed {i['name']} for {i['for']} favour increased by {i['favour']}, remaining {i['name']} {i['stock']}\n')
      money-=i['price']
      print('Your remaining money '+str(money)+'\n')
    else:
      print('you don\'t have enough money or out of stocks\n')
  else:
    print('gift not found')
  while True:
    player_shop_quit=input('If you want to continue shoping press "y"\nIf you want to quit the shop press "n"\n')
    if player_shop_quit not in ('y','n'):
      print('please enter the correct input\n')
      continue
    else:
      break
  if player_shop_quit=='y':
    shop()
  elif player_shop_quit=='n':
    print('you quit the shop')
shop()