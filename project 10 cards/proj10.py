###########################################################

    #  Computer Project #10

    # 

    #  Algorithm

    #    initialize table

    #    display menu

    #    display board

    #       prompt for an option and check validity through parse

    #       loop:

    #           if option is TF move card from tableau to foundation(check for win)

    #           if option is TT move card from tableau to tableau

    #           if option is WT move card from waste to tableau

    #           if option is WF move card from waste to foundation(check for win)

    #           if option is SW move card from stock to waste

    #           if option is R reatsrt game by intializing again

    #           if option is H display menu of choices

    #           if option is W quit program

    ###########################################################
from cards import Card, Deck

MENU ='''Prompt the user for an option and check that the input has the 
       form requested in the menu, printing an error message, if not.
       Return:
    TT s d: Move card from end of Tableau pile s to end of pile d.
    TF s d: Move card from end of Tableau pile s to Foundation d.
    WT d: Move card from Waste to Tableau pile d.
    WF d: Move card from Waste to Foundation pile d.
    SW : Move card from Stock to Waste.
    R: Restart the game (after shuffling)
    H: Display this menu of choices
    Q: Quit the game        
    '''

#initializes the first state of the game
def initialize():
    '''The function has no parameters and returns the starting state of the game with the four data
structures'''
    foundation = [[],[],[],[]]#create foundation
    tableau = [[],[],[],[],[],[],[]] #create tableau
    stock = Deck() #create deck
    stock.shuffle() #shuffle deck
    waste = []#create waste
    
    #dealing cards to each tableau column
    for i in range(1):
        tableau[0].append(stock.deal())
        tableau[1].append(stock.deal())
        tableau[2].append(stock.deal())
        tableau[3].append(stock.deal())
        tableau[4].append(stock.deal())
        tableau[5].append(stock.deal())
        tableau[6].append(stock.deal())
        for i in range(1):
            tableau[1].append(stock.deal())
            tableau[2].append(stock.deal())
            tableau[3].append(stock.deal())
            tableau[4].append(stock.deal())
            tableau[5].append(stock.deal())
            tableau[6].append(stock.deal())
            for i in range(1):
                tableau[2].append(stock.deal())
                tableau[3].append(stock.deal())
                tableau[4].append(stock.deal())
                tableau[5].append(stock.deal())
                tableau[6].append(stock.deal())
                for i in range(1):
                    tableau[3].append(stock.deal())
                    tableau[4].append(stock.deal())
                    tableau[5].append(stock.deal())
                    tableau[6].append(stock.deal())
                    for i in range(1):
                        tableau[4].append(stock.deal())
                        tableau[5].append(stock.deal())
                        tableau[6].append(stock.deal())
                        for i in range(1):
                            tableau[5].append(stock.deal())
                            tableau[6].append(stock.deal())
                            for i in range(1):
                                tableau[6].append(stock.deal())
    
    #flipping last cards in tableau 2 to 7
    for i in tableau[6][0:6]:
        i.flip_card()
    for i in tableau[5][0:5]:
        i.flip_card()
    for i in tableau[4][0:4]:
        i.flip_card()
    for i in tableau[3][0:3]:
        i.flip_card()
    for i in tableau[2][0:2]:
        i.flip_card()
    for i in tableau[1][0:1]:
        i.flip_card()

    #dealing last card in stock to waste pile
    waste.append(stock.deal())

    return(tableau,stock,foundation,waste)     
    
#displays the game setup
def display(tableau, stock, foundation, waste):
    """ display the game setup """
    stock_top_card = "empty"
    found_top_cards = ["empty","empty","empty","empty"]
    waste_top_card = "empty"
    if len(waste):
        waste_top_card = waste[-1] 
    if len(stock):
        stock_top_card = "XX" #stock[-1]
    for i in range(4):
        if len(foundation[i]):
            found_top_cards[i] = foundation[i][-1]
    print()
    print("{:5s} {:5s} \t\t\t\t\t {}".format("stock","waste","foundation"))
    print("\t\t\t\t     ",end = '')
    for i in range(4):
        print(" {:5d} ".format(i+1),end = '')
    print()
    print("{:5s} {:5s} \t\t\t\t".format(str(stock_top_card), str(waste_top_card)), end = "")
    for i in found_top_cards:
        print(" {:5s} ".format(str(i)), end = "")
    print()
    print()
    print()
    print()
    print("\t\t\t\t\t{}".format("tableau"))
    print("\t\t ", end = '')
    for i in range(7):
        print(" {:5d} ".format(i+1),end = '')
    print()
    # calculate length of longest tableau column
    max_length = max([len(stack) for stack in tableau])
    for i in range(max_length):
        print("\t\t    ",end = '')
        for tab_list in tableau:
            # print card if it exists, else print blank
            try:
                print(" {:5s} ".format(str(tab_list[i])), end = '')
            except IndexError:
                print(" {:5s} ".format(''), end = '')
        print()
    print()
    
# function to movw card from stock to the waste
def stock_to_waste( stock, waste ):
    '''That function has two parameters: the data structure representing the stock, and the data
structure representing the waste'''
    
    #check to see if stock is empty
    if stock.is_empty() :
        
        return False
    else:
        #appending stock to waste
        waste.append(stock.deal())
        return True

#function to check if two cards are the same colour
def check (suit1, suit2):

    ''' collects 2 variables and compares suits '''

    #conditions to determine if cards are the same colour
    if suit1 == 1 and (suit2 ==1 or suit2 ==4) :
        return False
    elif suit1 == 2 and (suit2 ==2 or suit2 ==3):
        return False
    elif suit1 == 3 and (suit2 ==3 or suit2 ==2):
        return False
    elif suit1 == 4 and (suit2 ==4 or suit2 ==1):
        return False
    else:
        return True
    
#function to move a card from the waste to the tableau
def waste_to_tableau( waste, tableau, t_num ):
    '''That function has three parameters: the data structure representing the waste, the data structure
representing the tableau, and a column number (the correct index in the tableau).'''
    card = waste[-1]
    card_suit = card.suit()
    
    #checking to see if tableau column is empty
    if len(tableau[t_num]) == 0:
        if card.rank()== 13:
            tableau[t_num].append(waste.pop())
            return True
        else:
            return False
    
    #checking rank and suit of tableau card
    elif (tableau[t_num][-1].rank() == card.rank() + 1) and (check(tableau[t_num][-1].suit(),card_suit))  :
        tableau[t_num].append(waste.pop())
        return True
        
    else:
        return False


#function to move a card from waste to the foundation
def waste_to_foundation( waste, foundation, f_num ):
    '''That function has three parameters: the data structure representing the waste, the data structure
representing the foundations, and a foundation number (the correct index in the foundation)'''
    card = waste[-1]

     #checking to see if foundation column is empty
    if len(foundation[f_num]) == 0:

        #check to see if card is an ace
        if card.rank() == 1 :
            foundation[f_num].append(waste.pop())
            return True    
        else :
            return False

    #check to see if card is the same suit and one rank below
    elif (foundation[f_num][-1].suit() == card.suit()) and (card.rank() == 1 + foundation[f_num][-1].rank()) :
        foundation[f_num].append(waste.pop())
        return True 
    else:
        return False
    

#function to move a card from tableau to the foundation
def tableau_to_foundation( tableau, foundation, t_num, f_num ):
    '''That function has four parameters: the data structure representing the tableau, the data structure
representing the foundations, a column number, and a foundation number.'''
    
    #checking to see if the foundation column is empty
    if len(foundation[f_num]) == 0:

        #checking to see if card is an ace
        if tableau[t_num][-1].rank() == 1 :
            foundation[f_num].append(tableau[t_num].pop())

            #code to flip last card in tableau
            if len(tableau[t_num])!=0:
                if tableau[t_num][-1].is_face_up() == True:
                    pass
                else:
                    tableau[t_num][-1].flip_card()
                
            return True    
        else :
            return False

    #checking rank and suite of card
    elif (foundation[f_num][-1].suit() == tableau[t_num][-1].suit()) and (tableau[t_num][-1].rank() == 1 + foundation[f_num][-1].rank()) :
        foundation[f_num].append(tableau[t_num].pop())

        #code to flip last card in tableau
        if len(tableau[t_num])!=0:
            if tableau[t_num][-1].is_face_up() == True:
                    pass
            else:
                tableau[t_num][-1].flip_card()
        return True 
    else:
        return False

#function to move card from a column on the tableau to another column
def tableau_to_tableau( tableau, t_num1, t_num2 ):
    '''That function has three parameters: the data structure representing the tableau, a source column
number, and a destination column number'''
    card = tableau[t_num1]
    card_suit = card[-1].suit()
    
    #checking to see if tableau column is empty
    if len(tableau[t_num2]) == 0:

        #checking to see if card is a king
        if card[-1].rank()== 13:
            tableau[t_num2].append(tableau[t_num1].pop())
            if len(tableau[t_num1])!=0:

                #code to flip last card in tableau
                if tableau[t_num1][-1].is_face_up() == True:
                    pass    
                else:
                    tableau[t_num1][-1].flip_card()
            return True
        else:
            return False

    #checking rank and suit of card
    elif (tableau[t_num2][-1].rank() == card[-1].rank() + 1) and (check(tableau[t_num2][-1].suit(),card_suit))  :
        tableau[t_num2].append(tableau[t_num1].pop())
        if len(tableau[t_num1])!=0:

            #code to flip last card in tableau
            if tableau[t_num1][-1].is_face_up() == True:
                pass    
            else:
                tableau[t_num1][-1].flip_card()
        return True
        
    else:
        return False

#funtion to check if game has been won
def check_win (stock, waste, foundation, tableau):
    '''Returns True if the game is in a winning state: all cards are in the foundation, stock is empty,
waste is empty and tableau is empty. Otherwise, return False.'''
    total = 0 
    count = 0

    #counting cards in foundation
    for value in foundation:
        if value == []: #if foundation is empty skip that list
            continue
        total += value[-1].rank()
    for each in tableau:
        if len(each)== 0:
            count+=1


    #checking if card total is right and all other variables are empty
    if (total ==52) and stock.is_empty() and (len(waste)==0) and (count ==7): 
        return True
    else:
        return False
    
def parse_option(in_str):
    '''Prompt the user for an option and check that the input has the 
           form requested in the menu, printing an error message, if not.
           Return:
        TT s d: Move card from end of Tableau pile s to end of pile d.
        TF s d: Move card from end of Tableau pile s to Foundation d.
        WT d: Move card from Waste to Tableau pile d.
        WF d: Move card from Waste to Foundation pile d.
        SW : Move card from Stock to Waste.
        R: Restart the game (after shuffling)
        H: Display this menu of choices
        Q: Quit the game        
        '''
    option_list = in_str.strip().split()
    
    opt_char = option_list[0][0].upper()
    
    if opt_char in 'RHQ' and len(option_list) == 1:  # correct format
        return [opt_char]
    
    if opt_char == 'S' and len(option_list) == 1:
        if option_list[0].upper() == 'SW':
            return ['SW']
    
    if opt_char == 'W' and len(option_list) == 2:
        if option_list[0].upper() == 'WT' or option_list[0].upper() == 'WF':
            dest = option_list[1] 
            if dest.isdigit():
                dest = int(dest)
                if option_list[0].upper() == 'WT' and (dest < 1 or dest > 7):
                    print("\nError in Destination")
                    return None
                if option_list[0].upper() == 'WF' and (dest < 1 or dest > 4):
                    print("\nError in Destination")
                    return None
                opt_str = option_list[0].strip().upper()
                return [opt_str,dest]
                               
    if opt_char == 'T' and len(option_list) == 3 and option_list[1].isdigit() \
        and option_list[2].isdigit():
        opt_str = option_list[0].strip().upper()
        if opt_str in ['TT','TF']:
            source = int(option_list[1])
            dest = int(option_list[2])
            # check for valid source values
            if opt_str in ['TT','TF'] and (source < 1 or source > 7):
                print("\nError in Source.")
                return None
            #elif opt_str == 'MFT' and (source < 0 or source > 3):
                #print("Error in Source.")
                #return None
            # source values are valid
            # check for valid destination values
            if (opt_str =='TT' and (dest < 1 or dest > 7)) \
                or (opt_str == 'TF' and (dest < 1 or dest > 4)):
                print("\nError in Destination")
                return None
            return [opt_str,source,dest]

    print("\nError in option:", in_str)
    return None   # none of the above

#main function
def main():   
    '''That function has no parameters; it controls overall execution of the program.'''
    start = initialize()
    tableau=  start[0]
    stock=  start[1]
    foundation =  start[2]
    waste=  start[3]

    print(MENU)
    display(start[0],start[1],start[2],start[3])
    option_in = input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): ")
    parse_re = parse_option(option_in)
    if parse_re == None:
        display(start[0],start[1],start[2],start[3])
        option_in = input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): ")
        parse_re = parse_option(option_in)
    else:
        pass
    
    
    while parse_re[0] != "Q":
        if parse_re[0] == "TF":
            s = int(parse_re[1])
            d = int(parse_re[2])

            result = tableau_to_foundation( tableau, foundation, s, d )
            if result == False:
                print("\nInvalid move!\n")
            else:
                if (check_win (stock, waste, foundation, tableau)) == True:
                    print("You won!")
                    display(start[0],start[1],start[2],start[3])
                    option_in == "Q"
                else:
                    display(start[0],start[1],start[2],start[3])
        elif parse_re[0] == "TT":
            s = int(parse_re[1])
            d = int(parse_re[2])
            result = tableau_to_foundation( tableau, foundation, s, d )
            if result == False:
                print("\nInvalid move!\n")
            else:
                display(start[0],start[1],start[2],start[3])
        elif parse_re[0] == "WT":
            n = parse_re[3]
            watse_re = waste_to_tableau( waste, tableau,n)
            if watse_re == False:
                print("\nInvalid move!\n")
            else:
                display(start[0],start[1],start[2],start[3])

        elif parse_re[0] == "WF":
            n = parse_re[3]
            watse_re = waste_to_tableau( waste, foundation,n)
            if watse_re == False:
                print("\nInvalid move!\n")
            else:
                if (check_win (stock, waste, foundation, tableau)) == True:
                    print("You won!")
                    display(start[0],start[1],start[2],start[3])
                    option_in == "Q"
                else:
                    display(start[0],start[1],start[2],start[3])
        elif parse_re[0] == "SW":
            stock_re = stock_to_waste( stock, waste )
            if stock_re == True:
                display(start[0],start[1],start[2],start[3])
            else:
               print("\nInvalid move!\n") 
        elif parse_re[0] == "R":
            start = initialize()
            print(MENU)
            display(start[0],start[1],start[2],start[3])
        elif parse_re[0] == "H":
            print(MENU)
        elif parse_re[0] == "Q":
            quit
        else:
            pass
        option_in = input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): ")
        parse_re = parse_option(option_in)
        if parse_re == None:
            display(start[0],start[1],start[2],start[3])
            option_in = input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): ")
            parse_re = parse_option(option_in)
        else:
            pass    
    else:
        pass    






if __name__ == '__main__':
     main()
