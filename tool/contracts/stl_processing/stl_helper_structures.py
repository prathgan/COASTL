class SwitchDict(dict):
    def __getitem__(self, key):
        return dict.get(self, key)
