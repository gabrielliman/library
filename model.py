class Book:

    REGULAR: int = 0
    NEW_RELEASE: int = 1
    CHILDREN: int = 2

    def __init__(self, title: str, price_code: int):
        self.title = title
        self.price_code = price_code

    def get_charge(self, days_rented: int) -> float:
        amount = 0
        if self.price_code == Book.REGULAR:
            amount += 2
            if days_rented > 2:
                amount += (days_rented - 2) * 1.5
        elif self.price_code == Book.NEW_RELEASE:
            amount += days_rented * 3
        elif self.price_code == Book.CHILDREN:
            amount += 1.5
            if days_rented > 3:
                amount += (days_rented - 3) * 1.5
        return amount
    def get_frequent_renter_points(self, days_rented: int, frequent_renter_points: int) -> int:
        frequent_renter_points += 1
        if self.price_code == Book.NEW_RELEASE and days_rented > 1:
            frequent_renter_points += 1
        return frequent_renter_points

class Rental:
    def __init__(self, book: Book, days_rented: int):
        self.book = book
        self.days_rented = days_rented
    
    def get_charge(self) -> float:
        return self.book.get_charge(self.days_rented)
    
    def get_frequent_renter_points(self, frequent_renter_points) -> int:
        return self.book.get_frequent_renter_points(self.days_rented, frequent_renter_points)


class Client:

    def __init__(self, name: str):
        self.name = name
        self.rentals = []

    def add_rental(self, rental: Rental):
        self.rentals.append(rental)

    def statement(self) -> str:

        total_amount = 0
        frequent_renter_points = 0
        result = f"Rental summary for {self.name}\n"
        
        for rental in self.rentals:
            amount = rental.get_charge()
            
            frequent_renter_points = rental.get_frequent_renter_points(frequent_renter_points)
            
            # add frequent renter points
            # frequent_renter_points += 1
            # if rental.book.price_code == Book.NEW_RELEASE and rental.days_rented > 1:
            #     frequent_renter_points += 1

            # show each rental result
            result += f"- {rental.book.title}: {amount}\n"
            total_amount += amount
        
        # show total result
        result += f"Total: {total_amount}\n"
        result += f"Points: {frequent_renter_points}"
        return result