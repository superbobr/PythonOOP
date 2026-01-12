class PetrolEngine:
    @staticmethod
    def start():
        return "Бензиновый двигатель запущен"


class ElectricEngine:
    @staticmethod
    def start():
        return "Электрический двигатель активирован"


class Car:
    def __init__(self, model, engine):
        self.model = model
        self.engine = engine

    def start_car(self):
        return self.engine.start()