# Missing Dates Finder

## Overview
This project is a Python script that identifies missing dates in a user-defined date range based on filenames in a specified folder. The script processes filenames that follow a specific naming convention containing dates, such as:

```
unformatted-product-ad-campaigns-report-YYYY-MM-DD
```

The script compares the extracted dates with the full range of dates to identify and report any missing files.

## Features
- Extracts dates from filenames using regex.
- Finds missing dates in a specified date range.
- Displays statistics on the total number of dates, files present, and missing dates.
- Generates a detailed list of missing dates for easy validation.

## Prerequisites
- Python 3.7+
- Basic knowledge of Python, Regular Expressions and file systems.
- Knowledge of running Python scripts in a terminal or IDE

## Setup and Usage
### 1. Clone the Repository
```bash
git clone <repository_url>
cd <repository_folder>
```

### 2. Install Dependencies
This script does not require any external Python libraries. Ensure Python is installed on your system.

### 3. Run the Script
```bash
python missing_dates_finder.py # Ensure the folder path provided has read permissions.
```

### 4. Provide User Inputs
- **Start Date:** Enter the start date in `YYYY-MM-DD` format.
- **End Date:** Enter the end date in `YYYY-MM-DD` format.
- **Folder Path:** Provide the folder path where the files are stored.

### Example Input
```
Enter start date (YYYY-MM-DD): 2024-12-01
Enter end date (YYYY-MM-DD): 2024-12-31
Provide the folder path where CSV files are stored: /path/to/your/folder
```

### Example Output
```
Total dates in the range: 31
Number of CSV files present: 25
Number of missing dates: 6
Missing dates:
2024-12-02
2024-12-05
2024-12-15
2024-12-20
2024-12-25
2024-12-30
```

## File Structure
```
.
├── missing_dates_finder.py   # Main script to find missing dates
├── README.md                 # Project documentation
```

## How It Works
1. **Date Extraction:** Extracts dates from filenames matching the regex pattern `unformatted-product-ad-campaigns-report-YYYY-MM-DD`.
2. **Date Comparison:** Compares the extracted dates with the full date range provided by the user.
3. **Statistics Generation:** Displays the total number of dates, files present, and missing dates, along with a list of missing dates.

## Contributions
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature/bug fix.
3. Commit your changes and push them to your branch.
4. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author
- **Sagar Gupta**
- GitHub: [sagarg1032](https://github.com/sagarg1032) - Explore more projects and contributions.

## Feedback
Feel free to raise an issue on GitHub if you encounter any bugs or have feature requests.

---

**Happy Coding!**