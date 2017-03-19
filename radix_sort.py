#!/usr/bin/python3
# -*- coding: utf-8 -*-

def countig_sort(mass,d):
    n = len(mass)
    k = 26
    count = []
    new_mass = []
    for i in range(0,k):
        count.append(0)
    for i in range(0,n):
        number = ord(mass[i][d:d+1]) - 97
        count[number] += 1
        new_mass.append(0)
    for i in range(1,k):
        count[i] += count[i-1]
    for i in range (n-1,-1,-1):
        number = ord(mass[i][d:d+1]) - 97
        count[number] -= 1
        new_mass[count[number]] = mass[i]
    return new_mass

def radix_sort(mass):
    for i in range(2,-1,-1):
        mass = countig_sort(mass,i)
    return mass

def read_file(path):
    mass = []
    with open(path, "r") as file:
        for line in file:
            mass.append(line.replace("\n",""))
    return mass

if __name__ == '__main__':
    path = "anagrams.txt"
    mass = radix_sort(read_file(path))
    print (mass)
