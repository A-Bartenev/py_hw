from base import Vehicle
from car import Car
from engine import Engine
from plane import Plan
from exceptions import *

if __name__=='__main__':
    test_vehicle=Vehicle()
    print(test_vehicle.fuel,test_vehicle.fuel_consumption,test_vehicle.weight)
    # Проверяем работу Vehicle
    test_vehicle.start()
    test_vehicle.fuel=100
    # test_vehicle.start()
    # test_vehicle.fuel = 50
    test_vehicle.move(15)
    print(test_vehicle.fuel,test_vehicle.fuel_consumption,test_vehicle.weight)
    # Проверяем работу Engine
    test_engine=Engine(34,16)
    # Проверяем работу Car
    test_car=Car()
    test_car.set_engine(test_engine)
    print(test_car.engin)
    # Проверяем работу Plan
    test_plan=Plan(123)
    print(test_plan.max_cargo)
    test_plan.load_cargo(100)
    print(test_plan.cargo)
    print(test_plan.remove_all_cargo())
    print(test_plan.cargo)