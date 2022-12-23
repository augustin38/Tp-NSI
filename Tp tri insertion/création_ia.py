from random import randint

def rdm():
  return [randint(0, 100) for a in range(randint(5, 10))]

  
def echange(ind1):
  aux = liste[ind1]
  liste[ind1] = liste[ind1+1]
  liste[ind1+1] = aux

  
def insertion_sort(arr):
    # Iterate through the elements of the list
    for i in range(1, len(arr)):
        # Save the value of the current element
        current_value = arr[i]
        # Initialize the position at which we will insert the current element
        position = i
        # Shift all the elements that are greater than the current element one position to the right
        while position > 0 and arr[position - 1] > current_value:
            arr[position] = arr[position - 1]
            position -= 1
        # Insert the current element into its proper position
        arr[position] = current_value
    return arr

liste = rdm()
print(liste)
liste = insertion_sort(liste)
print(liste)
