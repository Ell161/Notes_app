from service.Filter import Filter


class TitleFilter(Filter):

    @classmethod
    def filter(cls, collection, specification):
        """
        A method for filtering Notes by title.

        :param collection: dictionary object where the key is the record identifier
        and the value is an instance of the Note class
        :param specification: instance of the note Search Specification class
        :return: filter dictionary object where the key is the record identifier
        and the value is an instance of the Note class
        """
        filter_items = {}
        for key, value in collection.items():
            if specification.is_satisfied(value.get_title()):
                filter_items[key] = value
        return filter_items
