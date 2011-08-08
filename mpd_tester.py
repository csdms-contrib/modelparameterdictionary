#! /usr/env/python

#-----------------------------------------------------------------------
# mpd_tester.py
#
# This program does a simple test of the ModelParameterDictionary class.
#
# GT August 2011
#-----------------------------------------------------------------------

import model_parameter_dictionary
from model_parameter_dictionary import ModelParameterDictionary

print 'Testing ModelParameterDictionary ...'
my_param_dict = ModelParameterDictionary()
print 'Created a new dictionary.'
my_param_dict.read_from_file( 'myinputs.txt' )
print 'Opened and read myinputs.txt.'
pi = my_param_dict.read_float( 'PI' )
print 'Read PI =',pi
avogado = my_param_dict.read_float( 'AVOGADROS_NUMBER' )
print 'Read AVOGADROS_NUMBER =',avogado
fruit = my_param_dict.read_string( 'FAVORITE_FRUIT' )
print 'Read FAVORITE_FRUIT =',fruit
nmang = my_param_dict.read_int( 'NUMBER_OF_MANGO_WALKS' )
print 'Read NUMBER_OF_MANGO_WALKS =',nmang
apples_ok = my_param_dict.read_bool( 'ALSO_LIKES_APPLES' )
print 'Read ALSO_LIKES_APPLES =',apples_ok
missing_int = my_param_dict.read_int( 'MISSING_INT', 123 )
print 'Tried to read a missing integer with default value 123 =',missing_int
missing_float = my_param_dict.read_float( 'MISSING_FLOAT', 12.3 )
print 'Tried to read a missing float with default value 12.3 =',missing_float
missing_string = my_param_dict.read_string( 'MISSING_STRING', 'frog' )
print 'Tried to read a missing string with default value frog =',missing_string
missing_bool = my_param_dict.read_bool( 'MISSING_BOOL', True )
print 'Tried to read a missing bool with default value True =',missing_bool
print 'Test finished.'
