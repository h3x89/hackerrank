# https://learn.codesignal.com/course/92/unit/3/practice/1

# You are given two input arguments: an array of strings timePoints and an integer added_seconds. Each string in timePoints is in the HH:MM:SS format, representing a valid time from "00:00:00" to "23:59:59" inclusive. The integer added_seconds represents a number of seconds, ranging from 1 to 86,400. Your task is to create a new function, add_seconds_to_times(timePoints, added_seconds), which takes these two arguments and returns a new array of strings. Each string in the returned array is the new time, calculated by adding the provided added_seconds to the corresponding time in timePoints, formatted in HH:MM:SS.

# The array timePoints contains n strings, where n can be any integer from 1 to 100 inclusive. The time represented by each string in timePoints is guaranteed to be valid. The total time, after adding added_seconds, can roll over to the next day.

# Example

# For timePoints = ['10:00:00', '23:30:00'] and added_seconds = 3600, the output should be ['11:00:00', '00:30:00'].

def add_seconds_to_times(timePoints, added_seconds):
    result = []
    for time in timePoints:
        # Convert time to total seconds
        hours, minutes, seconds = map(int, time.split(':'))
        total_seconds = hours * 3600 + minutes * 60 + seconds + added_seconds
        
        # Handle day rollover
        total_seconds %= 86400  # 24*60*60 = 86400 seconds in a day
        
        # Convert back to HH:MM:SS
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        
        result.append(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
    return result

# 3600 seconds is 1 hour
print(add_seconds_to_times(['10:00:00', '23:30:00'], 3600))
# ['11:00:00', '00:30:00']
print(add_seconds_to_times(['23:30:00'], 3600))
# ['00:30:00']
print(add_seconds_to_times(['23:30:00', '10:00:00'], 3600))
# ['00:30:00', '11:00:00']
import unittest

class TestAddSecondsToTimes(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            add_seconds_to_times(['10:00:00', '23:30:00'], 3600),
            ['11:00:00', '00:30:00']
        )
    
    def test2(self):
        self.assertEqual(
            add_seconds_to_times(['00:00:00'], 86399),
            ['23:59:59']
        )
    
    def test3(self):
        self.assertEqual(
            add_seconds_to_times(['01:00:00', '02:00:00', '03:00:00'], 7200),
            ['03:00:00', '04:00:00', '05:00:00']
        )
    
    def test4(self):
        self.assertEqual(
            add_seconds_to_times(['23:59:59'], 1),
            ['00:00:00']
        )
    
    def test5(self):
        self.assertEqual(
            add_seconds_to_times(['12:00:00'], 43200),
            ['00:00:00']
        )

    def test6(self):
        self.assertEqual(
            add_seconds_to_times(['23:59:01', '23:59:02', '23:59:03'], 2),
            ['23:59:03', '23:59:04', '23:59:05']
        )
      
    def test7(self):
        self.assertEqual(
            add_seconds_to_times(['13:14:15', '16:17:18', '19:20:21', '22:23:24'], 0),
            ['13:14:15', '16:17:18', '19:20:21', '22:23:24']
        )

    def test8(self):
        self.assertEqual(
            add_seconds_to_times(['00:00:01', '00:00:02', '00:00:03', '00:00:04', '00:00:05', '00:00:06', '00:00:07', '00:00:08', '00:00:09', '00:00:10'], 30),
            ['00:00:31', '00:00:32', '00:00:33', '00:00:34', '00:00:35', '00:00:36', '00:00:37', '00:00:38', '00:00:39', '00:00:40']
        )

  
if __name__ == "__main__":
    unittest.main()