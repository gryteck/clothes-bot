class Rate:
    def __init__(self, start_rate):
        self.rate = start_rate

    def upd(self, new_rate):
        self.rate = new_rate
        return self.rate

    def get(self):
        return self.rate


rate = Rate(12.0)
