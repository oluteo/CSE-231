
##################################################
#   Computer Project #5
#   
#              
#   Algorithm:
#              prompt for a file to input
#               loop till a correct file is inputed
#               read through file and collect required values
#               assign to right values to the right functions
#               check if planet is habitable
#              close the file
#              print all information
##################################################
import math

#Constants
PI = math.pi   
EARTH_MASS =  5.972E+24    # kg
EARTH_RADIUS = 6.371E+6    # meters
SOLAR_RADIUS = 6.975E+8    # radius of star in meters
AU = 1.496E+11             # distance earth to sun in meters
PARSEC_LY = 3.262

#prompt to open the appropriate file
def open_file():
    ''' Docstring '''
    
    file_open = input("Input data to open: ")
    file_open_a = file_open + ".csv"
    while not (file_open == "KGF" or file_open == "all" or file_open == "small" or file_open == "singlestar") :
        try :
            file_open_a = open(file_open_a, "r")
            
        except FileNotFoundError :
            print("\nError: file not found.  Please try again.")
            file_open = input("Enter a file name: ")
            file_open_a = file_open + ".csv"
    file_open_a = open(file_open_a, "r")        
    return file_open_a

#function to detect floats   
def make_float(s):
    ''' Docstring '''
    try : 
        s = float(s)
    except ValueError :
        s = -1
    return s
def get_density(mass, radius):
    ''' Docstring '''
    if mass < 0 or radius<=0 :
        density = -1
    else: 
        mass *= 5.972E+24 
        radius *= 6.371E+6
        volume =  (4/3) * math.pi * radius**3
        density = mass/ volume
    return density    

#function to estimate plant's temperature and check if in habitable range
def temp_in_range(axis, star_temp, star_radius, albedo, low_bound, upp_bound):
    ''' Docstring '''
    if axis < 0 or star_temp < 0 or star_radius < 0 or albedo < 0:
        ans = False
    else :
      star_radius *= SOLAR_RADIUS
      axis *= AU
      planet_temp = star_temp * ((star_radius / (2*axis))**0.5) * ((1-albedo)**0.25) 

      if low_bound <= planet_temp <= upp_bound:
          ans = True
      else :
          ans =  False
    return ans

#function for the farthest distance from earth
def get_dist_range():
    ''' Docstring '''
    distance =input("\nEnter maximum distance from Earth (light years): ")
    while True:
        try:
            distance_float = float(distance)
            if distance_float < 0:
                print("\nError: Distance needs to be greater than 0.")
                distance = input("\nEnter maximum distance from Earth (light years): ")
            else: 
                return distance_float
        except:
            print("\nError: Distance needs to be a float.")
            distance = input("\nEnter maximum distance from Earth (light years): ")
        
   

#main funtion which houses the interaction with the user
def main():
         
    print('''Welcome to program that finds nearby exoplanets '''\
          '''in circumstellar habitable zone.''')

    #variables
    max_stars = 0
    max_planets = 0
    total_mass = 0
    
    
    num_mass = 0
    in_circumstellar = 0
    num_rocky_planets = 0
    num_gaseous_planets = 0

    #min(max) algorithm 
    min_distane_rocky = 9999
    min_distance_gaseous = 9999
    
    
    closest_rocky_planet = ""
    closest_gaseous_planet = ""
    


    #  open an input file for reading
    file_open = open_file()
    file_open.readline()

    # dist_range funtion called
    dist_range = get_dist_range()

    # variables
    low_bound = 200
    upp_bound = 350
    albedo = 0.5

    #looking through the file line by line
    for line in file_open:

        #  Read the distance
        float_range = make_float(line[114:])
        if (float_range*PARSEC_LY) > dist_range or float_range < 0:
            continue
        
        
        axis = make_float(line[66:77])
        planet_radius = make_float(line[78:85])
        star_temp = make_float(line[97:105])
        star_radius = make_float(line[106:113])

        # evaluating max number of planets and stars
        planet_name = str(line[:25])
        planet_name = planet_name.strip()
        
        num_stars_system = int(line[50:57])
        if num_stars_system > max_stars:
            max_stars = num_stars_system
            
        num_of_planets = int(line[58:65])
        if num_of_planets > max_planets:
            max_planets = num_of_planets
        
        #  finding total mass of planets
        planet_mass = make_float(line[86:96])
        if planet_mass > 0:
            total_mass += planet_mass
            num_mass += 1 
        
       
        density_rho = get_density(planet_mass, planet_radius)

        #   to determine if planet is habitable
        if temp_in_range(axis, star_temp, star_radius, albedo, low_bound, upp_bound) == True:
            in_circumstellar += 1
            
            if ((0 < planet_mass < 10) or (0 < planet_radius < 1.5)) or (density_rho > 2000):  #determine if rocky
                num_rocky_planets += 1
                if float_range < min_distane_rocky:
                    min_distane_rocky = float_range
                    closest_rocky_planet = planet_name
                    
            #gaseous 
            else:   
                num_gaseous_planets += 1
                if float_range < min_distance_gaseous:
                    min_distance_gaseous = float_range
                    closest_gaseous_planet = planet_name



    # closing file
    file_open.close()

    # printed outputs
    print("\nNumber of stars in systems with the most stars: {:d}.".format(max_stars))
    print("Number of planets in systems with the most planets: {:d}.".format(max_planets))
    print("Average mass of the planets: {:.2f} Earth masses.".format(total_mass/num_mass))
    print("Number of planets in circumstellar habitable zone: {:d}.".format(in_circumstellar))

    if num_rocky_planets > 0:
        print("Closest rocky planet in the circumstellar habitable zone {} is {:.2f} light years away.".format(closest_rocky_planet, min_distane_rocky*PARSEC_LY))
    else:  
        print("No rocky planet in circumstellar habitable zone.")

    if num_gaseous_planets > 0 :
        print("Closest gaseous planet in the circumstellar habitable zone {} is {:.2f} light years away.".format(closest_gaseous_planet, min_distance_gaseous*PARSEC_LY))
    else:
        print("No gaseous planet in circumstellar habitable zone.")  


if __name__ == "__main__":
    main()