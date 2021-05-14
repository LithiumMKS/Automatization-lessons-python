def displayinventory(vocabulary):
    print('Inventory: ')
    total = 0
    for k, v in vocabulary.items():
        print(str(v)+"  "+str(k))
        total += int(v)
    print('Total number of intems: '+str(total))


def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item not in inventory.keys():
            inventory.update({item: 1})
        else:
            inventory.update({item: inventory[item] + 1})

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = {'gold coin': 42, 'rope': 1}
'''
for item in dragonLoot:
    if item not in inv.keys():
        inv.update({item:1})
    else:
        inv.update({item:inv[item]+1})
'''

addToInventory(inv, dragonLoot)
displayinventory(inv)
