from base import Vehicle
from engine import Engine
class Car(Vehicle):
    engin=Engine()
    def set_engine(self,engine_options):
        self.engin=engine_options

if __name__=='__main__':
    pass