#!/usr/bin/env python

import math

def AskNum():
    number = input ("Enter number: ")
    print("\nThe number:",number, " is")
    if (int(number)%2) == 0:
        eo="even"
    else:
        eo="odd"
    print("\nThe number:",number, " is ", eo)

def AskSq():
    number = input ("Enter a number to Square: ")
    print(int(number) * int(number))

def DegFar():
    temp = input ("\n\nEnter a temperature in Fahrenheit : ")
    celsius = (int(temp) - 32) * (5/9)
    print ("is ","{:.2f}".format(celsius),"Celsius")

def retLargest():
    list_a = [34, 45,1,67,4,600,250,21,89,1001, 29, 39, 5]
    print ("The list   = ",list_a)
    list_a.sort()
    print("The sorted list = ",list_a)
    print("The largest number is = ",list_a[-1])

def Palin():
    list_a = ["Anna", "Civic","Kayak", "level", "Madam", "mom", "noon", "Racecar", "Radar",
              "Refer", "automobile", "rotor", "help", "school" ]
    #print ("\nString\tBackward\tPalinodrone?")
    print ("\nString", '{:<10}'.format("Backward"), '{:<10}'.format("Palinodrone?"))
    for x in list_a[:]:
        bkwd = x[::-1]
        if x.lower() == bkwd.lower():
            pal = "yes"
        else:
            pal = "no"
        print ('{:<10}'.format(x),'{:<10}'.format(bkwd),'{:<5}'.format(pal))

def VowelCount():
    vowels='aeiou'
    count=0
    string = ''.join([" Twinkle, twinkle, little star,\n",
                       "  How we wonder what you are.\n",
                       "  Up above the world so high,\n"
                       "  Like a diamond in the sky.\n",
                       "\n",
                       "  When the glorious sun has set,\n",
                       "  And the grass with dew is wet,\n",
                       "  Then you show your little light,\n",
                       "  Twinkle, twinkle, all the night.\n",
                       "\n",
                       "  When the golden sun doth rise,\n",
                       "  Fills with shining light the skies,\n",
                       "  Then you fade away from sight,\n",
                       "  Shine no more 'till comes the night."])
    for s in string:
        if s in vowels: count=count+1
    print("\n\n",string,"\n")
    print("There are ",count," vowels")

def DrawLine():
    print("\n\n. . . . . . . . . . . . . . . . . . .\n")

AskNum()
DrawLine()
AskSq()
DrawLine()
DegFar()
DrawLine()
retLargest()
DrawLine()
Palin()
DrawLine()
VowelCount()

