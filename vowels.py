#!/usr/bin/python
while True:
 char = raw_input("enter a character:")
 def vowel_check(char) :
  vowel = ['a','e','i','o','u']
  if char in vowel:
   print char, "is a vowel"
  else :
   print char, "isn't a vowel"
 vowel_check(char)