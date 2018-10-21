import os

#directories =  []
#for directory in os.walk ():
 #   directory.append(directory)
 #   print(directory)

directories = [directories [2] for directory in os.walk("C:\ Users\Pablo\PycharmProjects")]
directories = filter(lambda Item: list.count(Item),directories)
for directory in directories:
    print(directory)

