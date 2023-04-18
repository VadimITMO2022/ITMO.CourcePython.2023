from math import radians, cos, sin, asin, sqrt
import zip_util

zip_codes = zip_util.read_zip_all()

#-----------------------------------------------------
#  a place corresponding to ZIP Code

def func_loc(zip_code):
   i=0
   valid = False
   while i < 42048:
     m = zip_codes[i]
     if(zip_code == m[0]):
       valid = True
       break
     i+=1
   if  valid:
     str1 = "Zip code " + m[0] + " is in " \
      + m[3] + ", " + m[4] + ", " \
      + m[5]+ " county,\n" + "coordinates: (" \
      + str(m[1]) + ", " + str(m[2]) + ")"
   else:
     str1 = "This ZIP Code is invalid. Please input the valid ZIP Code "
   return str1

#-----------------------------------------------------
#  ZIP Code(-s), corresponding to the city and state
def func_zip(city, state):
   city=city.lower()
   city=city.title()
   state = state.upper()
   valid = False
   str1 =" "
   i=0
   while i < 42048:
     m = zip_codes[i]
     if(city == m[3] and state == m[4]):
       valid = True
       str1 = str1 + ", " + m[0]
     i+=1

   if  valid:
       str1 = "The following ZIP Code(s) found for " \
              + city + ", " + state + ":" + str1
   else:
     str1 = "The name of city or state is invalid. Please input the correct information"
   return str1

#---------------------------------------------------------------
# the shortest distance between 2 points on the Earth associated with two ZIP codes
def func_zip_point(zip_code1,zip_code2):

# latitude and longitude of the 1st point associated with the 1st ZIP code

   valid1 = False
   i=0
   while i < 42048:
     m = zip_codes[i]
     if(zip_code1 == m[0]):
       valid1 = True
       break
     i+=1

   phi1 = m[1]
   lam1 = m[2]

# latitude and longitude of the 2nd point associated with the 2nd ZIP code

   valid2 = False
   j = 0
   while j < 42048:
     p = zip_codes[j]
     if (zip_code2 == p[0]):
       valid2 = True
       break
     j += 1

   phi2 = p[1]
   lam2 = p[2]

# The angles in radians
   phi1 = radians(phi1)
   lam1 = radians(lam1)
   phi2 = radians(phi2)
   lam2 = radians(lam2)

# The Earth's radius in kilometers.
   R_km = 6371
# The Earth's radius in miles.
   R_mi = 3958.8

# The "Haversine formula"
   D_phi = phi2 - phi1
   D_lam = lam2 - lam1
   P = sin(D_phi / 2) ** 2 + cos(phi1) * cos(phi2) * sin(D_lam / 2) ** 2
   dis = 2 * R_mi * asin(sqrt(P))

   if not valid1 or not valid2:
       str1 = "The ZIP Code is invalid. Please input the valid ZIP Code"
   else:
       str1 = 'The distance between ' + str(zip_code1) + \
       ' and ' + str(zip_code2) + ' is ' + str("{:.2f}".format(dis)) + ' miles'

# The distance between two points
#   dis=distance_d(phi1, lam1, phi2, lam2)
   return str1

#---------------------------------------------------------------
# the main part
while 1:
 stringg = input("\nВведите одну из команд 'loc', 'zip', 'dist', 'end' \n")

 if(stringg == "loc"):
   zip_code=input("Enter a Zip code to lookup \n")
   str1 = func_loc(zip_code)
   print(str1)
 elif(stringg == "zip"):
    city = input("Enter a city name to lookup \n")
    state = input("Enter a state name to lookup \n")
    str1 = func_zip(city, state)
    print(str1)
 elif (stringg == "dist"):
    zip_code1 = input("Enter the first ZIP Code \n")
    zip_code2 = input("Enter the second ZIP Code \n")
    str1 = func_zip_point(zip_code1,zip_code2)
    print(str1)
 elif(stringg == "end"):
   break
 else:
     print("Invalid command")



