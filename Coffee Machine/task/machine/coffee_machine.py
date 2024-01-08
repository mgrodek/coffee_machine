class ChoosingActionState:
    name = "choosing_action"

    def __init__(self, coffee_machine):
        self.coffee_machine = coffee_machine

    def prompt(self):
        print()
        print("Write action (buy, fill, take, remaining, exit):")

    def interpret_input(self, action):
        self.coffee_machine.choose_action(action)


class ChoosingCoffeeState:
    name = "choosing_coffee"

    def __init__(self, coffee_machine):
        self.coffee_machine = coffee_machine

    def prompt(self):
        print()
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")

    def interpret_input(self, coffee_request):
        self.coffee_machine.buy(coffee_request)


class FillingWaterState:
    name = "filling_water"

    def __init__(self, coffee_machine):
        self.coffee_machine = coffee_machine

    def prompt(self):
        print()
        print("Write how many ml of water do you want to add:")

    def interpret_input(self, water):
        self.coffee_machine.fill_water(water)


class FillingMilkState:
    name = "filling_milk"

    def __init__(self, coffee_machine):
        self.coffee_machine = coffee_machine

    def prompt(self):
        print("Write how many ml of milk do you want to add:")

    def interpret_input(self, milk):
        self.coffee_machine.fill_milk(milk)


class FillingBeansState:
    name = "filling_beans"

    def __init__(self, coffee_machine):
        self.coffee_machine = coffee_machine

    def prompt(self):
        print("Write how many grams of coffee beans do you want to add:")

    def interpret_input(self, beans):
        self.coffee_machine.fill_beans(beans)


class FillingCupsState:
    name = "filling_cups"

    def __init__(self, coffee_machine):
        self.coffee_machine = coffee_machine

    def prompt(self):
        print("Write how many disposable cups of coffee do you want to add:")

    def interpret_input(self, cups):
        self.coffee_machine.fill_cups(cups)


class CoffeeMachine:
    water_total = 400
    milk_total = 540
    beans_total = 120
    cups_total = 9
    money_total = 550

    def __init__(self):
        choose_action_state = ChoosingActionState(self)
        choose_coffee_state = ChoosingCoffeeState(self)
        filling_water_state = FillingWaterState(self)
        filling_milk_state = FillingMilkState(self)
        filling_beans_state = FillingBeansState(self)
        filling_cups_state = FillingCupsState(self)
        self.current_state = choose_action_state
        self.available_states = {
            i.name: i for i in [choose_action_state, choose_coffee_state, filling_water_state, filling_milk_state,
                                filling_beans_state, filling_cups_state]
        }

    def start(self):
        user_input = self.get_input()
        while user_input != "exit":
            self.current_state.interpret_input(user_input)
            user_input = self.get_input()

    def get_input(self):
        self.current_state.prompt()
        return input()

    def choose_action(self, action):
        if action == "buy":
            self.current_state = self.available_states["choosing_coffee"]
        elif action == "fill":
            self.current_state = self.available_states["filling_water"]
        elif action == "take":
            self.take()
        elif action == "remaining":
            self.remaining()

    def buy(self, coffee_request):
        if coffee_request == "1":
            self.buy_coffee(250, 0, 16, 1, 4)
        elif coffee_request == "2":
            self.buy_coffee(350, 75, 20, 1, 7)
        elif coffee_request == "3":
            self.buy_coffee(200, 100, 12, 1, 6)
        self.current_state = self.available_states["choosing_action"]

    def buy_coffee(self, water, milk, beans, cups, money):
        if self.water_total - water < 0:
            print("Sorry, not enough water!")
            return
        elif self.milk_total - milk < 0:
            print("Sorry, not enough milk!")
            return
        elif self.beans_total - beans < 0:
            print("Sorry, not enough beans!")
            return
        elif self.cups_total - cups < 0:
            print("Sorry, not enough cups!")
            return
        elif self.money_total - money < 0:
            print("Sorry, not enough money!")
            return
        else:
            print("I have enough resources, making you a coffee!")
            self.water_total -= water
            self.milk_total -= milk
            self.beans_total -= beans
            self.cups_total -= cups
            self.money_total += money

    def fill_water(self, water):
        self.water_total += int(water)
        self.current_state = self.available_states["filling_milk"]

    def fill_milk(self, milk):
        self.milk_total += int(milk)
        self.current_state = self.available_states["filling_beans"]

    def fill_beans(self, beans):
        self.beans_total += int(beans)
        self.current_state = self.available_states["filling_cups"]

    def fill_cups(self, cups):
        self.cups_total += int(cups)
        self.current_state = self.available_states["choosing_action"]

    def take(self):
        print()
        print(f"I gave you ${self.money_total}")
        self.money_total = 0

    def remaining(self):
        print()
        print("The coffee machine has:")
        print(self.water_total, "of water")
        print(self.milk_total, "of milk")
        print(self.beans_total, "of coffee beans")
        print(self.cups_total, "of disposable cups")
        print(self.money_total, "of money")


CoffeeMachine().start()
