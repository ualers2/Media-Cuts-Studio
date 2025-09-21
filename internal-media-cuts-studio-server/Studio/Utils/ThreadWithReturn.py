import threading

class ThreadWithReturn(threading.Thread):
    def __init__(self, target, args=()):
        super().__init__()
        self.target = target
        self.args = args
        self.resultado = None

    def run(self):
        self.resultado = self.target(*self.args)

    def join(self, *args, **kwargs):
        super().join(*args, **kwargs)
        return self.resultado