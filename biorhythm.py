# The given script computes the biorhythm values for the current day and adjacent days.

import datetime
from math import sin

def getBiorhythm(zd):
    pi = 3.141592
    zd = int(zd)
    physical = sin((zd % 23)*(2*pi/23))
    emotion = sin((zd % 28)*(2*pi/23))
    intellect = emotion = sin((zd % 33)*(2*pi/23))
    return physical, emotion, intellect

print ("-"*80)

print ("This script outputs your biorhythm values, determined by your age in days. It presents")
print ("the data for a span of seven days, positioning today in the middle. This arrangement")
print ("helps you identify whether you're in a phase of decline or ascent in your cycle.")
print ("")

bd = input("Enter your birthday (format = mm/dd/yyyy): ")

# split the string into month, day, year
dL = bd.split("/")

# convert to format datetime.date(year, month, day))
birthday = datetime.date(int(dL[2]), int(dL[0]), int(dL[1]))

# get todays date
today = datetime.date.today()

# Calculate age in days since birth
age = (today - birthday).days

p = []  # physical well-being list over range of 7 days
e = []  # emotional well-being list over range of 7 days
i = []  # intellectual well-being list over range of 7 days

for ax in range(age-3, age+4):
    px, ex, ix = getBiorhythm(ax)
    p.append(str(int(100*px)))
    e.append(str(int(100*ex)))
    i.append(str(int(100*ix)))

print ("-"*80)

print ("Birthday     =", birthday)
print ("Today        =", today)
print ("Age in days  =", age)

print ("-"*80)

print ("Here are your biorhythm values (higher values best):")
print ("Days from today", '-3', '-2', '-1', 'Today', '+1', '+2', '+3')
print ("Physical     : ", p[0], p[1], p[2], p[3], p[4], p[5], p[6])
print ("Emotional    : ", e[0], e[1], e[2], e[3], e[4], e[5], e[6])
print ("Intellectual : ", i[0], i[1], i[2], i[3], i[4], i[5], i[6])

print ("-"*80)