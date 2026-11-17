ascii_chef = r'''
                            _          _
                           (c)___c____(c)
                            \ ........../
                             |.........|
                              |.......|
                              |.......|
                              |=======|
                              |=======|
                             __o)""""::?
                            C__    c)::;
                               >--   ::     /\
                               (____/      /__\
                               } /""|      |##|
                    __/       (|V ^ )\     |##|
                    o | _____/ |#/ / |     |##|
           @        o_|}|_____/|/ /  |     |##|
                          _____/ /   |     ~!!~
              ======ooo}{|______)#   |     /`'\
          ~~~~ ;    ;          ###---|8     ""
        ____;_____;____        ###====     /:|\
       (///0///@///@///)       ###@@@@|
       |~~~~~~~~~~~~~~~|       ###@@@@|
        \             /        ###@@@@|               +
         \___________/         ###xxxxx      /\      //
           H H   H  H          ###|| |      /  \    //
           H H   H  H           | || |     /____\  /~_^_
           H H   H  H           C |C |     _|@@|_ /__|#|_
           H H   H  H            || ||    /_|@@|_/___|#|/|
 v    \/   H(o) (o) H            || ::   |:::::::::::::|#|
 ~    ~~  (o)      (o)        Ccc__)__)  |ROMAN CANDLES|#|
  \|/      ~   @* & ~                    |:::::::::::::|/  \|/
   ~           \|/        !!        \ !/  ~~~~~~~~~~~~~    ~~~
               ~~~        ~~         ~~           ~~
'''

welcome = r'''
-----------------------------------------------------------------
*                                                               *
*                                                               *
*             Welcome to Chef Tomas Recommendation              *
*                                                               *
*                                                               *
-----------------------------------------------------------------
'''

instruction1 = 'What type of cuisine would you like to explore today? (e.g., Italian, Chinese, Mexican, etc.)'
question1 = 'Please enter your choice of cuisine: '
retry = "Sorry, we did not find matching cuisine. Please try again with a different search word. Press q to exit"
line = "---------------------------------------------"
chef_tomas_restaurants = "The restaurants that Chef Tomas recommends ARE....."
end = "Bye bye!"
yes_or_no = "Enter y for 'yes', n for 'no'"

def print_restaurants(match, restaurant_data):
    print(chef_tomas_restaurants)
    print(line)
    for elm in restaurant_data:
        if match in elm['cuisine']:
            print(f'''
              Name: {elm['name']}
              Price: {elm['price']}
              Rating: {elm['rating']}
              Address: {elm['address']}
              ''')
            print(line)

def print_matches(matches):
    for m in matches:
        print(m.capitalize())