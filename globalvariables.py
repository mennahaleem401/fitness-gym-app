class AppController:
    def __init__(self):
        self.shared_data = {}

    def set_data(self, key, value):
        self.shared_data[key] = value

    def get_data(self, key):
        return self.shared_data.get(key)
