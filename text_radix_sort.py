#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Only for text without space and other symbols (number, dot, comma etc)

def countig_sort(mass,k,d):
    n = len(mass)
    count = [0] * k
    new_mass = [0] * n
    for i in range(0,n):
        lens = len(mass[i])
        if d>=lens:
            number = ord(mass[i][lens-1:lens]) - 97
        else:
            number = ord(mass[i][d:d+1]) - 97
        count[number] += 1
    for i in range(1,k):
        count[i] += count[i-1]
    for i in range (n-1,-1,-1):
        lens = len(mass[i])
        if d>=lens:
            number = ord(mass[i][lens-1:lens]) - 97
        else:
            number = ord(mass[i][d:d+1]) - 97
        count[number] -= 1
        new_mass[count[number]] = mass[i]
    return new_mass

def radix_sort(mass,k):
    max_len = len(max(mass, key=len))
    for i in range(max_len - 1,-1,-1):
        mass = countig_sort(mass,k,i)
    return mass

def read_file(path):
    mass = []
    with open(path, "r") as file:
        for line in file:
            mass.append(line.replace("\n",""))
    return mass

if __name__ == '__main__':
    k = 26
    path = "anagrams.txt"
    mass = radix_sort(read_file(path), k)
    print (mass)
