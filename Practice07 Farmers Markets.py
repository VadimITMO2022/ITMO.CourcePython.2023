import csv
from math import radians, cos, sin, asin, sqrt
import zip_util

zip_codes = zip_util.read_zip_all()

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
       str1 = m[0]
       break
     i+=1

   if valid is False:
      print("The name of city or state is invalid. Please input the correct information")

   return str1

#---------------------------------------------------------------
# last of all farmers markets exported from 'Export.csv' with a 'number' markets per page

def  func_all(number):

 with open('Export.csv', newline='') as f:
    reader = csv.reader(f)
    i = 0
    for row in reader:
       print(row)
       i = i + 1
       if i % int(number) == 0:
             input('Чтобы продолжить, нажмите любую клавишу')


#---------------------------------------------------------------
# the shortest distance between 2 points on the Earth associated with two ZIP codes
def func_zip_point(zip_code1, zip_code2):

# latitude and longitude of the 1st point associated with the 1st ZIP code

   valid1 = False
   i=0
   while i < 42048:
     m = zip_codes[i]
     if(zip_code1 == m[0]):
       valid1 = True
       break
     i+=1

#   if valid1 is False:
#      print("The ZIP code is invalid. Please input the correct information")


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

#   if valid2 is False:
#      print("The ZIP code is invalid. Please input the correct information")

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

   return dis


#---------------------------------------------------------------
# the list of ZIP codes within distance 'distance' from 'zip_code'
def func_zip_dist(zip_code, distance):
   dist_dist = []

# calculation index 'i' corresponding to ZIP 'zip_code'
   i = 0
   while i < 42048:
        m = zip_codes[i]
        zip_code1 = m[0]
        if zip_code == zip_code1:
            break
        i += 1

# calculation  indexes 'i0' and 'i1'  [i0;i1]
   i0 = i - 300
   i1 = i + 300

   if i0 < 0:
       i0 = 0
   if i1 > 42048:
       i1 = 42048

# array 'dist_dist' contains zip-codes within distance 'dist'
# from 'zip_code'

   j = i0
   while j < i1 + 1:
     m = zip_codes[j]
     zip_code1 = m[0]
     dis = func_zip_point(zip_code1, zip_code)
     if dis < int(distance):
        dist_dist.append(zip_code1)
     j += 1

   return dist_dist

#---------------------------------------------------------------
# list of farmer's markets for given ZIP 'zip-code' and a distance
def func_zip_list(zip_code, distance):
# calculation array 'dist-dist' containing
# ZIP codes within the distance 'distance' from 'zip_code'
  dist_dist = func_zip_dist(zip_code, distance)
# print Farmers Markets with ZIP codes within 'distance' from 'zip_code'
  with open('Export.csv', newline='') as f:
   reader = csv.reader(f)
   for row in reader:
       j=0
       while j < len(dist_dist):
          if(dist_dist[j] == row[11]):
             print(row)
          j += 1

#---------------------------------------------------------------
# list of farmer's markets for given city, state and a distance
def func_zip_town(city, state, distance):
# ZIP code for given city and state
    zip_code=func_zip(city, state)
# list of farmer's markets for given ZIP-code and a distance
    func_zip_list(zip_code, distance)

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------

# main part

while 1:
 stringg = input("\nEnter one of the commands  'all', 'zip', 'town', 'end' \n")

 if(stringg == "all"):
   number=input("Enter a number of records per page \n")
   func_all(number)
 elif (stringg == "zip"):
   zip_code = input("Enter ZIP Code \n")
   distance = input("Enter distance (miles)\n")
   func_zip_list(zip_code, distance)
 elif(stringg == "town"):
    city = input("Enter a city name to lookup \n")
    state = input("Enter a state name to lookup \n")
    distance = input("Enter distance (miles)\n")
    func_zip_town(city, state, distance)
 elif(stringg == "end"):
   break
 else:
     print("Invalid command")



