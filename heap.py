#!/usr/bin/python3
# -*- coding: utf-8 -*-
import math
#A = [4,1,3,2,16,9,10,14,8,7]
#A = [1,2,3,4,5,6,7,8,9,10]
#A = [10,9,8,7,6,5,4,3,2,1]

heap_low = [0]
heap_high = [0]


def parent(A, x):
    return ((A.index(x))//2)


def right(A, x):
    return (A.index(x)*2)


def left(A, x):
    return (A.index(x)*2+1)

def min_heapify(A,x):
    if len(A)>=2:
        #print(A[x])
        l = left(A, A[x])
        r = right(A, A[x])
        if l<=len(A)-1 and A[l]<A[x]:
            largest = l
        else:
            largest = x
        if r<=len(A)-1 and A[r]<A[largest]:
            largest = r
        if largest != x:
            A[x], A[largest] = A[largest], A[x]
            min_heapify(A, largest)
    return A

def max_heapify(A,x):
    if len(A)>=2:
        l = left(A, A[x])
        r = right(A, A[x])
        if l<=len(A)-1 and A[l]>A[x]:
            largest = l
        else:
            largest = x
        if r<=len(A)-1 and A[r]>A[largest]:
            largest = r
        if largest != x:
            A[x], A[largest] = A[largest], A[x]
            max_heapify(A, largest)
    return A

def build_max_heapify(A):
    for i in range(((len(A)-1)//2),0,-1):
        min_heapify(A,i)
    return A

def build_min_heapify(A):
    for i in range(((len(A)-1)//2),0,-1):
        max_heapify(A,i)
    return A

def add_elemen_low(heap_low, x):
    heap_low.append(x)
    heap_low = build_min_heapify(heap_low)

def add_elemen_high(heap_high, x):
    heap_high.append(x)
    heap_high = build_max_heapify(heap_high)

def read_file(path):
    A = []
    with open(path, "r") as file:
        for line in file:
            A.append(int(line.replace("\n","")))
    return A

if __name__ == '__main__':
    A = read_file("input_16_10000.txt")
    for i in range(1,2016):
        if len(heap_low) == 0 or A[i]<max(heap_low):
            add_elemen_low(heap_low,A[i])
        else:
            add_elemen_high(heap_high,A[i])
        if math.fabs(len(heap_low)-len(heap_high))>1:
            if len(heap_low)>len(heap_high):
                x = heap_low[1]
                heap_low[1]=heap_low[len(heap_low)-1]
                heap_low = heap_low[:len(heap_low)-1]
                heap_low = max_heapify(heap_low,1)
                add_elemen_high(heap_high,x)
            elif len(heap_low)<len(heap_high):
                x = heap_high[1]
                heap_high[1]=heap_high[len(heap_high)-1]
                heap_high = heap_high[:len(heap_high)-1]
                heap_high = build_max_heapify(heap_high)
                add_elemen_low(heap_low,x)
        if (i-1)%2 != 0:
            print (i,"|", heap_low[1], heap_high[1])
        else:
            if len(heap_low)>len(heap_high):
                print (i,"|", heap_low[1])
            else:
                print (i,"|", heap_high[1])
        print ("heap_low:", heap_low[1:])
        print ("heap_high:", heap_high[1:])
