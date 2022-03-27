import os
import csv
csvpath = os.path.join('Solution', 'election_results.csv')
with open(csvpath) as election_data:
    print(election_data)
election_data.close()
output = os.path.join('Solution', 'election_analysis.txt')
output_file = open(output, 'w')
output_file.write("Counties in the Election")
output_file.write("\nArapahoe")
output_file.write("\nDenver")
output_file.write("\nJefferson")
output_file.close()
with open(csvpath) as election_data:
 file_reader = csv.reader(election_data)
 for row in file_reader:
    print(row)
with open(csvpath) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)
    





    










    




















