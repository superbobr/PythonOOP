from abc import ABC, abstractmethod


class Plugin(ABC):
    @abstractmethod
    def execute(self, data):
        pass


class UpperCasePlugin(Plugin):
    def execute(self, data):
        return data.upper()


class LowerCasePlugin(Plugin):
    def execute(self, data):
        return data.lower()



def run_plugins(plugins, data):
    result = []
    for plugin in plugins:
        result.append(plugin.execute(data))
    return result