import csv
import os


######################## READING A CSV FILE ###################

file_path = f'{os.getcwd()}\\Section17\\example.csv'
#open the file
data = open(file_path,encoding='utf-8')
#csv.reader
csv_data = csv.reader(data)
#reformat it into a python object such as list of lists
data_lines = list(csv_data)
print(data_lines)
print(len(data_lines))
print(data_lines[0][1])

####################### WRITING A CSV FILE ####################
file_to_output = open(f'{os.getcwd()}\\Section17\\output.csv', mode='w', newline='')
csv_writer = csv.writer(file_to_output, delimiter=',') ##Delimiter specifies how to seprate 2 cols
# csv_writer.writerow(['a','b','c'])
csv_writer.writerows([['1','2','3'],['3','2','1']]) ##will write as rows, list of lists