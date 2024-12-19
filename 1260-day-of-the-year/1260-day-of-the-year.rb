# @param {String} date
# @return {Integer}
def day_of_year(date)
   # Split the date string into year, month, and day
  year, month, day = date.split('-').map(&:to_i)

  # Days in each month (non-leap year)
  days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

  # Check for leap year
  if (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)
    days_in_month[1] = 29
  end

  # Calculate the total days up to the previous month
  total_days = days_in_month[0...(month - 1)].sum

  # Add the days of the current month
  total_days + day
end