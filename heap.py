#!/usr/bin/python3
# -*- coding: utf-8 -*-
import math
A = [1,2,3,4,5,6,7,8,9,10]
#A = [10,9,8,7,6,5,4,3,2,1]
heap_low = []
heap_high = []


def parent(A, x):
    try:
        if (A.index(x)-1)<0:
            parent = None
        else:
            parent = A[(A.index(x)-1)//2]
    except IndexError:
        parent = None
    return parent

def right(A, x):
    return (A.index(x)*2)
    #try:
    #    right = A[A.index(x)*2+2]
    #except IndexError:
    #    right = None
    #return right

def left(A, x):
    return (A.index(x)*2)
    #try:
    #    left = A[A.index(x)*2+1]
    #except IndexError:
    #    left = None
    #return left

def add_elemen_low(heap_low, x):
    check = False
    for element in heap_low:
        if x>element:
            heap_low.insert(heap_low.index(element),x)
            check = True
            break
    if check == False:
        heap_low.append(x)
    max_heapify(heap_low,0)

def add_elemen_high(heap_high, x):
    check = False
    for i in range(1,len(heap_high)):
        element = heap_high[i]
        if x<element:
            heap_high.insert(heap_high.index(element),x)
            check = True
            break
    if check == False:
        heap_high.append(x)
    max_heapify(heap_high,0)

def max_heapify(A,x):
    #print (A[x],x)
    if len(A)>=3:
        #x = A.index(x)

        l = left(A, A[x])
        r = right(A, A[x])
        print (l, r, x, A)
        if l<=len(A) and A[l]>A[x]:
            largest = l
        else:
            largest = x
        if r<=len(A) and A[r]>A[largest]:
            largest = r
        #print largest
        if largest != x:
            A[x], A[largest] = A[largest], A[x]
            max_heapify(A, largest)

if __name__ == '__main__':
    for i in range(0,10):
        #find where add new element
        if len(heap_low)== 0:
            add_elemen_low(heap_low,A[i])
        elif A[i]<heap_low[0]:
            add_elemen_low(heap_low,A[i])
        else:
            add_elemen_high(heap_high,A[i])

        if math.fabs(len(heap_low)-len(heap_high))>1:
            if len(heap_low)>len(heap_high):
                x = heap_low[0]
                heap_low.remove(x)
                max_heapify(heap_low,0)
                add_elemen_high(heap_high,x)

            elif len(heap_low)<len(heap_high):
                x = heap_high[0]
                max_heapify(heap_high,0)
                heap_high.remove(x)
                add_elemen_low(heap_low,x)
        if i%2 != 0:
            print (i,"|", heap_low[0], heap_high[0])
        else:
            if len(heap_low)>len(heap_high):
                print (i,"|", heap_low[0])
            else:
                print (i,"|", heap_high[0])
        print ("heap_low:", heap_low)
        print ("heap_high:", heap_high)
    #print (heap_low, heap_high)
