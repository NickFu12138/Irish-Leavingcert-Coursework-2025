import csv  # import the CSV module to read and write files
# list of csv files to be merged
paths = ["cleaned_2017.csv",
         "cleaned_2018.csv",
         "cleaned_2019.csv",
         "cleaned_2020.csv",
         "cleaned_2021.csv",
         "cleaned_2022.csv"]

merged = []# list to store merged data
merged_file ="house_cost_overburden_.csv" #name of the new single file contain six years data
header_written = False # flag to ensure the header is written only once not six times

for i in paths:
    # use with method to read new lines from six seperated csv files
    with open(i,"r") as file:
        reader = csv.reader(file)
        header = next(reader) # read hearder role
        header[0] = ""
        if not header_written: # write the header only once from the first file
            merged.append(header)
            header_written = True
        for row in reader:  # append all data rows to the merged list
            merged.append(row)
# write new row into the csv
with open(merged_file,"w",newline = "") as file:
    writer = csv.writer(file) #create write object
    writer.writerows(merged) # write all collected rows to the new file
    
    


# print confirmation message
print(f"files are now merged succesfully to {merged_file}")

    