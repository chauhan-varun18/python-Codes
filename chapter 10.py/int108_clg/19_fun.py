cities = ["Noida","Spn","Delhi", "Jalandhar"]
heroes = ["ironman","Thor" , "Shaktiman"]

print(cities[0] , end=" ")
print(heroes[2])   # end=" " ek hi line m likhne k liye

# def print_len(list):
#     print(len(list))

# print_len(cities)
# print_len(heroes)

def print_list (list):
    for iteam in list :
        print(iteam, end=" ")

print_list(cities)
