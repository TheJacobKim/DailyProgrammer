# Description
# No more hiding from your alarm clock! You've decided you want your computer to keep you updated on the time so you're never late again. A talking clock takes a 24-hour time and translates it into words.
# Input Description
# An hour (0-23) followed by a colon followed by the minute (0-59).
# Output Description
# The time in words, using 12-hour format followed by am or pm.
# Sample Input data
# 00:00
# 01:30
# 12:05
# 14:01
# 20:29
# 21:00
# Sample Output data
# It's twelve am
# It's one thirty am
# It's twelve oh five pm
# It's two oh one pm
# It's eight twenty nine pm
# It's nine pm
# Extension challenges (optional)
# Use the audio clips found here to give your clock a voice.


def talking_clock(hour, minute):
    """A simple attempt to make a talking clock."""
    talk = "It's "
    num_for_hour_list = ['twelve ', 'one ', 'two ', 'three ', 'four ', 'five ', 'six ', 'seven ', 'eight ', 'nine ', 'ten ', 'eleven ', 'twelve ', 'thirteen ', 'fourteen ', 'fifteen ', 'sixteen ', 'seventeen ', 'eighteen ', 'nineteen ']
    num_by_one_list = ['', 'one ', 'two ', 'three ', 'four ', 'five ', 'six ', 'seven ', 'eight ', 'nine ', 'ten ',
                       'eleven ', 'twelve ', 'thirteen ', 'fourteen ', 'fifteen ', 'sixteen ', 'seventeen ', 'eighteen ', 'nineteen ']
    num_by_ten_list = ['oh ', ' ', 'twenty ', 'thirty ', 'forty ', 'fifty ',]
    is_PM = False

    if hour>12:
        hour = hour - 12
        is_PM = True

    talk += num_for_hour_list[hour]

    if minute == 0:
        pass
    elif minute < 10:
        talk += 'oh ' + num_by_one_list[minute]
    elif minute < 20:
        talk += num_by_one_list[minute]
    else:
        talk += num_by_ten_list[int(minute/10)]
        talk += num_by_one_list[minute%10]

    if is_PM == True:
        talk += 'pm'
    else:
        talk += 'am'

    print(talk)

print("Type any time in this format - ##:##")
time = input("Input: ")
hour = int(time[0:2])
minute = int(time[3:5])

if len(time)>5 or hour>24 or minute>60:
    print("Please input according to the format.")
else:
    talking_clock(hour, minute)