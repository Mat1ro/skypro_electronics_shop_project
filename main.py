from src.item import Item

if __name__ == '__main__':
    Item.instantiate_from_csv("src/items.csv")
    print(Item.all)
