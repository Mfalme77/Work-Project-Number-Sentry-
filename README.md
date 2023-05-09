# Work-Project-Number-Sentry-
Number Sentry code
This code uses the pandas library to handle the .txt, csv, and xlsx files. You must import pandas to run (import pandas as pd, then use pd. to call pandas)
The 1st set of fuctions (create_number_sentry_list1-6) are to create each individual file.
This can definetly be consolidated into one function

The main function (create_file) uses pandas to read the 1st file which is in xlsx form ( I will need to add functionality to handle conditions when not true). When used in a variable pandas will appear as pd just as in the import statement.

Next there are 3 list conversions in order to arrive at a list of strings. This was done to avoid type errors when trying to append.

pd is used again to read the csv file.

followed by the calls to grab each index of the list

finally we see the earlier create_number_sentry_list functions along with code to write each to a .txt file named output'1-6'.txt


