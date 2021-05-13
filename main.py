inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def displayinventory(vocabulary):
    print('Inventory: ')
    total = 0
    for k, v in vocabulary.items():
        print(str(v)+"  "+str(k))
        total += int(v)
    print('Total number of intems: '+str(total))


displayinventory(inventory)
