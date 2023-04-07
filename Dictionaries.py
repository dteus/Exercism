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
        print(caixa)
        if values in inventory:
            inventory[values] += 1
        else:
            inventory.update([(values,(caixa[values]+ inventory[values]))])
    return inventory

add_items({"wood": 4, "iron": 2}, ["iron", "iron"])