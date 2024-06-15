#This class has been called restaurant data as it holds the variables for the
#list stored in the RestaurantManager class. The class name was chosen as it
#clearly explains what it does
class RestaurantData:
    #The restaurant variable was created to store the name of the restaurant
    #the user is creating. It clearly defines the information that will be held in it
    restaurant = None
    #As the above variable, suburb_location stored the name of the suburb
    suburb_location = None
    #As above, the food_rating stores the rating of food quality.
    food_rating = 0
    #As above, the service_rating stores the value of service quality.
    service_rating = 0
    #As above, the cost_rating stores the value of value for money.    
    cost_rating = 0
    #As above, the overall_rating stores the value of overall rating.    
    overall_rating = 0

#The RestaurantManager class holds the list where all user inputs will be stored
#It also holds the backend features of the program manager and is instrumental
#in the program running.
class RestaurantManager:
    #This list holds all values imported from the CSV as well as user inputed
    #data that is manually saved by the user.
    restaurant_rating=[]

    #This method has been created to load and read the csv file storing
    #all data from this program. Its name clearly defines what it does.
    def load_csv(self,file_name):
            with open (file_name+".csv","r") as data_file:
                for line in data_file:
                    #This variable has been created to store all data inputed
                    #directly from the csv. It has been called fields as it
                    #clearly defines the imported fields from the CSV.
                    fields = line.strip().split(",")
                    #restaurant_name has been created to hold the value imported
                    #from the csv's first column which is restaurants
                    restaurant_name = fields[0]
                    #suburb_data has been created to hold the value imported
                    #from the csv's second column which is the suburb data
                    suburb_data = fields[1]
                    #food_data has been created to hold the value imported
                    #from the csv's third column which is the food quality
                    food_data = fields[2]
                    #service_data has been created to hold the value imported
                    #from the csv's fourth column which is service rating
                    service_data = fields[3]
                    #cost_data has been created to hold the value imported
                    #from the csv's fifth column which is value for money rating
                    cost_data = fields[4]
                    #overall_rating has been created to hold the value imported
                    #from the csv's sixth column which was the restaurants
                    #overall rating
                    overall_data = fields[5]
                    self.append_to_list(restaurant_name,suburb_data,food_data,
                                        service_data,cost_data,overall_data)

    #This method was created to append the imported data from the csv into
    #the restaurant_rating list above. It clearly defines its actions as append_
    #to_list
    def append_to_list(self,restaurant_name,suburb_data,food_data,service_data,
                       cost_data,overall_data):
        restaurant_data = RestaurantData()
        restaurant_data.restaurant=restaurant_name
        restaurant_data.suburb_location=suburb_data
        restaurant_data.food_rating=food_data
        restaurant_data.service_rating=service_data
        restaurant_data.cost_rating=cost_data
        restaurant_data.overall_rating=overall_data

        self.restaurant_rating.append(restaurant_data)
