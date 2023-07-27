from Notes_app.service.Filter import Filter


class ContentFilter(Filter):
    def filter(self, items, specification):
        filter_items = []
        for item in items:
            if specification.is_satisfied(item.get_content()):
                filter_items.append(item)
        return filter_items
