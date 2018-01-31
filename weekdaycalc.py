
baseline_y = 2017
baseline_m = 12
baseline_d = 31
baseline_weekday = 7  #7=Sunday

day = input("Which day? ")
month = input("Which month? ")
year = input("Which year? ")

         

   ###################       


#is target year leap?

def isleapyear(y):
     if ((y % 4 == 0) and (y % 100 != 0)) or (y % 400 == 0):
          return True
     
     else:
          return False

#daynum in targetyear:

def leap_numberofday(m,d):
     leap_year_vec=[31,29,31,30,31,30,31,31,30,31,30,31] #day 1-366
     index_m=0
     daynum = 0
     while index_m < (m-1): #changed -2 to -1
          daynum = daynum + leap_year_vec[index_m]
          index_m = index_m + 1
     #should have daynumber from day 1 to last day of month before target
     fulldaynum = daynum + d
     return fulldaynum

def unleap_numberofday(m,d):
     unleap_year_vec=[31,28,31,30,31,30,31,31,30,31,30,31] #day 1-365
     index_m=0
     daynum = 0
     while index_m < (m-1): #changed -2 to -1
          daynum = daynum + unleap_year_vec[index_m]
          index_m = index_m + 1
     #should have daynumber from day 1 to last day of month before target
     fulldaynum = daynum + d
     return fulldaynum



#calc daynum between targetyear and baseline(date):
def days_between_targetdate_and_baseline(d,m,y):
     
     if y > 2017: #don't count days in 2017, add days in targetyear before target
          print "Target year is after 2017"
          daycount=0
          y=y-1 #so we don't add full yeardays from targetyear yet
          while y > 2017:
               if isleapyear(y):
                    daycount = daycount+366
                    print str(y) + " is leap"
               else:
                    daycount = daycount+365
                    print str(y) + " is not leap"
               y = y-1
               
          print "Days between the end of 2017 and the beginning of target year are: " + str(daycount)
          
          if isleapyear(y):
               daycount = daycount+leap_numberofday(m,d)
               print "Target year is a leap year and target day is day " + str(leap_numberofday(m,d)) + " in its year."
          else:
               daycount = daycount+unleap_numberofday(m,d)
               print "Target year is not a leap year and target day is day " + str(unleap_numberofday(m,d)) + " in its year."
 
          return daycount

     

     elif y < 2017: #add days in 2017, add days in targetyear after target
          daycount=0
          y=y+1 #so we don't add full targetyear (instead just "restdays")
          while y <= 2017:
               if isleapyear(y):
                    daycount = daycount+366
                    print str(y) + " is leap"
               else:
                    daycount = daycount+365
                    print str(y) + " is not leap"
               y = y+1

          if isleapyear(y):
               daycount = daycount+(366-leap_numberofday(m,d))
               print "Target year is a leap year and target day is day " + str(leap_numberofday(m,d)) + " in its year."

          else:
               daycount = daycount+(365-unleap_numberofday(m,d))
               print "Target year is a leap year and target day is day " + str(leap_numberofday(m,d)) + " in its year."
               
          return daycount

     
               
     else: #add difference in days in 2017 (must be before target or target itself)
          print "Target year is 2017"
          
          if m==12 and d==31:
               return 0 #it's the target itself -> sun
          
          else: #it's before the target
               unleap_year_vec=[31,28,31,30,31,30,31,31,30,31,30,31]
               daycount=unleap_year_vec[m-1]-d #days from target to month-end

               if m!=12: #if month isn't december, add restmonths between 
                    index_m=11
                    while index_m > (m-1):
                         daycount = daycount + unleap_year_vec[index_m]
                         index_m= index_m-1
          
               print str(daycount)+" days between "+str(d)+"/"+str(m)+"/"+str(y)+" and 31/12/2017."
               return daycount


#finalcalc: fulldaynum between target and baseline (difference) and weekdaycalc

def weekdaycalc(d,m,y):

     if y > 2017: #sunday + daycountstuffmod
          weekday=(7+days_between_targetdate_and_baseline(d,m,y))%7
          print "From Sunday, 31/12/2017 to "+ str(d)+"/"+str(m)+"/"+str(y)+", we add "+ str(days_between_targetdate_and_baseline(d,m,y)) + " days."

     else: #sunday - daycountstuffmod
          weekday=7-(days_between_targetdate_and_baseline(d,m,y)%7)
          print "From Sunday, 31/12/2017 to "+ str(d)+"/"+str(m)+"/"+str(y)+", we subtract "+ str(days_between_targetdate_and_baseline(d,m,y)) + " days."

     print "It's day " + str(weekday) + " of the week."
     return weekday


def translatetoweekday(n):
     weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
     return weekdays[n-1]

n = weekdaycalc(day, month, year)
print translatetoweekday(n)






