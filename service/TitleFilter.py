from Notes_app.service.Filter import Filter


class TitleFilter(Filter):
    def filter(self, items, specification):
        filter_items = []
        for item in items:
            if specification.is_satisfied(item.get_title()):
                filter_items.append(item)
        return filter_items
