class GenHelper(object):
    config = None

    def __init__(self, config):
        self.config = config

    def contains_lookalikes(self, text: str):
        for e in self.config.lookalikes_charlist:
            if text.find(e) != -1:
                return True
        return False
