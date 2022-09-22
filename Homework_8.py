'''
Importing functions datetime,timedelta and date from datetime
'''
from datetime import datetime,timedelta,date
'''
Below is some example list
'''
example_list=[{"name":"Bill","birthday":datetime(1993, 9, 24)},
      {"name":"John","birthday":datetime(1998, 9, 24)},
      {"name":"Caleb","birthday":datetime(1997, 9, 28)},
      {"name":"Daniel","birthday":datetime(1985, 9, 25)},
      {"name":"Sergii","birthday":datetime(1983, 10, 1)},
      {"name":"Myke","birthday":datetime(1984, 9, 27)},
      {"name":"Konstantin","birthday":datetime(1997, 9, 29)}
      ]
'''
Creating function, which will take some_list with dictionaries
Dictionaries has keys "name" and "birthday"
Name is string format. Birthday is datetime format
'''
def get_birthdays_per_week(some_list):
    '''
    Creating empty list and finding next monday
    '''
    lst=[]
    today= date.today()
    days_ahead = 0 - today.weekday()
    if days_ahead <= 0: # Target day already happened this week
         days_ahead += 7
    new_monday = today + timedelta(days_ahead)
    '''
    Creating new dictionary with keys as date from next monday and values as empty lists
    '''
    new_dict={new_monday.strftime('%A %d %B %Y'):[],
              (new_monday+timedelta(days=1)).strftime('%A %d %B %Y'):[],
              (new_monday+timedelta(days=2)).strftime('%A %d %B %Y'):[],
              (new_monday+timedelta(days=3)).strftime('%A %d %B %Y'):[],
              (new_monday+timedelta(days=4)).strftime('%A %d %B %Y'):[],
              (new_monday+timedelta(days=5)).strftime('%A %d %B %Y'):[],
              (new_monday+timedelta(days=6)).strftime('%A %d %B %Y'):[],
              (new_monday+timedelta(days=7)).strftime('%A %d %B %Y'):[]
              }
    '''
    Now we parce through list of dictionaries.
    When key "birthday" found, year of value replaced with current year
    After we check if we have birthdays on Saturday and Sunday 
    If yes we add string to Monday
    '''
    for diction in some_list:
        for key,value in diction.items():
            if key=="birthday":
                diction["birthday"]=value.replace(year=today.year)
                if diction["birthday"].date()==new_monday-timedelta(days=2):
                    list(new_dict.values())[0].append(str(diction["name"]) + " birthday was on Saturday") 
                if diction["birthday"].date()==new_monday-timedelta(days=1):
                    list(new_dict.values())[0].append(str(diction["name"]) + " birthday was on Sunday")  
                if diction["birthday"].strftime('%A %d %B %Y') in new_dict:
                    new_dict[diction["birthday"].strftime('%A %d %B %Y')].append(diction["name"])
    '''
    Now we will add items from dictionary to list
    If is used to check if any value is empty or not.
    Code below is used for user friendly interface
    '''
    i=0
    while i!=8:
        if len(list(new_dict.values())[i])>=1:
            lst.append(f"{list(new_dict)[i]}: {', '.join(list(new_dict.values())[i])}\n")
        else:
            lst.append(f"{list(new_dict)[i]}:\n")
        i+=1
    '''
    Now we can show result in console
    '''
    print("".join(lst))

get_birthdays_per_week(example_list)
