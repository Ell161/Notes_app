from service.Filter import Filter


class DateFilter(Filter):

    @classmethod
    def filter(cls, collection, specification):
        """
        A method for filtering Notes by date.

        :param collection: dictionary object where the key is the record identifier
        and the value is an instance of the Note class
        :param specification: instance of the note Search Specification class
        :return: filter dictionary object where the key is the record identifier
        and the value is an instance of the Note class
        """
        filter_items = {}
        for key, value in collection.items():
            if value.get_date_of_create() is not None:
                if specification.is_satisfied(value.get_date_of_create()):
                    filter_items[key] = value
            elif value.get_date_of_update() is not None:
                if specification.is_satisfied(value.get_date_of_update()):
                    filter_items[key] = value
        return filter_items
