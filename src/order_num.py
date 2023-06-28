class OrderNum:
    def __init__(self, start_state):
        self.state = start_state

    def __call__(self):
        self.state += 1

    def upd(self, new):
        self.state = new
        return self.state

    def get(self):
        self.state += 1
        return self.state


order_num = OrderNum(1365)
