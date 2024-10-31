from exceptions import *

from abc import ABC


class Vehicle(ABC):
    started=False

    def __init__(self,weight=10, fuel=15, fuel_consumption=34):
        self.weight=weight
        self.fuel=fuel
        self.fuel_consumption=fuel_consumption
    def start (vehicle_status):
        if vehicle_status.started==False and vehicle_status.fuel!=0:
            vehicle_status.started=True
        else:
            raise LowFuelError("нет топлива в баке")
    def move (vehicle_status, distance):
        if vehicle_status.fuel/vehicle_status.fuel_consumption*100>distance:
            vehicle_status.fuel=vehicle_status.fuel-distance/vehicle_status.fuel_consumption
        else:
            raise NotEnoughFuel("не хватит топлива")

if __name__=='__main__':
    pass



