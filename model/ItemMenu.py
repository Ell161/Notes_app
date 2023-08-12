class ItemMenu:
    def __init__(self, name, function=None, data=None):
        self.name = name
        self.function = function
        self.data = data

    def get_name(self):
        return self.name

    def get_function(self):
        return self.function()

    def get_function_with_data(self, data):
        return self.function(data)

    def get_data(self):
        return self.data

    def set_function(self, function):
        self.function = function

    def draw(self, point):
        if self.data is not None:
            if self.data.get('date_of_update') is not None:
                print(f'[{point}]  {self.name:50} {self.data.get("date_of_update")}')
            elif self.data.get('date_of_create') is not None:
                print(f'[{point}]  {self.name:50} {self.data.get("date_of_create")}')
        else:
            print(f'[{point}]  {self.name}')
