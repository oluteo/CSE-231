###########################################################

    #  Computer Project #8

    #

    #  Algorithm

    #    prompt for a file name till correct input is given(return file pointer)

    #    read the names from the name file and return list of names

    #    read the frineds file and retun the list of friends for each name 

    #       create a dictionary of the friends and use it to find the common friends, max common friends, second friends, and max second friends

    #       find max friends of all the names
    #       for option 4: prompt for a name and display all the friends of that person

    ###########################################################

 
import string
MENU = '''
 Menu : 
    1: Popular people (with the most friends). 
    2: Non-friends with the most friends in common.
    3: People with the most second-order friends. 
    4: Input member name, to print the friends  
    5: Quit                       '''

#function to open files and return the pointer
def open_file(s):
    '''This function prompts the user to input a file name to open and keeps prompting until a
correct name is entered.'''

    #prompt to input file name
    prompt = input("\nInput a {} file: ".format(s))

    #loop till correct file name is inputed
    while True:
        try: 
            fp = open(prompt,"r")
            return fp
        except FileNotFoundError: 
            print("\nError in opening file.")
            prompt = input("\nInput a {} file: ".format(s))
    return fp

#function to read all the names from the name.txt file
def read_names(fp):
    '''This function reads the Names.txt file using file pointer, fp.'''

    read_names_list = []

    #iterate through all the lines and append to empty list
    for line in fp:
        edited = line.strip("\n")
        read_names_list.append(edited)
    return read_names_list

#function to pair all the names with their list of friends
def read_friends(fp,names_lst):
    '''This function reads the Friends.csv file using file pointer, fp'''
    read_friends_list = []
    
    #iterate through the friends.csv file
    for line in fp:
        list_of_no = []
        lst = []
    #num_friends = line.strip(",")
        num_friends = line.split(",")
        for x in num_friends:
            try :
                x = int(x)
                list_of_no.append(x)
            except (TypeError,ValueError) :
                continue
            
            #x = x.strip()
        num_friends = list_of_no   
        for each in num_friends:

            #apending the index of each friend to frined list 
            friend_name = names_lst[each]
            lst.append(friend_name)
        read_friends_list.append(lst)
    return read_friends_list        

#function to create a dictionary of all the names and their friends 
def create_friends_dict(names_lst,friends_lst):
    '''This function takes the two lists created in the read_names function and the
read_friends function and builds a dictionary'''
    friends_dict = dict()

    #iterating through the dictionary and assigning each name to their friend with name ad key and friends as value
    for line,y in enumerate(names_lst):
        friends_dict[y] = friends_lst[line]
    return friends_dict        

#function to find the people that have frinds in common and their friends
def find_common_friends(name1, name2, friends_dict):
    '''This function takes two names (strings) and the friends_dict (returned by the
create_friends_dict) and returns a set of friends that the two names have in
common.'''

    #putting each friend list in sets and finding the intersection of the two
    friends_1 = set(friends_dict[name1])
    friends_2 = set(friends_dict[name2])
    common_friends = friends_1 & friends_2
    return common_friends

#function to find the person with the most number of friends
def find_max_friends(names_lst, friends_lst):
    '''This function takes a list of names and the corresponding list of friends and determines
who has the most friends'''
    max_list = []
    no_of_fri = []

    #iterrating through the list
    for line,y in enumerate(names_lst):

        #finding the length of the frinds each person has and adding to a new list
        no_ = len(friends_lst[line])
        no_of_fri.append(no_)

    #calculating the maximum number in the list
    max_no = max(no_of_fri)

    #finding all the people that have the calculated maximum number of friends
    for t,w in enumerate(no_of_fri):
        if w ==max_no:
            max_list.append(names_lst[t])

    return (sorted(max_list), max_no)

#function to find the maximum number of common friends
def find_max_common_friends(friends_dict):
    '''This function takes the friends dictionary and finds which pairs of people have the most
friends in common.'''
    edited_pairs = []
    no_of_fri = []
    possible_pairs = []
    key_dict = dict()

    #iterating through the dictionrary 
    for key, value in friends_dict.items():
        for key2,value2 in friends_dict.items():
            
            #including he constraints
            if (key2,key) in key_dict :
                continue
            elif key == key2:
                continue
            elif key2 in value:
                continue
            elif key in value2 :
                continue
            
            #storing the keys in a dictionary
            common_friends = find_common_friends(key, key2, friends_dict)
            key_dict[(key,key2)]= common_friends
    
    #syntax to calculate the max no. of common friends
    for line,y in key_dict.items():
        no_ = len(y)
        no_of_fri.append(no_)
    max_no = max(no_of_fri)
    for line,y in key_dict.items():
        if len(y) ==max_no:
            edited_pairs.append(line)

    return (edited_pairs, max_no)

#function to find the friends of friends of a person   
def find_second_friends(friends_dict):
    '''Here we consider second-order friendships, that is, friends of friends.'''
    second_dict = dict()

    #iterating through the dictionary
    for line,y in friends_dict.items():
        f_set = set()

        #grouping each friend of friend in a set 
        for each in y: 
            friends_friends = friends_dict[each]
            f_set =f_set.union(set(friends_friends)) 

        #discarding unecessary names
        f_set.discard(line)
        f_set-= set(y)
        second_dict[line] = f_set         
    return (second_dict)

#function to find the person with the maximum number od second friends
def find_max_second_friends(seconds_dict):
    '''Here we again consider the max of second-order friendships, that is, friends of friends'''
    no_of_fri = []
    edited_pairs= []

    #iterating through the dictionary
    for line,y in seconds_dict.items():
        no_ = len(y)
        no_of_fri.append(no_)
    max_no = max(no_of_fri)
    for line,y in seconds_dict.items():
        if len(y) ==max_no:
            edited_pairs.append(line)

    return (edited_pairs, max_no)

#main function to interact with the user
def main():
    print("\nFriend Network\n")
    fp = open_file("names")
    names_lst = read_names(fp)
    fp = open_file("friends")
    friends_lst = read_friends(fp,names_lst)
    friends_dict = create_friends_dict(names_lst,friends_lst)

    for name,friends in friends_dict.items():
     #   print(name,":")
      #  print("   {}".format(friends))
      pass

    #list of options to select from
    print(MENU)
    choice = input("\nChoose an option: ")
    while choice not in "12345":
        print("Error in choice. Try again.")
        choice = input("Choose an option: ")
        
    while choice != '5':

        if choice == "1":
            max_friends, max_val = find_max_friends(names_lst, friends_lst)
            print("\nThe maximum number of friends:", max_val)
            print("People with most friends:")
            for name in max_friends:
                print(name)
                pass
                
        elif choice == "2":
            max_names, max_val = find_max_common_friends(friends_dict)
            print("\nThe maximum number of commmon friends:", max_val)
            print("Pairs of non-friends with the most friends in common:")
            for name in max_names:
                print(name)
                
        elif choice == "3":
            seconds_dict = find_second_friends(friends_dict)
            max_seconds, max_val = find_max_second_friends(seconds_dict)
            print("\nThe maximum number of second-order friends:", max_val)
            print("People with the most second_order friends:")
            for name in max_seconds:
                print(name)

        #option 4       
        elif choice == "4":
            cont= True

            #prompting for a name
            Prompt= input("\nEnter a name: ")

            #looping till a valid name is entered
            while cont:
                try :
                    friends_dict[Prompt]
                    #print("duakduhuasidhaisd")
                    print("\nFriends of {}:" .format(Prompt))

                    #printing the frineds of the name
                    for each in friends_dict[Prompt] :
                        print (each)
                    cont = False
                except:
                    print("\nThe name {} is not in the list.".format(Prompt))

                    Prompt= input("\nEnter a name: ")

        else: 
            print("Shouldn't get here.")
            
        choice = input("\nChoose an option: ")
        while choice not in "12345":
            print("Error in choice. Try again.")
            choice = input("Choose an option: ")

if __name__ == "__main__":
    main()
