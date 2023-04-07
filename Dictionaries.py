def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    inventory = {}
    for values in items:
        auxiliar = items.count(values)
        if values not in inventory:
            inventory.update([(values, auxiliar)])
    return inventory
        
def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    caixa={}
    for values in items:
        auxiliar = items.count(values)
        if values not in caixa:
            caixa.update([(values, auxiliar)])
    for values in caixa:
        if values in inventory:
            inventory[values] += caixa[values]
        else:
            inventory.update([(values,(caixa[values]))])
    return inventory

def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    for values in items:
        if inventory[values]>0: inventory[values] -= 1
    return inventory

def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    if item in inventory: 
        inventory.pop(item)
        return inventory
    return inventory

def list_inventory(inventory):
    """Create a list containing all (item_name, item_count) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    retorno =[]
    for item in inventory:
        if inventory[item]>0:
            retorno.append((item, inventory[item]))
    return retorno
