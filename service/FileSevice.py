import json
import os


class FileService:
    @classmethod
    def read_file(cls, filename):
        if os.path.exists('data.json') and os.stat("data.json").st_size != 0:
            with open(filename, 'r', encoding='utf-8') as file:
                return json.loads(file.read())
        else:
            return None

    @classmethod
    def write_to_file(cls, data, filename):
        data = json.dumps(data)
        data = json.loads(str(data))
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
