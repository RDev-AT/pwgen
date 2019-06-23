# imports
import json


class Export(object):
    def export_text(self, data: list, seperator: str= ";"):
        return seperator.join(data)

    def export_json(self, data: list):
        return json.dumps(data)
