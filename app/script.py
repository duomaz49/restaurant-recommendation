from utils import ascii_chef, welcome, instruction1, question1, retry, line, chef_tomas_restaurants, yes_or_no, end, print_restaurants, \
    print_matches
from data import cuisines, restaurant_data

print(ascii_chef)
print(welcome)
print(instruction1)

quit = False

while not quit:
    print(question1)
    answer = str(input().strip()).lower()
    matches = [c for c in cuisines if c.startswith(answer)]

    if answer == "q":
        print(end)
        break

    if matches:
        if len(matches) == 1:
            match = matches[0]
            print(f"The only matching word is {match.capitalize()}")
            print(f"Do you want to look at {match.capitalize()}? {yes_or_no}")
            y_or_n = str(input().strip()).lower()

            if y_or_n == 'y':
                print_restaurants(match, restaurant_data)
                print(f"Do you want to find another restaurant? {yes_or_no}")
                y_or_n = str(input().strip()).lower()
                if y_or_n == 'y':
                    continue
                else:
                    print(end)
                break
        else:
            while True:
                print("Chef Tomas found multiple matches:")
                print_matches(matches)
                print("Please try to search with one of the above words")
                option = str(input().strip()).lower()
                if option == "q":
                    print(end)
                    break
                if option in matches:
                    print_restaurants(option, restaurant_data)
                    print(f"Do you want to find another restaurant? {yes_or_no}")
                    y_or_n = str(input().strip()).lower()
                    if y_or_n == 'y':
                        continue
                    else:
                        print(end)
                        quit = True
                        break
                else:
                    print("Please input one of the options... or press 'q' to exit")
                    print_matches(matches)
    else:
        print(retry)
