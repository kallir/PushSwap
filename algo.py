import sys
import math

#variables global
operations = ""
special = False

##
# FONCTIONS PUSH SWAP
##
#sa sb
def swap(list, name):
    if not list:
        return

    n = "s" + name[-1]
    global operations
    temp = list[0]
    list[0] = list[1]
    list[1] = temp

    if not operations:
        operations += n
    else:
        operations += " " + n
    return list

def sc(la, lb):
    swap(la, "la")
    swap(lb, "lb")

#pa pb
def push(first, second, name):
    if not first:
        return
    
    n = "p" + name[-1]
    global operations
    second.insert(0 , first[0])
    first.pop(0)

    if not operations:
        operations += n
    else:
        operations += " " + n

    return first, second

# ra rb
def rotate(list, name):
    global operations
    n = "r" + name[-1]
    list.append(list[0])
    list.pop(0)

    if not operations:
        operations += n
    else:
        operations += " " + n
    return list

def rr(la, lb):
    rotate(la, "la")
    rotate(lb, "lb")

# rra rrb 
def rotate_last(list, name):
    global operations
    n = "rr" + name[-1]
    if not operations:
        operations += n
    else:
        operations += " " + n
    list.insert(0, list[len(list) -1])
    list.pop(len(list) -1)
    return list

def rrr(la, lb):
    rotate_last(la, "la")
    rotate_last(lb, "lb")
##
# FIN DES FONCTIONS PUSH SWAP
##

##
# APPEL D'ALGO
##

def algo(la, lb = []):
    if all(la[i] <= la[i+1] for i in range(len(la)-1)):
        return

    while not all(la[i] <= la[i+1] for i in range(len(la)-1)):
        while len(la) > 1:
            if la[0] < la[1]:
                push(la, lb, "lb")
            else:
                swap(la, "la")
                push(la, lb, "lb")
        while len(lb) > 0:
            push(lb, la, "la")

    print(operations)
    if special:
        prompt = input('Order another list ? (y/n) ')
        prompt = prompt.strip()
        if prompt == "y" or prompt == "yes" or prompt == "Y" or prompt == "Yes":
            init()
        else:
            print("Bye !")        

def init(args = []):
    global operations
    global special 
    operations = ""
    if args == [] or args[-1] == "-s":
        special = True
        num_input = input('Enter a list of integers separated by spaces: ')
        nums = [int(num) for num in num_input.split()]
    else:
        args.pop(0)
        nums = [int(num) for num in args]
    algo(nums, [])

init(sys.argv)