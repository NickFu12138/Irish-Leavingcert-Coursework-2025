import csv     # import the CSV module to read and write to the file 
import pygal   # import pygal module to generate interactive graphs, from https://www.pygal.org/en/stable/installing.html



# remove any second hand house prices as they are not what we are discussing 
raw_1 = "new house prices.csv"
cleaned_1 = "cleaned_new_house_prices.csv"

cleaned_data = []

with open(raw_1, "r") as file:
    reader = csv.reader(file)
    # use next skip the header row 
    header = next(reader)
    
    header.pop(3)
    
    header[0] = "Statistic Label"
    
    # use strip to remove any unwanted character  
    header[0] = header[0].split(":")[-1].strip()
    
    cleaned_data.append(header)
    
    for row in reader:
        if row[0] == "Second Hand House Prices":
            continue
          
        if row[2].strip().lower() == "national":
                continue
            
        row.pop(3)
            
        cleaned_data.append(row)
            
# use with method to write new lines in the cleaned csv files
with open(cleaned_1, "w", newline = "") as file:
    writer = csv.writer(file)
    writer.writerows(cleaned_data)
    
    
    
print(f"cleaned data are stored in: {cleaned_1}")

