import pygal # import pygal module to generate interactive graphs, from https://www.pygal.org/en/stable/installing.html
import csv # import the CSV module to read and write to the file
from pygal.style import Style    # import the style class from Pygal module to customize chart styles from https://www.pygal.org/en/3.0.0/documentation/styles.html

# average_house_price_ visualiztion


def visualize_1(csv_file, output_svg):
    # initialize data storage
    years = []
    galway_prices = []
    other_areas_prices = []
    dublin_prices = []
    cork_prices = []

    # read csv files
    with open(csv_file, 'r') as file:
        # use of dictionary
        reader = csv.DictReader(file)
        for row in reader:
            # avoid adding years repeatly as four data are displayed in a singe year
            if row['Years'] not in years:
                years.append(row['Years'])
            if row['Area'] == 'Galway':
                galway_prices.append(float(row['VALUE']))
            elif row['Area'] == 'Other areas':
                other_areas_prices.append(float(row['VALUE']))
            elif row['Area'] == 'Dublin':
                dublin_prices.append(float(row['VALUE']))
            elif row['Area'] == 'Cork':
                cork_prices.append(float(row['VALUE']))

    # visualize
    line_chart = pygal.Line()
    line_chart.title = 'House Prices Over Time by Area'
    # from years list (1975,1976,1977,etc...)
    line_chart.x_labels = years
    line_chart.x_label_rotation = 45  # prevent x label crowded together by rotate it  
    line_chart.x_title = 'Years'  # create x label
    line_chart.y_title = 'Price (€)'  # create y label
    line_chart.add('Galway', galway_prices)
    line_chart.add('Other Areas', other_areas_prices)
    line_chart.add('Dublin', dublin_prices)
    line_chart.add('Cork', cork_prices)

    # create a legend 
    line_chart.legend_at_bottom = True

    # output svg file
    line_chart.render_to_file(output_svg)

# call the function
csv_file_path = 'cleaned_new_house_prices.csv'  
output_svg_path = 'house_prices_by_area.svg'
visualize_1(csv_file_path, output_svg_path)

print(f"SVG file successfully created: {output_svg_path}")






# Housing Cost Overburden visualiztion

#2017
categories = []
spending_25 = []
spending_40 = []
spending_50 = []

# Select the starting and ending rows of the year data
start_row = 1
end_row = 5 

# Read data from a CSV file and extract the data of a specific row
with open('house_cost_overburden_.csv', 'r') as file:
    reader = csv.reader(file)
    rows = list(reader)  # Convert the data into a list so that it can be accessed by row index

    for row in rows[start_row:end_row]:
        categories.append(row[0].strip()) 
        spending_25.append(float(row[1]))  
        spending_40.append(float(row[2]))  
        spending_50.append(float(row[3]))  

# create bar chart
bar_chart = pygal.Bar()
bar_chart.title = 'Housing Cost Overburden Spending as Percentage of Disposable Income (2017)'
bar_chart.x_labels = categories

bar_chart.legend_at_bottom= True

# add the information 
bar_chart.add('HCB, spending over 25%', spending_25)
bar_chart.add('HCB, spending over 40%', spending_40)
bar_chart.add('HCB, spending over 50%', spending_50)

# export svg file 
bar_chart.render_to_file('HCB_2017.svg')


#2018
categories = []
spending_25 = []
spending_40 = []
spending_50 = []

# Select the starting and ending rows of the year data
start_row = 5
end_row = 9 

# Read data from a CSV file and extract the data of a specific row
with open('house_cost_overburden_.csv', 'r') as file:
    reader = csv.reader(file)
    rows = list(reader)  # Convert the data into a list so that it can be accessed by row index

    for row in rows[start_row:end_row]:
        categories.append(row[0].strip()) 
        spending_25.append(float(row[1]))  
        spending_40.append(float(row[2]))  
        spending_50.append(float(row[3]))  

# create bar chart
bar_chart = pygal.Bar()
bar_chart.title = 'Housing Cost Overburden Spending as Percentage of Disposable Income (2018)'
bar_chart.x_labels = categories

bar_chart.legend_at_bottom= True

# add the information 
bar_chart.add('HCB, spending over 25%', spending_25)
bar_chart.add('HCB, spending over 40%', spending_40)
bar_chart.add('HCB, spending over 50%', spending_50)

# export svg file 
bar_chart.render_to_file('HCB_2018.svg')



#2019
categories = []
spending_25 = []
spending_40 = []
spending_50 = []

# Select the starting and ending rows of the year data
start_row = 9
end_row = 13 

# Read data from a CSV file and extract the data of a specific row
with open('house_cost_overburden_.csv', 'r') as file:
    reader = csv.reader(file)
    rows = list(reader)  # Convert the data into a list so that it can be accessed by row index

    for row in rows[start_row:end_row]:
        categories.append(row[0].strip()) 
        spending_25.append(float(row[1]))  
        spending_40.append(float(row[2]))  
        spending_50.append(float(row[3]))  

# create bar chart
bar_chart = pygal.Bar()
bar_chart.title = 'Housing Cost Overburden Spending as Percentage of Disposable Income (2019)'
bar_chart.x_labels = categories

bar_chart.legend_at_bottom= True

# add the information 
bar_chart.add('HCB, spending over 25%', spending_25)
bar_chart.add('HCB, spending over 40%', spending_40)
bar_chart.add('HCB, spending over 50%', spending_50)

# export svg file 
bar_chart.render_to_file('HCB_2019.svg')



#2020
categories = []
spending_25 = []
spending_40 = []
spending_50 = []

# Select the starting and ending rows of the year data
start_row = 13 
end_row = 17 

# Read data from a CSV file and extract the data of a specific row
with open('house_cost_overburden_.csv', 'r') as file:
    reader = csv.reader(file)
    rows = list(reader)  # Convert the data into a list so that it can be accessed by row index

    for row in rows[start_row:end_row]:
        categories.append(row[0].strip()) 
        spending_25.append(float(row[1]))  
        spending_40.append(float(row[2]))  
        spending_50.append(float(row[3]))  

# create bar chart
bar_chart = pygal.Bar()
bar_chart.title = 'Housing Cost Overburden Spending as Percentage of Disposable Income (2020)'
bar_chart.x_labels = categories

bar_chart.legend_at_bottom= True

# add the information 
bar_chart.add('HCB, spending over 25%', spending_25)
bar_chart.add('HCB, spending over 40%', spending_40)
bar_chart.add('HCB, spending over 50%', spending_50)

# export svg file 
bar_chart.render_to_file('HCB_2020.svg')



#2021
categories = []
spending_25 = []
spending_40 = []
spending_50 = []

# Select the starting and ending rows of the year data
start_row = 17
end_row = 21  

# Read data from a CSV file and extract the data of a specific row
with open('house_cost_overburden_.csv', 'r') as file:
    reader = csv.reader(file)
    rows = list(reader)  # Convert the data into a list so that it can be accessed by row index

    for row in rows[start_row:end_row]:
        categories.append(row[0].strip()) 
        spending_25.append(float(row[1]))  
        spending_40.append(float(row[2]))  
        spending_50.append(float(row[3]))  

# create bar chart
bar_chart = pygal.Bar()
bar_chart.title = 'Housing Cost Overburden Spending as Percentage of Disposable Income (2021)'
bar_chart.x_labels = categories

bar_chart.legend_at_bottom= True

# add the information 
bar_chart.add('HCB, spending over 25%', spending_25)
bar_chart.add('HCB, spending over 40%', spending_40)
bar_chart.add('HCB, spending over 50%', spending_50)

# export svg file 
bar_chart.render_to_file('HCB_2021.svg')



#2022 
categories = []
spending_25 = []
spending_40 = []
spending_50 = []


# Select the starting and ending rows of the year data
start_row = 21  
end_row = 26   

# Read data from a CSV file and extract the data of a specific row
with open('house_cost_overburden_.csv', 'r') as file:
    reader = csv.reader(file)
    rows = list(reader)  # Convert the data into a list so that it can be accessed by row index

    for row in rows[start_row:end_row]:
        categories.append(row[0].strip()) 
        spending_25.append(float(row[1]))  
        spending_40.append(float(row[2]))  
        spending_50.append(float(row[3]))  

# create bar chart
bar_chart = pygal.Bar()
bar_chart.title = 'Housing Cost Overburden Spending as Percentage of Disposable Income (2022)'
bar_chart.x_labels = categories

bar_chart.legend_at_bottom= True

# add the information 
bar_chart.add('HCB, spending over 25%', spending_25)
bar_chart.add('HCB, spending over 40%', spending_40)
bar_chart.add('HCB, spending over 50%', spending_50)

# export svg file 
bar_chart.render_to_file('HCB_2022.svg')





# Average Monthly Rent visualization 

for row in data:
    
    pie_chart.add(str(row['Year']), row['Rent'], color=row['Color'])


pie_chart.render_to_file('average_monthly_rent_.svg')







# by using style in pygal module so I can choose which color to use 
custom_style = Style(
    colors=["#FFE5E5", "#FFCCCC", "#FFB2B2", "#FF9999", "#FF8080",
            "#FF6666", "#FF4D4D", "#FF3333", "#FF1A1A", "#FF0000",
            "#E60000", "#CC0000", "#B20000", "#990000", "#800000", "#660000"]
)

pie = pygal.Pie(style=custom_style, title="Average Monthly Rent by Year", inner_radius=0.4)

# append the data
data = [
    {"Year": 2011, "Rent": 1011.73},
    {"Year": 2012, "Rent": 1027.15},
    {"Year": 2010, "Rent": 1042.32},
    {"Year": 2013, "Rent": 1069.58},
    {"Year": 2009, "Rent": 1157.71},
    {"Year": 2014, "Rent": 1159.25},
    {"Year": 2015, "Rent": 1270.44},
    {"Year": 2008, "Rent": 1271.31},
    {"Year": 2016, "Rent": 1365.64},
    {"Year": 2017, "Rent": 1484.84},
    {"Year": 2018, "Rent": 1610.27},
    {"Year": 2019, "Rent": 1659.85},
    {"Year": 2020, "Rent": 1740.62},
    {"Year": 2021, "Rent": 1777.69},
    {"Year": 2022, "Rent": 1867.94},
    {"Year": 2023, "Rent": 1990.57},
]

# append the information
for row in data:
    pie.add(str(row['Year']), row['Rent'])

# extract svg files
pie.render_to_file('average_monthly_rent_.svg')










