import csv    # import the CSV module to read and write to the file
import pygal  # import pygal module to generate interactive graphs, from https://www.pygal.org/en/stable/installing.html



# remove any second hand house prices as they are not what we are discussing 
raw_2 = "monthly average rent.csv"
cleaned_2 = "cleaned_monthly_average_rent.csv"

cleaned_data = []

with open(raw_2, "r") as file:
    reader = csv.reader(file)
    
    next(reader)
    next(reader)
    
    
    header = ["Year", "Rent"]
    
    cleaned_data.append(header)
    
    for row in reader:
        cleaned_data.append(row)
        #row.pop(1)
        
            
# use with method to write new lines in the cleaned csv files
with open(cleaned_2, "w", newline = "") as file:
    writer = csv.writer(file)
    writer.writerows(cleaned_data)
    
    
    
print(f"cleaned data are stored in: {cleaned_2}")

