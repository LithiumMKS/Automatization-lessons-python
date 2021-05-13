dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
dict = {}
for item in dragonLoot:
    if item not in dict.keys():
        dict = dict.update({item, 1})
    else:
        dict = dict.update({item, int(dict.value(item)+1)})