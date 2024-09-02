def most_common_month(date1, date2):
    # Define a dictionary to store the count of each month
    month_count = {
        '01': 0, '02': 0, '03': 0, '04': 0, '05': 0, '06': 0,
        '07': 0, '08': 0, '09': 0, '10': 0, '11': 0, '12': 0
    }
    
    # Split the input dates to extract the month
    day1, month1, year1 = date1.split('-')
    day2, month2, year2 = date2.split('-')
    
    # Convert month strings to integers
    month1 = int(month1)
    month2 = int(month2)