class Cab:
    def __init__(self,cab_id,driver_name,car_model,is_available):
        self.cab_id = cab_id
        self.driver_name = driver_name
        self.car_model = car_model
        self.is_available = is_available

    def start_trip(self):
        self.is_available = False

    def end_trip(self):
        self.is_available = True

class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name

    def book_cab(self,cab):
        if cab.is_available:
            cab.start_trip()
            print(f"Customer {self.name} booked cab {cab.cab_id}.")
        else:
            print(f"Cab {cab.cab_id} is not available.")
    
    def end_trip(self, cab):
        cab.end_trip()
        print(f"Customer {self.name} ended trip with cab {cab.cab_id}.")


class CabBookingSystem:
    def __init__(self):
        self.cabs = []
        self.customers = []

    def add_cab(self,cab):
        self.cabs.append(cab)
        print(f"Cab {cab.cab_id} ({cab.car_model}) by {cab.driver_name} added")

    def register_customer(self,customer):
        self.customers.append(customer)
        print(f"Customer {customer.customer_id} ({customer.name}) registered")

    def show_available_cabs(self):
        print("Available cabs:")
        for cab in self.cabs:
            if cab.is_available:
                print(f"- {cab.cab_id}: {cab.car_model} by {cab.driver_name}")

    def find_cab_by_id(self,cab_id):
        for cab in self.cabs:
            if cab.cab_id == cab_id:
                return cab
        return None
    
    def find_customer_by_id(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        return None

obj = CabBookingSystem()

cab1 = Cab("C001", "Sai", "BMW", True)
cab2 = Cab("C002", "Pranith", "Porshe", True)
obj.add_cab(cab1)
obj.add_cab(cab2)

cust1 = Customer("U001", "Alice")
obj.register_customer(cust1)

cust1.book_cab(cab1)

obj.show_available_cabs()

cust1.end_trip(cab1)

obj.show_available_cabs()