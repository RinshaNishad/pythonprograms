from abc import ABC,abstractmethod
class Ide(ABC):
    @abstractmethod
    def debug(self):
        pass

class Pycharm(Ide):
    def debug(self):
        print("pycharm debug method")

class Eclipse(Ide):
    def debug(self):
        print("eclipse debug method")

pyc=Pycharm()
pyc.debug()
# elc=Eclipse()
# elc.debug()

