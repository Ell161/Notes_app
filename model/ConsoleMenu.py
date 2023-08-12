from colorama import init, Fore, Style


class ConsoleMenu:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.cursor = 0

    def add_item(self, item):
        self.items.append(item)

    def get_item(self, index):
        return self.items[index]

    def get_item_by_name(self, name):
        for item in self.items:
            if name.lower() == item.get_name().lower():
                return item

    def extend_items(self, items):
        self.items.extend(items)

    def clear_items(self):
        self.items.clear()

    def len_items(self):
        return len(self.items)

    def draw(self):
        self.draw_title(self.name)
        if len(self.items) != 0:
            for i_item, item in enumerate(self.items):
                item.draw(i_item + 1)
        else:
            print('---Information not found---')

    @classmethod
    def draw_title(cls, title):
        init()
        print(Fore.BLUE + Style.BRIGHT + '\n' + '-' * (len(title) + 12))
        print(f'|  {Fore.CYAN}---{title}---  {Fore.BLUE}|')
        print('-' * (len(title) + 12) + Fore.RESET)
