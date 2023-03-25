import json

class FileExecution:

    def __init__(self):
        pass

    def data_searchup(self, related_id, datatype):
        with open(datatype, "r") as file:
            data = json.load(file)
        return data[related_id]["name"]

    def id_check(self, related_id, data_type):
        with open(data_type, "r") as file:
            data = json.load(file)
        if related_id in data:
            return True
        else:
            return False

    def update_file(self, data_pattern, data_type):

        try:
            with open(data_type, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open(data_type, "w") as file:
                json.dump(data_pattern, file, indent=4)
        else:
            data.update(data_pattern)
            with open(data_type, "w") as file:
                json.dump(data, file, indent=4)