###########################################################
#  Project 06
#
#
# Algorithm:
#           Prompt for a file until a correct file is opened 
#           display menu option
#           read file and convert to tupule
#           if option 1 get output for regions
#           sort characteristics by criterion(holds tuples, criteria, and value)
#           sort characteristics by criteria
#           display characteristics
#           quit the program 
############################################################
import csv
from operator import itemgetter

#constants
NAME = 0
ELEMENT = 1
WEAPON = 2
RARITY = 3
REGION = 4

#menu options
MENU = "\nWelcome to Genshin Impact Character Directory\n\
        Choose one of below options:\n\
        1. Get all available regions\n\
        2. Filter characters by a certain criteria\n\
        3. Filter characters by element, weapon, and rarity\n\
        4. Quit the program\n\
        Enter option: "

#strings
INVALID_INPUT = "\nInvalid input"

CRITERIA_INPUT = "\nChoose the following criteria\n\
                 1. Element\n\
                 2. Weapon\n\
                 3. Rarity\n\
                 4. Region\n\
                 Enter criteria number: "

VALUE_INPUT = "\nEnter value: "

ELEMENT_INPUT = "\nEnter element: "
WEAPON_INPUT = "\nEnter weapon: "
RARITY_INPUT = "\nEnter rarity: "

HEADER_FORMAT = "\n{:20s}{:10s}{:10s}{:<10s}{:25s}"
ROW_FORMAT = "{:20s}{:10s}{:10s}{:<10d}{:25s}"


# function to input correct file name
def open_file():
    '''
    asks the user to input a file name  until a correct file name is inputed
    
    '''
    file_open = input("Enter file name: ")

    #keeps prompting till correct file name is inputed
    while True:
        try:
            open_file = open(file_open)
            return open_file
        except FileNotFoundError:
            print("\nError opening file. Please try again.")
            file_open = input("Enter file name: ")

#function to read the correct file
def read_file(fp):
    '''
    Reads the csv file using file pointer
    Value: file pointer
    Returns: list of tuples where each tuple is a character
    '''
    #reads csv file
    csv_reader = csv.reader(fp)

    #skips header
    next(csv_reader,None)

    list_1 = []

    for line in csv_reader:

        #indexes for each value in csv file
        name = str(line[0])
        rarity = int(line[1])
        element = str(line[2])
        weapon = str(line[3])
        region = str(line[4])
        region = region if region else None

        list_tuple = (name , element , weapon , rarity , region)
        list_1.append(list_tuple)

    return list_1

#function to sort characters by criterion
def get_characters_by_criterion (list_of_tuples, criteria, value):
    '''
    Retrieve the characters that match a certain criteria
     
    '''
    cri_list = [] 

    for x in list_of_tuples:

        if x[criteria] is None:  
            continue    
        elif criteria == RARITY:    
            if x[criteria] == value and type(x[criteria]) is int and type(value) is int:
                cri_list.append(x)
        else:   
            if (value.lower() == x[criteria].lower()) and type(x[criteria]) is str and type(value) is str:
                cri_list.append(x)

    return cri_list

# function to retreive characters by criteria
def get_characters_by_criteria(master_list, element, weapon, rarity):
    '''
    This function takes as parameter the list of tuples returned by the read_file function
(master_list), an element, a weapon, and a rarity and returns a list of tuples filtered using
those 3 criterias
    '''
    criteria_1 = get_characters_by_criterion(master_list , ELEMENT , element)
    criteria_2 = get_characters_by_criterion(criteria_1 , WEAPON , weapon)
    criteria_3 = get_characters_by_criterion(criteria_2 , RARITY, rarity)
    return criteria_3

# function to retreive regions 
def get_region_list  (master_list):
    '''
    Retrieve all available regions into a list
    
    '''
    list_region = []

    for line in master_list:
        region = line[4]
        if region != None:
            if region in list_region:
                continue
            else:
                list_region.append(region)

    list_region_new= sorted(list_region)
    return list_region_new

#function to sort list
def sort_characters (list_of_tuples):
    '''
    Creates a new list where character tuples have been sorted
    
    '''
    return sorted(list_of_tuples, key=itemgetter(3) , reverse = True)

#function to display characters with their info
def display_characters (list_of_tuples):
    '''
    Displays the characters along with their information
    
    '''
    if list_of_tuples == []:
        print("\nNothing to print.")

    else:
        print(HEADER_FORMAT.format("Character", "Element", "Weapon", "Rarity", "Region"))

        for lines in list_of_tuples: 
            region = lines[4]
            if region == None:
                #prints formatted regions
                print(ROW_FORMAT.format( lines[0] , lines[1] , lines[2] , lines[3] , 'N/A' ))
            else:
                print(ROW_FORMAT.format( lines[0] , lines[1] , lines[2] , lines[3] , region ))

#function to retreive menu
def get_option():
    '''
    Prompt for input (MENU in the starter code).
    
    '''
    while True:
        menu_1 = input(MENU)
        try:
            menu_1_int = int(menu_1)
            if 1 <= menu_1_int <= 4:
                return menu_1_int
            else:
                print("\nNothing to print.")
        except ValueError:
            print("\nNothing to print.")


# main function
def main():
    #reads file and outputs list of tuples
    output = read_file(open_file()) 

    #calls for menu   
    menu_1 = get_option()   

    
    while menu_1 != 4:

        #conditions for different menu values selected
        if menu_1 == 1:
            #sorts by region
            print("\nRegions:")     
            regions = get_region_list(output)

            
            print(", ".join(regions) )   

        
        if menu_1 == 2:

            #sorts by criteria
            criteria_entered= input(CRITERIA_INPUT)   
            value_entered = ""

            try:
                criteria_entered_int = int(criteria_entered)
                if not (1 <= criteria_entered_int <= 4):
                    print(INVALID_INPUT)
                    criteria_entered= input(CRITERIA_INPUT)
            except ValueError:
                print(INVALID_INPUT)
                criteria_entered= input(CRITERIA_INPUT)


            value_entered = input(VALUE_INPUT)
            if criteria_entered_int == RARITY:
                try:
                    value_entered = int(value_entered)
                except:
                    print(INVALID_INPUT)
                    menu_1 = get_option()
                    continue    

            character_criterion = get_characters_by_criterion(output, criteria_entered_int, value_entered)    
            character_sort = sort_characters(character_criterion)   
            display_characters(character_sort)   

       
        if menu_1 == 3:

           
            element = (input(ELEMENT_INPUT)).upper()
            weapon = (input(WEAPON_INPUT)).upper()
            rarity = input(RARITY_INPUT)

            while True:
                try:
                    rarity = int(rarity)
                    break
                except ValueError:
                    print(INVALID_INPUT)
                    rarity = input(RARITY_INPUT)

            character_criteria = get_characters_by_criteria(output, element, weapon, rarity)    
            character_sort = sort_characters(character_criteria)   
            display_characters(character_sort)   

        
        menu_1 = get_option()



# DO NOT CHANGE THESE TWO LINES
#These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.  
if __name__ == "__main__":
    main()