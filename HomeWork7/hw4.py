class KeyValueStorage():
    keys_dict = {}

    def __init__(self, path):
        with open(path) as file:
            while True:
                line = file.readline()
                if line == '':
                    break
                key_value = line.split('\n')[0].split('=')
                if len(key_value) < 2 or key_value[0] == '':
                    raise ValueError

                if not hasattr(self, key_value[0]):
                    setattr(self, key_value[0], key_value[1])
                    self.keys_dict[key_value[0]] = key_value[1]

    def __getitem__(self, key):
        return self.keys_dict[key]
