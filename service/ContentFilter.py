from service.Filter import Filter


class ContentFilter(Filter):
    @classmethod
    def filter(cls, collection, specification):
        filter_items = {}
        for key, value in collection.items():
            if specification.is_satisfied(value.get_content()):
                filter_items[key] = value
        return filter_items
