#    CS 2302 Data Structures
#    Professor Diego Aguirre
#    TA  Anindita Nath
#    Lab 5 option B
#    11/27/2018 by Edgar Escobedo 80502432

#In order to complete this lab we were asked to implement the Min-Heap data structure and use it to do the heapsort, we would do it by
#appending each new number to the heap, and going through min heap each time an element is inserted in order to maintain its
#Min-Heap structure. Then for the part of the extract min, I will take the value at the index 0 (minimum value) which I will return
#and change the value of the index 0, to the last value of the heap, lastly shrink by 1 the heap. Further explanation will be given
#with the methods


class Heap:
    def __init__(self):
        self.heap_array = []


    #Insertion of the new value and usage of the min heap with this new value to maintain the Min-Heap properties
    def insert(self, val):
        self.heap_array.append(val)
        self.min_heap()


    #Two base cases, if length of the heap is 1, it is already a min heap so just return, the second method will work for any size
    #by checking all the indices, starting from the last one to its parent, being index -1 // 2. If the parent is greater than the
    #index, we will swap them
    def min_heap(self):
        if len(self.heap_array) is 1:
            return self
        last_element = len(self.heap_array) - 1
        while last_element is not 0:
            parent = (last_element - 1) // 2
            if self.heap_array[last_element] < self.heap_array[parent]:
                tmp = self.heap_array[last_element]
                self.heap_array[last_element] = self.heap_array[parent]
                self.heap_array[parent] = tmp
            last_element -= 1
        return self


    #Extract_min will take the value at the first index, call min heap to main its properties, shrink the heap by 1 and
    #return that value
    def extract_min(self):
        if self.is_empty():
            return None
        minimum_number = self.heap_array[0]
        self.heap_array[0] = self.heap_array[len(self.heap_array) - 1]
        del self.heap_array[-1]
        if len(self.heap_array) is 0:
            return minimum_number
        self.min_heap()
        return minimum_number

    #Regular print if needed
    def print(self):
        count = 0
        while count < len(self.heap_array):
            print(self.heap_array[count])
            count +=1

    #Check if the heap is empty
    def is_empty(self):
        for num in self.heap_array:
            if num is not None:
                return False
        return True

a = Heap ()

#In following lines the user will be asked the name of the file, the values of the files will be enter to the heap
#and the sorted list will be shown


print("Welcome to the heap master program")
file_name = input("Please select the name of the file you want to use\n")
print("In the next lines you will see the numbers gotten from your file in the sequence they were introduced\n")
with open(file_name+".txt") as f:
    passwords_list = f.read().splitlines()
counter = 0
while (counter != len(passwords_list)):
    list_x = passwords_list[counter]
    wrds = list_x.split(",")
    counter2 = 0
    show_line = []
    while (counter2 != len(wrds)):
        wrds[counter2] = wrds[counter2].replace(" ", "")
        if wrds[counter2] is not "":
            a.insert(int(wrds[counter2]))
            show_line.append(int(wrds[counter2]))
        counter2 += 1
    print(show_line)
    counter +=1

ordered_list = []
print("\nNow by using min heap we will sort the list and show it in its sorted form")
print("+\n++\n+++\n++++")
while a.is_empty() is not True:
    x = a.extract_min()
    ordered_list.append(x)
print(ordered_list)
print("++++\n+++\n++\n+")
print("\n             Thank you")

