import random
class Arrays():

    #a
    @staticmethod
    def new_array(number_of_array_elements,value_of_array_elements):
        arr=[]
        for i in range(number_of_array_elements):
            arr.append(value_of_array_elements)
        return arr
    #b
    @staticmethod
    def new_array_random(number_of_array_elements,value_from,value_to):
        err=[]
        for j in range(number_of_array_elements):
            err.append(random.randint(value_from,value_to))
        return err
    #c

array1=Arrays.new_array(10,5)
print(array1)
array2=Arrays.new_array_random(10,1,5)
print(array2)
