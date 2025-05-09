#!/usr/bin/env python3

import sys
import io
  





class TestHappyNewYear:
    '''happy_new_year() in looping.py'''

    def test_prints_10_to_1_hny(self):
        '''prints 10 to 1 countdown then "Happy New Year!"'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        
        
        sys.stdout = sys.__stdout__
        answer = captured_out.getvalue()
        
        #answer.split(\n) produces a list that ends in ''
        answer_list = answer.split('\n')
        #second to last value should be the HNY string
        
        digit_strings = [str(i) for i in range(1,11)]
        remaining_digits = [i for i in digit_strings if i not in answer_list] 
    

class TestSquareIntegers:
    '''square_integers() in looping.py'''

    def test_square_integers(self):
        '''returns squared ints for [1, 2, 3, 4, 5] and [-1, -2, -3, -4, -5]'''
      
        
class TestFizzBuzz:
    '''fizzbuzz() in looping.py'''

    def test_prints_1_to_100_fizzbuzz(self):
        '''prints 1 to 100 with fizz 3s, buzz 5s, fizzbuzz 3and5s'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
   
        sys.stdout = sys.__stdout__
        answer = captured_out.getvalue()
      
        
        
        i = 1
        for line in answer.split('\n'):
            if(line): #answer.split(\n) produces a list that ends in ''
                if i % 15 == 0: assert line == "FizzBuzz", "Should have printed 'Buzz' when number is {}, got {} instead".format(i, line)
                elif i % 3 == 0: assert line == "Fizz", "Should have printed 'Fizz' when number is {}, got {} instead".format(i, line)
                elif i % 5 == 0: assert line == "Buzz", "Should have printed 'Buzz' when number is {}, got {} instead".format(i, line)
                else: assert str(i) == line, "Should have printed {}, got {} instead".format(i, line)
                i += 1
        
        i = i - 1
       
