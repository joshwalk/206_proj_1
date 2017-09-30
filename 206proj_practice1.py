import os
import filecmp
import csv
import re
import datetime

with open('P1DataA.csv', 'r') as csv_input_file:
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

#print(l_of_d)

l_of_d_sorted = sorted(l_of_d, key=lambda k: k['Last'])
top_dict = l_of_d_sorted[0]
top_dict_first_name = top_dict['First']
top_dict_last_name = top_dict['Last']
full_name = top_dict_first_name + " " + top_dict_last_name
print(full_name)

count_dict = {}
list_of_class_strings = []
for d in l_of_d:
    for k, v in d.items():
        if k == 'Class':
            list_of_class_strings.append(v)
for class_name in list_of_class_strings:
    count_dict[class_name] = count_dict.get(class_name, 0) + 1
tuples_list_class_count = sorted(count_dict.items())
print(tuples_list_class_count)

day_count_dict = {}
list_of_day_strings = []
for d in l_of_d:
    for k, v in d.items():
        if k == 'DOB':
            day_number = re.findall('/(.*)/', v)
            list_of_day_strings.append(day_number[0])
for a in list_of_day_strings:
    day_count_dict[a] = day_count_dict.get(a, 0) + 1
tuples_list_day_count = sorted(day_count_dict.items())
tuples_list_day_count.sort(key=lambda x:x[1], reverse=True)
print(tuples_list_day_count[0][0])

list_of_dob = []
list_of_ages = []
for d in l_of_d:
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
print (round(age_avg))

unparsed_date = '4/28/1993'
parsed_date_month = int(re.findall('(.*)/.*/.*', unparsed_date)[0])
parsed_date_day = int(re.findall('/(.*)/', unparsed_date)[0])
parsed_date_year_full = int(re.findall('.*/.*/(.*)', unparsed_date)[0])
print(parsed_date_year_full)

today = datetime.date.today()
date_of_birth = datetime.date(parsed_date_year_full, parsed_date_month, parsed_date_day)
age = today - date_of_birth
age_in_years = age.total_seconds() / (365.25*24*60*60)
print(age_in_years)

with open('practice_out.csv', 'w') as file_out:
    csv_output = csv.writer(file_out)
    i = 0
    while i < len(l_of_d_sorted):
        for k, v in l_of_d_sorted[i].items():
            if k == 'First':
                first_name = v
            elif k == 'Last':
                last_name = v
            elif k == 'Email':
                email = v
                i += 1
        csv_output.writerow([first_name, last_name, email])
        # print(first_name + "," + last_name + "," + email)



# for line in csv_input:
#     print(line[4])
