
# FINDS SMALLEST VALUE
def findSmallest(arr):
  # STORES VALUE 
  smallest = arr[0]
  # STORES INDEX
  smallest_index = 0
  for i in range(1, len(arr)):
    if arr[i] < smallest:
      smallest_index = i
      smallest = arr[i]      
  return smallest_index

# SORTS ARRAY IN NEW ARRAY
def selectionSort(arr):
  newArr = []
  for i in range(len(arr)):
      # GETS SMALLES AND ADDS TO NEW ARRAY
      smallest = findSmallest(arr)
      newArr.append(arr.pop(smallest))
  return newArr

print(selectionSort([5, 3, 6, 2, 10]))