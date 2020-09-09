#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 11:37:43 2020

@author: kabram
"""
practicum = int(input('What problem do you want to show?\n'))

if practicum == 1:
    full_name = input('What is your full name (First & Last)?\n')
    first = full_name.split(' ')[0]; last = full_name.split(' ')[-1]
    height_in = float(input('What is your height in inches?\n')); height_cm = height_in * 2.54
    weight_lbs = float(input('What is your weight in pounds?\n')); weight_kg = weight_lbs * 0.45359237
    bmi = weight_kg / ((height_cm / 100)**2)
    print('\nFirst name:\t' + first + '\n' + 'Last name:\t' + last + '\n' + 'Your height is:\t' + str(height_cm) + ' cm\n' + 'Your weight is:\t' + str(weight_kg) + ' kg\n' + 'Your BMI is:\t' + str(bmi))

if practicum == 2:
    # ask input; create empty list; set counter
    number_of_ints = int(input('How many numbers?\n')); list_numbers = []; i = 1
    # loop for specified entry count
    while i <= number_of_ints:
        loop_input = input('What is number %s value?\n' % str(i))
        list_numbers.append(int(loop_input)); i+=1
    # evals for order of list
    if list_numbers == sorted(list_numbers):
        print('\nAscending Order')
    if list_numbers == sorted(list_numbers, reverse = True):
        print('\nDesending Order')
    if list_numbers != sorted(list_numbers) and list_numbers != sorted(list_numbers, reverse = True):
        print('\nNo Order')