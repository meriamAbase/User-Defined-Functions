# Programming with User-defined Functions

### Task Requirements:
Follow these steps:

* Create a Python file called **holiday.py**.

* Your task will be to calculate a user’s total holiday cost, which includes the plane cost, hotel cost, and car-rental cost.

* First, get the following user inputs:

    1. **city_flight**: The city they will be flying to. (You can create some options for them. Remember each city will have different flight costs.)
    2. **num_nights**: The number of nights they will be staying at a hotel
    3. **rental_days**: The number of days for which they will be hiring a car.

* Next, create the following four functions:

    1. **hotel_cost**: This function will take **num_nights** as an argument, and return a total cost for the hotel stay (you can choose the price per night charged at the hotel).
    2. **plane_cost**: This function will take **city_flight** as an argument and return a cost for the flight. (Hint: use if/else if statements in the function to retrieve a price based on the chosen city.)
    3. **car_rental**: This function will take **rental_days** as an argument and return the total cost of the car rental (you can choose the daily rental cost.)
    4. **holiday_cost**: This function will take the three arguments **hotel_cost**, **plane_cost**, **car_rental**. Using these three arguments, you can call all three of the above functions with respective arguments and finally return a total cost for your holiday.

* Print out all the details about the holiday in a readable way.

* Try running your program with different combinations of input to show its compatibility with different options.
