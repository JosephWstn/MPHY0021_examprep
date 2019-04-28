import csv
import json
import matplotlib.pyplot as plt
import math

# initialise empty rainfall dictionary
rainfall_dictionary = {}

# read CSV file
with open("python_language_1/python_language_1_data.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ",")
    
    # skip header line
    next(readCSV) 
    
    # go through rows, assigning values
    for row in readCSV:
        year = int(row[0])
        day = int(row[1])
        rainfall = float(row[2])
        
        # if dictionary doesn't contain current year, add it 
        if year not in rainfall_dictionary:
            current_year_rain_list = []
            current_year_rain_list.append(rainfall)
            rainfall_dictionary[year] = current_year_rain_list
        
        # if dictionary does contain current year, append the new rainfall
        else:
            current_year_rain_list = rainfall_dictionary[year]
            current_year_rain_list.append(rainfall)
            rainfall_dictionary[year] = current_year_rain_list


# write json file        
with open("data.json", "w") as fp:
    json.dump(rainfall_dictionary, fp)
    
    
def plot_year(JSON_filename, year, colour = "blue"):
    """
    plot the rainfall throughout a specified year
    
    parameters
    ----------
    JSON_filename (str):
        The name of the JSON file containing the full set of rainfall data
    year (str):
        The year of interest
    colour (str):
        Optional parameter of colour of plot
        
    returns
    -------
    N/A
    
    """
    # read JSON file
    full_JSON = json.load(open(JSON_filename, "r"))
    
    # access specified year
    rainfall_in_year = full_JSON[year]

    # plot the current year lists
    year_plot, year_plot_axes = plt.subplots()
    year_plot_axes.plot(rainfall_in_year, colour)
    name = year+"raindata.png"
    year_plot.savefig(name)

    

def plot_average(JSON_filename, start, end):
    """
    plot the yearly average rainfall over a specified time period
    
    parameters
    ----------
    JSON_filename (str):
        The name of the JSON file containing the full set of rainfall data
    start (str):
        The begining of the time period of interest
    end (str):
        The end of the time period of interest
        
    returns
    -------
    N/A
    
    """
    
    # read JSON file
    full_JSON = json.load(open(JSON_filename, "r"))
    
    # get list of years between start and end
    years = range(int(start), int(end)+1)
    
    # create averages list
    averages = []
    for year in years:
        current_year_data = full_JSON[str(year)]
        current_year_average = sum(current_year_data)/float(len(current_year_data))
        averages.append(current_year_average)
        
    # plot the averages
    averages_plot, averages_plot_axes = plt.subplots()
    averages_plot_axes.plot(years, averages, "blue")
    name = start + "-" + end +"averages.png"
    averages_plot.savefig(name)


def CF_single_value(value):
    """
    Carry out the correction factor of a single value
    parameters
    ----------
    value (float):
        The value for the CF to be carried out on
    
    returns
    -------
    The new corrected value
    """
    return value * 1.2 **(math.sqrt(2))


def CF_yearlist_for(JSON_filename, year):
    """
    Carry out the correction factor on a specified year using a for loop
    parameters
    ----------
    JSON_filename (str):
        The name of the JSON file containing the full set of rainfall data
    year (str):
        The year of interest
    
    returns
    -------
    The new corrected values of the year
    """
    
    full_JSON = json.load(open(JSON_filename, "r"))
    year_list = full_JSON[year]
    
    # create new list using CF
    new_year_list = []
    for value in year_list:
        new_value = CF_single_value(value)
        new_year_list.append(new_value)
    return new_year_list

def CF_yearlist_comp(JSON_filename, year):
    """
    Carry out the correction factor on a specified year using a for loop
    parameters
    ----------
    JSON_filename (str):
        The name of the JSON file containing the full set of rainfall data
    year (str):
        The year of interest
    
    returns
    -------
    The new corrected values of the year
    
    
    List comprehension cons:
        - can produce harder to read code
    List comprehension pros:
        - more concise code
        - can do advanced statements such as nexted loops
        - faster than for loop
        
    For loop cons:
        - longer code
        - slower than list comp
    For loop pros:
        - easier to read and understand
    """
    
    
    full_JSON = json.load(open(JSON_filename, "r"))
    year_list = full_JSON[year]
    
    # create new list using CF
    new_year_list = [CF_single_value(value) for value in year_list]
    return new_year_list
    
    

# create the plots specified
plot_year("data.json", "1998", "black")
plot_average("data.json", "1988", "2000")