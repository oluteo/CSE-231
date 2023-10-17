###########################################################

    #  Computer Project #9

    #

    #  Algorithm

    #    get the securities and prices file pointer

    #    create a set and master dictionary from the securities file pointer

    #    edit the master dictionary by adding prices from the prices file pointer

    #       get the max price of a company

    #       find the max and average company price

    #       create a display function to properly display outputs

    #       in main:

    #               print banner and create master dictionary
    #               display options and ask user for input till a valid input is given
    #               for options:
    #                   option 1 prints the set of companies 
    #                   option 2 prints company symbols
    #                   option 3 prompts for a company symbol and displays max price of that  company
    #                   option 4 finds the max company price
    #                   option 5 prompts for a company symbol and displays average price of that  company                
    #                    option 6 quits the program
    ###########################################################
import csv
import string
MENU = '''\nSelect an option from below:
            (1) Display all companies in the New York Stock Exchange
            (2) Display companies' symbols
            (3) Find max price of a company
            (4) Find the company with the maximum stock price
            (5) Find the average price of a company's stock
            (6) quit
    '''
WELCOME = "Welcome to the New York Stock Exchange.\n"
    
#function to open files and return the pointer
def open_file():
    '''This function is going to ask the user for both files to open. keeps looping for the
first one until a file is open.then the second'''
    cont = True
    new = True
    #prompt to input file name
    prompt = input("\nEnter the price's filename: ")

    #loop till correct file name is inputed
    while cont:
        try: 
            prices_fp = open(prompt,"r")
            cont = False
        except FileNotFoundError: 
            print("\nFile not found. Please try again.")
            prompt = input("\nEnter the price's filename: ")
    #prompt to input file name
    prompt = input("\nEnter the security's filename: ")

    #loop till correct file name is inputed
    while new:
        try: 
            
            securities_fp = open(prompt,"r")
            new = False
        except FileNotFoundError: 
            print("\nFile not found. Please try again.")
            prompt = input("\nEnter the security's filename: ")
    return (prices_fp,securities_fp)

#function to create a master dictionary from the securities file pointer
def read_file(securities_fp):
    '''This function takes the security’s file pointer that has the names of the companies and
their codes '''

    #csv reader to read the file pointer
    file_read = csv.reader(securities_fp)
    set_name = set()
    master_dictionary = dict()
    value_list = []
    next(file_read,None)

    #iterating through the file
    for line in file_read:
        
        #line.strip(",")
        #line.split(",")

        #indexing for each value to be retrieved
        company_name = line[1]
        
        company_code = line[0]
        sector_company = line[3]
        subsector_company = line[4]
        address = line[5]
        date_added = line[6]
        empty_lst = []
        
        #appending to empty list
        value_list.append(str(company_name))
        value_list.append(str(sector_company))
        value_list.append(str(subsector_company))
        value_list.append(str(address))
        value_list.append(str(date_added))
        value_list.append(empty_lst)

        #adding to master dictionary
        master_dictionary[company_code] = value_list
        value_list=[]
        set_name.add(company_name)
    return (set_name,master_dictionary)

#function that adds prices to the master dictionary using the prices file pointer    
def add_prices (master_dictionary, prices_file_pointer):
    '''This function does not return anything, but it changes the master dictionary while reading
the prices file'''
    prices_list = []

    #csv reader to read the file pointer
    file_read = csv.reader(prices_file_pointer)
    next(file_read,None)

    #iterating through the file
    for line in file_read:

        #indexing for each value to be retrieved
        date = line[0]
        open_info = float(line[2])
        close_info = float(line[3])
        low_info = float(line[4])
        high_info = float(line[5])
        prices_list.append(date)
        prices_list.append(open_info)
        prices_list.append(close_info)
        prices_list.append(low_info)
        prices_list.append(high_info)
        
        #appending prices to the empty list in the master dictionary
        for key,value in master_dictionary.items():
            if line[1] == key:
                
                value[5].append(prices_list)
        prices_list = []        

#function that outputs the maximum price of an inputed company symbol       
def get_max_price_of_company (master_dictionary, company_symbol):
    '''This function takes the master dictionary and a company symbol, and it gets the max high
price and the date of the max price. It returns the tuple'''
    
    #checking to see if the symbol exists
    if company_symbol in master_dictionary:
        info = master_dictionary[company_symbol][5]
        output = []

        #iterating through the prices list in the master dictionary value
        for each in info:
            high_values = each[4]
            date_values = each [0]
            output.append((high_values,date_values))

        #check to see if theres a value
        if len(output) == 0 :
            return(None,None)
        else:
            #max price and date outputed
            max_info = max(output)
            return max_info
    else:
        return(None,None)

#funtion to find the company with the current highest price
def find_max_company_price (master_dictionary):
    '''This function takes the master dictionary and finds the company with the highest high
price'''
    
    list_tup = []
    sym_lst = []

    #iterating through the dictionary
    for key in master_dictionary:
        tup = get_max_price_of_company(master_dictionary,key)

        #check to see if there is value
        if not (tup == (None,None)):
            list_tup.append((tup[0],key))
        else:
            pass
    
    #finding the max price and company symbol
    (max_val,max_sym) = max(list_tup)
    
                
    return max_sym,max_val
    
#function that outputs the average price of an inputed company symbol      
def get_avg_price_of_company (master_dictionary, company_symbol):
    '''This function uses the master dictionary and company symbol to find the average high
price for the company'''
    output = []

    #check to see if symbol exists
    if company_symbol in master_dictionary:
        info = master_dictionary[company_symbol][5]
        
        #assigning index to the value to be retrieved
        for each in info:
            high_values = float(each[4])
            output.append(high_values)

        #checking for zero division error
        try:
            average = sum(output)/len(output)
            return round(average,2)
        except:
            average = sum(output)/1
            return round(average,2)
            
    else:
        return (0.0) 

#function to display in a better format    
def display_list (lst):  # "{:^35s}"
    '''takes a list of strings and displays that list in three
columns, each column is 35 characters wide'''

    #zip funtion used
    for a,b,c in zip(lst[::3],lst[1::3],lst[2::3]):
        formatted = ("{:^35s}{:^35s}{:^35s}".format(a,b,c))
        
        L = len(a)
        
        #print (lst[-1])
        print (formatted)
   
#main function to interract with user           
def main():

    #printed banner
    print(WELCOME)

    #opening file, getting file pointers and creating master dictionary
    file_pointers = open_file()
    securities_fp_dict = read_file(file_pointers[1])
    add_prices(securities_fp_dict[1],file_pointers[0])

    #printing menu of options
    print(MENU)

    #prompting for an option
    prompt_option = input("\nOption: ")

    #loop till exited
    while prompt_option != "6":

        #option 1 prints the set of companies 
        if prompt_option == "1":
            print("\n{:^105s}".format("Companies in the New York Stock Market from 2010 to 2016"))
            display_list(sorted(securities_fp_dict[0]))
            print("\n")

        #option 2 prints company symbols
        elif prompt_option == "2":
            symbols_ = []
            print(("\ncompanies' symbols:"))
            for key,value in securities_fp_dict[1].items():
                symbols_.append(key)
            display_list(sorted(symbols_))
            print("\n")

        #option 3 prompts for a company symbol and displays max price of that  company
        elif prompt_option == "3":

            #prompting for company symbol
            prompt_sym = input("\nEnter company symbol for max price: ")

            #loop til correct symbol is inputed
            while prompt_sym not in securities_fp_dict[1]:
                print("\nError: not a company symbol. Please try again.")
                prompt_sym = input("\nEnter company symbol for max price: ")
            else:
                pass
            max_price = get_max_price_of_company (securities_fp_dict[1],prompt_sym)
        
            if max_price == (None,None):
                print("\nThere were no prices.")
            else:
                print("\nThe maximum stock price was ${:.2f} on the date {:s}/\n".format(max_price[0],max_price[1]))

        #option 4 finds the max company price
        elif prompt_option == "4": 
            max_stock_price = find_max_company_price (securities_fp_dict[1])
            print("\nThe company with the highest stock price is {:s} with a value of ${:.2f}\n".format (max_stock_price[0],max_stock_price[1]))

        #option 5 prompts for a company symbol and displays average price of that  compan
        elif prompt_option == "5": 

            #prompting for company symbol
            prompt_sym = input("\nEnter company symbol for average price: ")

            #loop till correct symbol is inputed
            while prompt_sym not in securities_fp_dict[1]:
                print("\nError: not a company symbol. Please try again.")
                prompt_sym = input("\nEnter company symbol for average price: ")
            else:
                pass
            avg_price = get_avg_price_of_company (securities_fp_dict[1],prompt_sym)
            
            if avg_price == (0.0):
                print("\nThere were no prices.")
            else:
                print("\nThe average stock price was ${:.2f}.\n".format(avg_price))
        else:
            print("\nInvalid option. Please try again.")
        
        #reprint menu
        print(MENU)
        prompt_option = input("\nOption: ")    
    else:
        pass
    
if __name__ == "__main__": 
    main() 
