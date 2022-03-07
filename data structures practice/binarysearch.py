
    #BINARY SEARCH
def binary_search(list, item):
    # FIRST ELEMENT 
    low = 0 
    # LAST ELEMENT
    high = len(list) - 1

    # STILL SEARCHING
    while low <= high:
    
    #CHECK MIDDLE ITEM
      mid = (low + high) // 2
      guess = list[mid]
      print("attempt")
    # IF ITEM MATCHES
      if guess == item:
        return mid
    # IF THE GUESS IS TOO HIGH
      if guess > item:
    # MOVES BACK ONE
        high = mid - 1 
      # IF THE GUESS IS TOO LOW
      else:
        low = mid + 1

    # ITEM NOT IN ARRAY
    return None

my_list = [1,2,3,4,5,6,7,8,9,10]

print(binary_search(my_list,8))