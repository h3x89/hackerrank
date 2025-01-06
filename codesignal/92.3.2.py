# https://learn.codesignal.com/course/92/unit/3/practice/2

# You are given a time period formatted as a string in the HH:MM:SS - HH:MM:SS format. HH:MM:SS represents the time in hours, minutes, and seconds form, and the hyphen (-) separates the start time from the end time of the period.

# Your task is to calculate how many minutes pass from the start time until the end time.

# Here are some guidelines:

# The input times are always valid time strings in the HH:MM:SS format, with HH ranging from 00 to 23, and MM and SS from 00 to 59.
# The output should be an integer, representing the total length of the time period in minutes.
# The start time of the period will always be earlier than the end time, so periods that cross over midnight (like 23:00:00 - 01:00:00) are not considered.
# We are interested in the number of times the time passes some HH:MM:00 after the start time until the end time. Any remaining seconds should be disregarded; for instance, a period of "12:15:00 - 12:16:59" represents 1 minute, not 2, and a period of "12:14:59 - 12:15:00" also represents 1 minute.

# Your function should look like this:

# def time_period_length(time_period):
#     pass  # Your code goes here
# Where time_period is a string formatted as HH:MM:SS - HH:MM:SS. The function should return a single integer that represents the total length of the specified time period in minutes.

# Example:

# time_period_length("12:15:30 - 14:00:00")  # should return 105

def time_period_length(time_period):
    # Split the time period into start and end times
    start_time, end_time = time_period.split(' - ')

    # Split the start and end times into hours, minutes, and seconds
    start_hours, start_minutes, start_seconds = map(int, start_time.split(':'))
    end_hours, end_minutes, end_seconds = map(int, end_time.split(':'))

    # Convert the start and end times to total minutes without seconds
    start_total_minutes = start_hours * 60 + start_minutes
    end_total_minutes = end_hours * 60 + end_minutes

    # Check if the start time is greater than the end time
    if start_total_minutes > end_total_minutes:
        end_total_minutes += 1440  # Add 24 hours to the end time

    # Calculate the total minutes between the start and end times
    total_minutes = end_total_minutes - start_total_minutes
    return total_minutes

print(time_period_length("12:15:30 - 14:00:00"))  

import unittest
class SolutionTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(time_period_length("00:00:00 - 00:00:01"), 0)

    def test2(self):
        self.assertEqual(time_period_length("00:00:00 - 00:01:00"), 1)

    def test3(self):
        self.assertEqual(time_period_length("00:59:59 - 01:00:00"), 1)

    def test4(self):
        self.assertEqual(time_period_length("00:00:00 - 23:59:59"), 1439)

    def test5(self):
        self.assertEqual(time_period_length("01:05:05 - 16:30:50"), 925)

    def test6(self):
        self.assertEqual(time_period_length("12:15:30 - 14:00:00"), 105)

    def test7(self):
        self.assertEqual(time_period_length("02:45:20 - 06:37:35"), 232)

if __name__ == '__main__':
    unittest.main()