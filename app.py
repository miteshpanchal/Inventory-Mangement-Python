class InventorySystem:
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity):
        if item not in self.items:
            self.items[item] = 0
        self.items[item] += quantity

    def remove_item(self, item, quantity):
        if item not in self.items:
            raise ValueError("Item does not exist")
        if self.items[item] < quantity:
            raise ValueError("Insufficient quantity")
        self.items[item] -= quantity

    def get_item_quantity(self, item):
        if item not in self.items:
            return 0
        else:
            return self.items[item]

def main():
    inventory_system = InventorySystem()

    print("Enter a command:")
    command = input()

    while command != "exit":
        if command == "add":
            item = input("Enter the item to add: ")
            quantity = int(input("Enter the quantity to add: "))
            inventory_system.add_item(item, quantity)
        elif command == "remove":
            item = input("Enter the item to remove: ")
            quantity = int(input("Enter the quantity to remove: "))
            inventory_system.remove_item(item, quantity)
        elif command == "get":
            item = input("Enter the item to get the quantity of: ")
            quantity = inventory_system.get_item_quantity(item)
            print("The quantity of {} is {}.".format(item, quantity))
        else:
            print("Invalid command.")

        print("Enter a command:")
        command = input()

if __name__ == "__main__":
    main()
