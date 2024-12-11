import time


class Building:
        """
        Use the vocabulary below and try to create an own class.

        Class: The blueprint for creating objects (in this case, Car).
        Instance: An individual object created from a class.
        Attribute: A characteristic of the instance (like color or make).
        Method: A function defined inside a class that acts on instances (like start_engine).
        """
        def __init__(self, floors, elevator, stairs, windows, sign_on_wall):
            self.floors = floors
            self.elevator = elevator
            self.stairs = stairs
            self.windows = windows
            self.sign_on_wall = sign_on_wall

        def open_entrace_doors(self):
            pass

        def turn_on_lights(self):
            turned_on_timer = time.time()
            turn_off_time = turned_on_timer + 2
            print('lampan tänds')
            while time.time() < turn_off_time:
                lights = 1
            print('lampan släcks')
            lights = 0
            return

dollarstore = Building(2,1, 2, 100, 'Dollar Store')
# dollarstore.turn_on_lights()
print('******************************')
print('*       ' + dollarstore.sign_on_wall + '         *')
print('******************************')


class Elevator:
    """This class handles the operations of the lift"""
    def __init__(self, max_weight, max_people, current_floor: int, floors: int) -> None:
        self.num_buttons = floors
        self.max_weight = max_weight
        self.max_people = max_people
        self.current_floor = current_floor

    def change_floor(self):
        """This is the process of moving the lift cart by pressing it's buttons"""
        print(f'Nu är hissen på plan {self.current_floor}')
        try:
            chosen_floor: int = int(input('Chose floor '))
        except TypeError:
            print(f'{chosen_floor} is not an integer, try again!')

        number_of_changing_floor = abs(chosen_floor - self.current_floor)

        if self.current_floor < chosen_floor:
            self.current_floor = self.current_floor + (chosen_floor - self.current_floor)
        else:
            self.current_floor = self.current_floor + (chosen_floor - self.current_floor)

        time.sleep(number_of_changing_floor*2)

        print(f'Nu är hissen på plan {self.current_floor}')

        go_again = input(f'Vill du åka hiss igen? ')
        if go_again == 1:
            self.change_floor()
        return self.current_floor

hiss1 = Elevator(2000, 14, 0, 4)
hiss1.change_floor()

#dollarstore = Building(2, elevator=Elevator(num_buttons=floors),
#                       stairs=0, windows=45, sign_on_wall='dolalrstore')

#print(dollarstore.sign_on_wall)

