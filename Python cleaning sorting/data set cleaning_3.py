import csv        # import the CSV module to read and write to the file
import pygal   # import pygal module to generate interactive graphs, from https://www.pygal.org/en/stable/installing.html


raw_1 = "2017.csv"
cleaned_1 = "cleaned_2017.csv"

cleaned_data_1 = []
# use with method to read new lines in the uncleaned csv files
with open(raw_1, "r") as file:
    reader = csv.reader(file)
    #isolate csv header 
    header = next(reader)
    header = [num.replace(",","") for num in header]
    header[0] = "2017"
    cleaned_data_1.append(header)
    
    for row in reader:
        row[0] =  row[0].replace(",","")
        cleaned_data_1.append(row)
            
    #newline tell python not to do any extra processing of newline characters
with open(cleaned_1, "w", newline = "") as file:
    writer = csv.writer(file)
    writer.writerows(cleaned_data_1)
    
    
    
print(f"cleaned data are stored in:{cleaned_1}")


raw_2 = "2018.csv"
cleaned_2 = "cleaned_2018.csv"

cleaned_data_2 = []
# use with method to read new lines in the uncleaned csv files
with open(raw_2, "r") as file:
    reader = csv.reader(file)
    #isolate csv header 
    header = next(reader)
    header = [num.replace(",","") for num in header]
    header[0] = "2018"
    cleaned_data_2.append(header)
    
    for row in reader:
        row[0] =  row[0].replace(",","")
        cleaned_data_2.append(row)
            
    #newline tell python not to do any extra processing of newline characters
with open(cleaned_2, "w", newline = "") as file:
    writer = csv.writer(file)
    writer.writerows(cleaned_data_2)
    
    
    
print(f"cleaned data are stored in:{cleaned_2}")


raw_3 = "2019.csv"
cleaned_3 = "cleaned_2019.csv"

cleaned_data_3 = []
# use with method to read new lines in the uncleaned csv files
with open(raw_3, "r") as file:
    reader = csv.reader(file)
    #isolate csv header 
    header = next(reader)
    header = [num.replace(",","") for num in header]
    header[0] = "2019"
    cleaned_data_3.append(header)
    
    for row in reader:
        row[0] =  row[0].replace(",","")
        cleaned_data_3.append(row)
            
    #newline tell python not to do any extra processing of newline characters
with open(cleaned_3, "w", newline = "") as file:
    writer = csv.writer(file)
    writer.writerows(cleaned_data_3)
    
    
    
print(f"cleaned data are stored in:{cleaned_3}")

raw_4 = "2020.csv"
cleaned_4 = "cleaned_2020.csv"

cleaned_data_4 = []
# use with method to read new lines in the uncleaned csv files
with open(raw_4, "r") as file:
    reader = csv.reader(file)
    #isolate csv header 
    header = next(reader)
    header = [num.replace(",","") for num in header]
    header[0] = "2020"
    cleaned_data_4.append(header)
    
    for row in reader:
        row[0] =  row[0].replace(",","")
        cleaned_data_4.append(row)
            
    #newline tell python not to do any extra processing of newline characters
with open(cleaned_4, "w", newline = "") as file:
    writer = csv.writer(file)
    writer.writerows(cleaned_data_4)
    
    
    
print(f"cleaned data are stored in:{cleaned_4}")


raw_5 = "2022.csv"
cleaned_5 = "cleaned_2022.csv"

cleaned_data_5 = []
# use with method to read new lines in the uncleaned csv files
with open(raw_5, "r") as file:
    reader = csv.reader(file)
    #isolate csv header 
    header = next(reader)
    header = [num.replace(",","") for num in header]
    header[0] = "2022"
    cleaned_data_5.append(header)
    
    for row in reader:
        row[0] =  row[0].replace(",","")
        cleaned_data_5.append(row)
            
    #newline tell python not to do any extra processing of newline characters
with open(cleaned_5, "w", newline = "") as file:
    writer = csv.writer(file)
    writer.writerows(cleaned_data_5)
    
    
    
print(f"cleaned data are stored in:{cleaned_5}")

raw_6 = "2021.csv"
cleaned_6 = "cleaned_2021.csv"

cleaned_data_6 = []
# use with method to read new lines in the uncleaned csv files
with open(raw_6, "r") as file:
    reader = csv.reader(file)
    #isolate csv header 
    header = next(reader)
    header = [num.replace(",","") for num in header]
    header[0] = "2021"
    cleaned_data_6.append(header)
    
    for row in reader:
        row[0] =  row[0].replace(",","")
        cleaned_data_6.append(row)
            
    #newline tell python not to do any extra processing of newline characters
with open(cleaned_6, "w", newline = "") as file:
    writer = csv.writer(file)
    writer.writerows(cleaned_data_6)
    
    
    
print(f"cleaned data are stored in:{cleaned_6}")
