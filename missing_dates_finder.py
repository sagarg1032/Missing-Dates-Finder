import os
import re
from datetime import datetime, timedelta

# Function to extract date from filename
def extract_date_from_filename(filename):
    # Use regex to find the date in the filename with a specific pattern
    match = re.search(r'unformatted-product-ad-campaigns-report-(\d{4}-\d{2}-\d{2})', filename)
    if match:
        return match.group(1)  # Return the extracted date string
    return None  # Return None if no match is found

# Function to find missing dates in a given range
def find_missing_dates_in_range(start_date, end_date, available_dates):
    current_date = start_date  # Initialize the current date to the start date
    missing_dates = []  # List to store missing dates

    # Loop through each day in the date range
    while current_date <= end_date:
        date_str = current_date.strftime("%Y-%m-%d")  # Format the current date as a string
        if date_str not in available_dates:
            missing_dates.append(date_str)  # Add to missing dates if not present
        current_date += timedelta(days=1)  # Move to the next day

    return missing_dates  # Return the list of missing dates

# Prompt user for date range
start_date_str = input("Enter start date (YYYY-MM-DD): ")  # Get the start date from the user
end_date_str = input("Enter end date (YYYY-MM-DD): ")  # Get the end date from the user

# Convert input strings to datetime objects
start_date = datetime.strptime(start_date_str, "%Y-%m-%d")  # Parse start date string
end_date = datetime.strptime(end_date_str, "%Y-%m-%d")  # Parse end date string

# Ask the user to input the folder path where CSV files are stored
folder_path_input = input("Provide the folder path where CSV files are stored: ")

# Remove any double quotes from the input folder path
folder_path = folder_path_input.strip().replace('"', '')  # Clean up the folder path input

# Get list of filenames in the folder
filenames = os.listdir(folder_path)  # List all files in the specified folder

# Extract dates from filenames
available_dates = set()  # Use a set to store unique dates
for filename in filenames:
    date = extract_date_from_filename(filename)  # Extract date from each filename
    if date:
        available_dates.add(date)  # Add the date to the set if extracted

# Find missing dates in the given range
missing_dates = find_missing_dates_in_range(start_date, end_date, available_dates)

# Calculate the number of CSV files present and missing
total_dates = (end_date - start_date).days + 1  # Total days in the date range
present_count = len(available_dates)  # Count of available dates
missing_count = len(missing_dates)  # Count of missing dates

# Print counts and missing dates
print(f"Total dates in the range: {total_dates}")  # Print total dates in the range
print(f"Number of CSV files present: {present_count}")  # Print the count of present files
print(f"Number of missing dates: {missing_count}")  # Print the count of missing dates

if missing_dates:
    print("Missing dates:")
    for missing_date in missing_dates:
        print(missing_date)  # Print each missing date
else:
    print("No missing dates found.")  # Print a message if no dates are missing