# For this task, I am going to create a holiday calculator, that 
# calculates the users total holiday costs, which includes
# plane cost, hotel cost, and car rental cost.

# =============================================================================
# First, create the following 4 def functions:
def hotel_cost(num_nights: int) -> int:
    """
    The function calculates the total cost of a hotel stay based on the number
    of nights.
    
    Args:
        num_nights: The number of nights the guest will be staying at the hotel.
    Returns:
        int: The total cost of staying at a hotel for a given number of nights.
    """
    return 65 * num_nights
    

def plane_cost() -> int:
    """
    The function 'plane_cost()' prompts the user to choose a destination.
    Returns: 
        int: The cost of the plane ticket for the chosen destination.
    """
    while True:
        city_flight = (input("\033[32;1mChoose from options 1 to 5: \033[0m"))
        if city_flight == "1":
            return 175
            
        elif city_flight == "2":
            return 150
        
        elif city_flight == "3":
            return 200
        
        elif city_flight == "4":
            return 250
        
        elif city_flight == "5":
            return 275
        
        else:
            print("Please choose a valid destination")
        

def car_rental(rental_days: int) -> int:
    """
    This calculates the total cost of renting a car based on the number of
    rental days.
    
    Args:
        rental_days: The number of days the car is rented for.
    Returns:
        int: The total cost of renting a car for the specified number of days.
    """
    return 25 * rental_days


def holiday_cost(hotel_cost: int, plane_cost: int, car_rental: int) -> int:
    """
    The function calculates the total cost of a holiday by adding the costs of
    the hotel (if any), plane, and car rental (if any).
    
    Args:
        hotel_cost: The cost of the hotel for the holiday.
        plane_cost: The cost of the plane ticket for the holiday.
        car_rental: The cost of renting a car for the holiday.
    Returns:
        int: The total cost of the holiday, which is the sum of the hotel cost,
        plane cost, and car rental cost.
    """
    total_cost = hotel_cost + plane_cost + car_rental
    return total_cost


#  ================================ Main code ================================
print("\033[42;30;1m======================= Hello, welcome to Holiday Tracker! =======================\033[0m")


while True:
    # Displays destination options.
    print("\n\033[32;1mLet's plan your holiday and work out the total cost.\033[0m\n")
    print("\033[42;30;1m======================= Destination =======================\033[0m")
    print("\n\033[32;1mWhere would you like to travel to?\033[0m\n")
    print("\033[31;1m1. London \033[0m")
    print("\033[33;1m2. Paris \033[0m") 
    print("\033[32;1m3. Hong Kong \033[0m")
    print("\033[36;1m4. New York \033[0m")
    print("\033[35;1m5. South Africa \033[0m\n")

    # The 'plane_cost()' function prompts the user to choose a destination and
    # returns the cost of a plane ticket based on the chosen destination.
    ticket_cost = plane_cost()


    # This code block uses a 'try-except' statement to handle any 'ValueError'
    # that may occur when the user enters the number of nights and car hire 
    # days.
    while True:
        try: 
            print("\n\033[42;30;1m======================= Total Nights =======================\033[0m")
            nights = int(input("\n\033[32;1mHow many nights will you be staying? Enter 0 for none: \033[0m"))
            print("\n\033[42;30;1m======================= Car Hire =======================\033[0m")
            car = int(input("\n\033[32;1mHow many days will you be hiring a car for? Enter 0 for none: \033[0m"))
            break
        except ValueError:
            print("Please enter a valid number: ")
        

    print("\n\033[42;30;1m======================= Cost Breakdown: =======================\033[0m\n")
    # Calculates the total hotel cost based on the number of nights.
    # If no hotel is needed, prints "No hotel needed".
    hotel_total = 0 
    while True:
        if nights == 0:
            print("\033[32;1mNo hotel needed.\033[0m")
            break
        else:
            hotel_total = hotel_cost(nights)
            print(f"\033[32;1mHotel cost:\033[0m £{hotel_total}.")
            break

    # Calulates the total car rental cost.
    # If no car is needed, prints "No car needed".
    car_total = 0 
    while True:
        if car == 0:
            print("\033[32;1mNo car needed.\033[0m")
            break
        else:
            car_total = car_rental(car)
            print(f"\033[32;1mCar rental cost:\033[0m £{car_total}.")
            break

    # Prints the ticket cost.
    print(f"\033[32;1mTicket cost:\033[0m £{ticket_cost}.")


    # Prints the final total cost for the holiday.
    final_total = holiday_cost(hotel_total, ticket_cost, car_total)
    print("\n\033[42;30;1m======================= Total Cost: =======================\033[0m\n")
    print(f"\033[32;1mThe total cost is:\033[0m £{final_total}.\n")

    
    # Prompts the user to choose if they wish to calculate another trip or
    # simply end the program.
    if input("\033[32;1mPress enter to calculate another trip or type anything to quit:\033[0m "):
        break


# Finally, a little goodbye message.
print("\033[42;30;1m======================= Thank you for using our services! Enjoy your trip! =======================\033[0m")

