# Import necessary libraries
import time  # For time-related functions
import json  # For JSON parsing
import requests  # For making HTTP requests
import pandas as pd  # For working with data frames

# Record the start time of the script
start_time = time.time()

# Read the CSV file containing airport codes into a DataFrame
Airport_file = pd.read_csv('airport_codes.csv')

# Extract the 'Code' column from the DataFrame and convert it to a list
codes = Airport_file['Code'].tolist()

# Initialize DataFrames to store total departures and arrivals
Total_departures = pd.DataFrame()
Total_arrival = pd.DataFrame()

# Loop through each airport code
for j, i in enumerate(codes):

    # Define a function to fetch data from the API based on the airport code
    def file_path_():    
        # Construct the URL for API request using the airport code
        url = f'https://api.aviationapi.com/v1/vatsim/pilots?apt=K{i}'
        
        # Send HTTP GET request to the API endpoint with a timeout of 10 seconds
        response = requests.get(url, timeout=10)
        
        # Introduce a delay every 40 requests to avoid rate limiting
        if j % 40 == 0:
            time.sleep(20)
            
        # Initialize DataFrames to store departures and arrivals
        df_departures = pd.DataFrame()
        df_arrivals = pd.DataFrame()
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            try:
                # Extract departures and arrivals data from the JSON response
                df_departures = pd.DataFrame(data[i]['Departures'])
                df_arrivals = pd.DataFrame(data[i]['Arrivals'])
            except KeyError:
                # Handle the case where the 'Departures' or 'Arrivals' key is missing
                pass
        else:
            # Print an error message if the request fails
            print(f"Failed to fetch data. Status code: {response.status_code}")
        
        # Return the DataFrames containing departures and arrivals data
        return df_departures, df_arrivals
    
    # Call the function to fetch data for the current airport code
    A, B = file_path_()

    # Concatenate the departures and arrivals data with the total departures and arrivals DataFrames
    Total_departures = pd.concat([Total_departures, A], ignore_index=True)
    Total_arrival = pd.concat([Total_arrival, B], ignore_index=True)

# Write the total departures and arrivals data to CSV files
Total_departures.to_csv('Total Departures.csv', index=False)
Total_arrival.to_csv('Total Arrival.csv', index=False)

# Record the end time of the script
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

# Print the elapsed time
print("Elapsed time:", elapsed_time, "seconds")
