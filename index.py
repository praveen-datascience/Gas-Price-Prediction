def read_file(filename):
    """ This function is used to read excel file and return dataframe """
    res = pd.read_csv(filename)
    return res

def clean_file(filename):
    """ find missing prices column and replace with average price """
    missing_price = filename['Prices'].isnull()
    price_average = filename['Prices'].mean()
    filename['Prices'].fillna(price_average, inplace=True)
    filename = filename.dropna()
    return filename

def line_plot(filename):
    x = filename['Dates']
    y = filename['Prices']
    plt.plot(x,y,label = 'Gas Prices',color='green', marker='o', linestyle='dashed' , linewidth=2 , markersize=12 , markeredgecolor='red')
    
    # Extract Nov,December,jan,feb,mar data
    data_nov_mar = filename[filename['Dates'].dt.month.isin([11, 12, 1, 2, 3])]
    plt.plot(data_nov_mar['Dates'], data_nov_mar['Prices'], color='blue', marker='o', linestyle='-', linewidth=2,
             markersize=8, markeredgecolor='black', label='Nov - Mar')
    
    plt.title('October 2020 - September 2024', fontdict={'fontname': 'Comic Sans MS' , 'fontsize': 20 , 'color': 'Red'})
    plt.xlabel('Date', fontdict={'fontname': 'Times New Roman' , 'fontsize': 15})
    plt.ylabel('Price', fontdict={'fontname': 'Comic Sans MS' , 'fontsize': 15})
    plt.legend()
    plt.show()
    
def get_estimated_price(filename, input_date):
    """ This function returns the estimated gas price for a given date """
    # Convert input date to datetime format
    input_date = pd.to_datetime(input_date)

    # Filter the data for the given date
    filtered_data = filename[filename['Dates'] == input_date]

    # Check if data exists for the given date
    if filtered_data.empty:
        return "No data available for the given date."

    # Retrieve the price value
    estimated_price = filtered_data['Prices'].values[0]

    return estimated_price

#read csv file
data = read_file("Nat_Gas.csv")
#check initial dataframe
print(data.head())

data = clean_file(data)

#Convert 'Dates' column to datetime format
data['Dates'] = pd.to_datetime(data['Dates'])

# Sort the data by date
data = data.sort_values('Dates')

line_plot(data)


# Take input date from the user
input_date = input("Enter a date (YYYY-MM-DD): ")

# Get the estimated price for the input date
estimated_price = get_estimated_price(data, input_date)
print("Estimated gas price for", input_date, "is", estimated_price)
