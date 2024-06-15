import sys
import backend

restaurant_manager = backend.RestaurantManager()

#This class has been created to hold the Program's front end functionality. Its
#name clearly defines what it does in that it acts as the program's user
#interface
class ProgramUI:
     
    #This method was created to run the overall program. This method calls on
    #multiple methods to allow the program to function. Its name clearly
    #explains that it runs the program.
    def run_program(self):
        #Intro has been created to hold the value of the introduction so it
        #could be printed in one section without exceeding the limit of python's
        #80 column limit
        intro = ("This program has been designed to allow you to ")
        intro+=("submit feeback for restaurants.\n")

        sys.stdout.write(intro)
        #file_name is the variable used to store the value of the csv file
        #to be opened.
        x=0
        #This while loop will contin ue to run for a long as the user is
        #trying to open a file that does not exist.
        while(x==0):
            try:
                file_name=self.get_string("\nWhat file would you like to open: ")
                restaurant_manager.load_csv(file_name)
                x=+1
            except:
                sys.stdout.write("\nThat file does not exist, try again: ")
        
        sys.stdout.write("\n"*80)
        sys.stdout.write("What would you like to do?\n")

        #Choice is the variable that holds the user's menu selection choice.
        #Its name is clear and defines what value it holds inside.
        choice = self.display_menu()
        #This while loop will run while the user's choice is not 5. Each
        #sends the user to a different function of the program and if they
        #select 5 the while loop will end and the program will close.
        while(choice!=5):
            if choice == 1:
                sys.stdout.write("\n"*80)
                self.add_entry()
            elif choice == 2:
                sys.stdout.write("\n"*80)
                self.display_entries()
            elif choice == 3:
                sys.stdout.write("\n"*80)
                self.remove_data()
            elif choice == 4:
                sys.stdout.write("\n"*80)
                self.save_all_data()
            else:
                self.get_string("That is not an option. Click return to continue\n")

            choice=self.display_menu()
        sys.stdout.write("\n"*80)
        sys.stdout.write("Thank you for using this program!\n")

    #This method displays the menu to the user. It name clearly defines what it
    #does.
    def display_menu(self):
 
        #The display_menu variable has been created so that the program is able
        #to display each line presented to use user without being restricted
        #by python's maximimum 80 column limit.
        display_menu=("\n[1] Add New Restaurant Rating\n")
        display_menu+=("[2] Display Existing Ratings\n")
        display_menu+=("[3] Remove A Rating\n")
        display_menu+=("[4] Save All Changes\n")
        display_menu+=("[5] Exit\n\n")

        sys.stdout.write(display_menu)

        #The user_choice variable is used to stored the users choice from the
        #get_int method. This value will be returned and used elsewhere in the
        #program.
        user_choice = self.get_int("Choose an option ")
        return user_choice            

    #This method will get and store a users input. This method has been created
    #to save time as when using it in multiple places throughout this program
    def get_string(self,prompt):
        sys.stdout.write(prompt)
        sys.stdout.flush()

        #response is the variable created to house the user's input to be
        #used in other sections of the program.
        response = sys.stdin.readline().strip()
        return response

    #This method will get and store a users input. This method has been created
    #to save time as when using it in multiple places throughout this program
    def get_int(self,prompt):

        #response is the variable created to house the user's input to be
        #used in other sections of the program.
        response = None

        #This while loop was created to ensure that a user inputed a correct
        #input. While the user is inputing an incorrect value, they will be
        #prompted to try again.
        while(response == None):
            try:
                response=int(self.get_string(prompt))
            except:
                prompt = "Must select a whole \"number\". Try again: "
        return response

    #This method will get and store a users input. This method has been created
    #to save time as when using it in multiple places throughout this program
    def get_float(self,prompt):

        #response is the variable created to house the user's input to be
        #used in other sections of the program.
        response = None

        #This while loop was created to ensure that a user inputed a correct
        #input. While the user is inputing an incorrect value, they will be
        #prompted to try again.
        while(response == None):
            try:
                response = float(self.get_string(prompt))
            except:
                prompt = "Must be a number value. Try again: "
            return response
                         

    #This method has been created to enable the user to input new data into the
    #program. This method will ask the user to input the required values and
    #then append them to the list.
    def add_entry(self):
        
        restaurant_name = self.get_string("\nPlease enter restaurant: ").lower()
        suburb_data = self.get_string("\nEnter the suburb: ").lower()

        sys.stdout.write("\nThe following are out of 10\n")
        
        food_data = self.get_float("\nEnter the Food Rating: ")
        service_data = self.get_float("\nEnter the Service Rating: ")
        cost_data = self.get_float("\nEnter the Cost Rating: ")

        sys.stdout.write("\nOverall rating must be a whole number out of 10\n")
        
        overall_data = self.get_int("\nEnter your Overall Rating: ")
        restaurant_manager = backend.RestaurantManager()
        restaurant_manager.append_to_list(restaurant_name,suburb_data,food_data,
                                          service_data,cost_data,overall_data)


    #This method was created to be able to display all values to the user. The
    #name of this method was chosen as it clearly defines its actions.
    def display_entries(self):
        x=0
        #This while loop will continue to run as long as x is lower then the
        #amount of entries in the list. Everytime it searches and displays an
        #item, x will have 1 added to it so it will stop once all are displayed
        while(x<len(restaurant_manager.restaurant_rating)):

            for data in restaurant_manager.restaurant_rating:
                sys.stdout.write("\nRestaurant: "+data.restaurant+
                                 "\nLocation: "+(data.suburb_location)+
                                 "\nFood Rating: "+str(data.food_rating)+
                                 "/10\nService Rating: "+
                                 str(data.service_rating)+
                                 "/10\nCost Rating: "+str(data.cost_rating)+
                                 "/10\nOverall Rating: "+
                                 str(data.overall_rating)+"/10\n\n")
            
                x+=1
        sys.stdout.write("Click enter to continue")
        sys.stdin.readline()
        sys.stdout.write("\n"*80)
                
    #This method has been created to allow the user to save all new data into
    #the csv file. The name was chosen as it clearly explains it will save
    #all data
    def save_all_data(self):
        restaurant_manager = backend.RestaurantManager()
        x=0
        #num_month has been created to store the value of list length to be used
        #in the while loop statically so it cannot change as the while loop is
        #running
        num_month = len(restaurant_manager.restaurant_rating)
        try:
            data_file = open(self.get_string
                             ("What would you like to call this file?")+
                              ".csv","w")

            #This while loop will continue to run as long as x is lower num_month
            #This allows the method to write all new data into the CSV
            while(x<num_month):
                data_file.write(restaurant_manager.restaurant_rating[x].
                                restaurant+",")
                data_file.write((restaurant_manager.restaurant_rating[x].
                                suburb_location)+",")
                data_file.write(str(restaurant_manager.restaurant_rating[x].
                                    food_rating)+",")
                data_file.write(str(restaurant_manager.restaurant_rating[x].
                                    service_rating)+",")
                data_file.write(str(restaurant_manager.restaurant_rating[x].
                                    cost_rating)+",")
                data_file.write(str(restaurant_manager.restaurant_rating[x].
                                    overall_rating)+"\n")
                x += 1
            data_file.close()
            sys.stdout.write("Data has been saved! Click enter to continue")
            sys.stdin.readline()
            sys.stdout.write("\n"*80)
        except:
            sys.stdout.write("Error, could not save")
        
    #This method was created to remove data from the list. When is is called on
    #the method will have the user search for a restaurant and delete any
    #matching entries.
    def remove_data(self):
            restaurant_manager = backend.RestaurantManager()
            if (len(restaurant_manager.restaurant_rating)<=0):
                sys.stdout.write("There are no entries yet, add entry first!\n")
                return

            #search_restaurant is a variable being used to hold the value of the
            #restaurant the user is searching for to delete.
            search_restaurant = self.get_string("What entry do you want to delete? "
                                           ).lower()

            x=0
            #This while loop will run while x is less then the number of entries
            #in the list. As it searches each line and removing any entries it
            #will add 1 to x for each line it searches ensuring it stops once all
            #are searched
            while(x<len(restaurant_manager.restaurant_rating)):
                if (search_restaurant == restaurant_manager.
                    restaurant_rating[x].restaurant):

                    del (restaurant_manager.restaurant_rating[x])

                    x-=1
                    
                x += 1



program_UI = ProgramUI()
program_UI.run_program()


    
