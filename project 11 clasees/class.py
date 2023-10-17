###########################################################

    #  Computer Project #11

    #

    #  Algorithm

    #    create a class "Volume" and define attributes(magnitude and units)

    #    create methods __repr__ and __str__ to represend current objet as string

    #    create method is_valid,get_units,get_magnitude,metric_customary

    #       create method __eq__ to compare 2 volume objects

    #       create methods add and sub to add and subtract 2 volume objects

    ###########################################################

#constants
UNITS = ["ml","oz"]
MLperOZ = 29.5735295625  # ml per oz
DELTA = 0.000001

#Class definition
class Volume(object):

    #initializing attributes
    def __init__(self,magnitude= 0,units = "ml"):   # this line is incomplete: parameters needed
        '''accepts two parameters: the magnitude of the volume and the units
in which it is measured'''

        #conditions to check valid magnitude or units
        if magnitude > 0 and (type(magnitude) == int or type(magnitude) == float):
            self.magnitude = magnitude
        elif not (magnitude > 0 and (type(magnitude) == int or type(magnitude) == float)):
            self.magnitude = 0
            self.units = None
        else:
            pass
        
        #defining attributes
        if units in UNITS :
            self.units = units

        elif not(units in UNITS):
            self.magnitude = None
            self.units = None
        else:
            pass


       

    #defining __str__ method   
    def __str__(self):    # this line is incomplete: parameters needed
        '''will return a representation of the current object as a
character string.'''

        #checking to see if object is valid
        if self.units == None or self.magnitude == 0:
            return ("Not a Volume")
        else:
            
            return ("{:.3f} {}".format(self.magnitude,self.units))

    #defining __repr__ method   
    def __repr__(self):    # this line is incomplete: parameters needed
        '''will return a representation of the current object as a
character string.'''

        #checking to see if object is valid
        if self.units == None or self.magnitude == 0:
            return ("Not a Volume")
        else:
           
            return ("{:.6f} {}".format(self.magnitude,self.units))
        
    #defining is_valid method
    def is_valid(self):     # this line is incomplete: parameters needed
        '''Returns a Boolean to indicate whether or not
Volume is valid.'''

        #conditions
        if self.units == None or self.magnitude == 0:
            return False
        else:
            return True
    
    #defining get_units method
    def get_units(self):     # this line is incomplete: parameters needed
        '''Returns units stored during construction'''
        if self.units == None or self.magnitude == 0 :
            return None
        else:
            return self.units
    
    #defining get_magnitude method
    def get_magnitude(self):  # this line is incomplete: parameters needed
        '''Returns magnitude stored during construction'''
        if self.magnitude == 0:
            return (0)
        else:
            return self.magnitude
    
    #defining metric method
    def metric(self):      # this line is incomplete: parameters needed
        '''Returns a Volume object equivalent to V
(in the metric system if V is valid otherwise
it returns an invalid Volume object)'''

        #cheking if object is valid
        if self.units == None or self.magnitude == 0:
            return Volume(self.magnitude,self.units)
        
        #if unit is already in metric
        elif self.units == "ml":
            new = (self.magnitude,self.units)
            return Volume(new)

        #conversion
        else:
            conv = self.magnitude *MLperOZ
            return Volume(conv, UNITS[0]) 
            
    #defining customary method 
    def customary(self):    # this line is incomplete: parameters needed
        '''Returns a Volume object equivalent to V
(in the US customary system if V is valid).
otherwise, it returns an invalid Volume object)'''

        #cheking if object is valid
        if self.units == None or self.magnitude == 0:
            return Volume(self.magnitude,self.units)

        #if unit is already in customary
        elif self.units == "oz":
            new = (self.magnitude,self.units)
            return Volume(new)
        
        #conversion
        else:
            conv = self.magnitude /MLperOZ
            return Volume(conv, UNITS[1]) 

    #defining __eq__ method    
    def __eq__(self,other):  # this line is incomplete: parameters needed
        '''The class will have an __eq__ method which will be called when the == will be called'''

        #cheking if object is valid
        if self.units == None or self.magnitude == 0:
            return False
        
        #comparing values to check equality
        elif other.get_units() == None or other.get_magnitude() == 0:
            return False
        elif self.units != other.get_units():
            if self.units == UNITS[0]:
                new = self
                new1= new.customary()
                if abs(new1.get_magnitude() - other.get_magnitude()) < DELTA:
                    return True
                else:
                    return False
            elif self.units == UNITS[1]:
                new = self
                new1= new.metric()
                if abs(new1.get_magnitude() - other.get_magnitude()) < DELTA:
                    return True
                else:
                    return False
        else:
            return True

    #defining add method
    def add(self,other):  # this line is incomplete: parameters needed
        '''addition of two “Volume” objects.'''

        #cheking if object is valid
        if self.units == None or self.magnitude == 0:
            return Volume(None,None)
        
        #if other is a constant
        elif type(other) == int or type(other) == float:
            return Volume((self.magnitude+other),self.units)
        elif other.get_units() == None or other.get_magnitude() == 0:
            return Volume(None,None)
        
        #addition of objects
        else:
            if self.units != other.units:
                if self.units == UNITS[0]:
                    new = other
                    new1= new.metric()
                    
                    return Volume((self.magnitude+new1.magnitude),self.units)
                elif self.units == UNITS[1]:
                    new = other
                    new1= new.customary()
                    return Volume((self.magnitude+new1.magnitude),self.units)
                else:
                    pass
                   
            elif self.units == other.units:
                return Volume((self.magnitude+other.magnitude),self.units)
            else:
                pass
    
    #defining sub method
    def sub(self,other): # this line is incomplete: parameters needed
        '''subtraction of two “Volume” objects.'''

        #cheking if object is valid
        if self.units == None or self.magnitude == 0:
            return Volume(None,None)

        #if other is a constant
        elif type(other) == int or type(other) == float:
            return Volume((self.magnitude-other),self.units)

        elif other.get_units() == None or other.get_magnitude() == 0:
            return Volume(None,None)
        
        #subtraction of objects
        else:
            if self.units != other.units:
                if self.units == UNITS[0]:
                    new = other
                    new1= new.metric()
                    
                    return Volume((self.magnitude-new1.magnitude),self.units)
                elif self.units == UNITS[1]:
                    new = other
                    new1= new.customary()
                    return Volume((self.magnitude-new1.magnitude),self.units)
                else:
                    pass
                   
            elif self.units == other.units:
                return Volume((self.magnitude-other.magnitude),self.units)
            else:
                pass
