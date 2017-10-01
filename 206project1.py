# Joshua Walker
# Project 1
# github username: joshwalk

import os
import filecmp
import csv
import datetime
import re

def getData(file):
#Input: file name
#Ouput: return a list of dictionary objects where
#the keys will come from the first row in the data.

#Note: The column headings will not change from the
#test cases below, but the the data itself will
#change (contents and size) in the different test
#cases.

	#Your code here:
	with open(file, 'r') as csv_input_file:
	    csv_input = csv.reader(csv_input_file)

	    l_of_d = []
	    header_row = next(csv_input)
	    for row in csv_input:
	        d = {}
	        i = 0
	        while i<len(header_row):
	            d[header_row[i]] = row[i]
	            i = i + 1
	        l_of_d.append(d)
	return l_of_d

#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName

	#Your code here:
	l_of_d_sorted = sorted(data, key=lambda k: k[col])
	top_dict = l_of_d_sorted[0]
	top_dict_first_name = top_dict['First']
	top_dict_last_name = top_dict['Last']
	full_name = top_dict_first_name + " " + top_dict_last_name
	return full_name

#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	#Your code here:
	count_dict = {}
	list_of_class_strings = []
	for d in data:
	    for k, v in d.items():
	        if k == 'Class':
	            list_of_class_strings.append(v)
	for class_name in list_of_class_strings:
	    count_dict[class_name] = count_dict.get(class_name, 0) + 1
	tuples_list_class_count = sorted(count_dict.items())
	tuples_list_class_count.sort(key=lambda x: x[1], reverse=True)
	return tuples_list_class_count



# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	day_count_dict = {}
	list_of_day_strings = []
	for d in a:
	    for k, v in d.items():
	        if k == 'DOB':
	            day_number = re.findall('/(.*)/', v)
	            list_of_day_strings.append(day_number[0])
	for a in list_of_day_strings:
	    day_count_dict[a] = day_count_dict.get(a, 0) + 1
	tuples_list_day_count = sorted(day_count_dict.items())
	tuples_list_day_count.sort(key=lambda x:x[1], reverse=True)
	tuples_list_day_count_int = tuples_list_day_count[0][0]
	return int(tuples_list_day_count[0][0])

# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	#Note from me: I realized later I went a little overboard in the precision of age calculation -- just wanted to be safe
	list_of_dob = []
	list_of_ages = []
	for d in a:
	    for k, v in d.items():
	        if k == 'DOB':
	            list_of_dob.append(v)
	for dob in list_of_dob:
	    parsed_date_month = int(re.findall('(.*)/.*/.*', dob)[0])
	    parsed_date_day = int(re.findall('/(.*)/', dob)[0])
	    parsed_date_year = int(re.findall('.*/.*/(.*)', dob)[0])
	    today = datetime.date.today()
	    date_of_birth = datetime.date(parsed_date_year, parsed_date_month, parsed_date_day)
	    age = today - date_of_birth
	    age_in_years = age.total_seconds() / (365.25*24*60*60)
	    list_of_ages.append(age_in_years)
	age_sum = 0
	for age in list_of_ages:
	    age_sum += age
	age_avg = age_sum/len(list_of_ages)
	return round(age_avg)

#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None

	# Your code here:
	l_of_d_sorted_csv = sorted(a, key=lambda k: k[col])
	output_file = open(fileName, 'w')
	i = 0
	while i < len(l_of_d_sorted_csv):
		for k, v in l_of_d_sorted_csv[i].items():
			if k == 'First':
				first_name = v
			elif k == 'Last':
				last_name = v
			elif k == 'Email':
				email = v
				i += 1
		output_file.write(first_name + "," + last_name + "," + email + "\n")

################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),40)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)

	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()
