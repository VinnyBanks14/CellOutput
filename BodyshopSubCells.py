# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 10:48:54 2020

@author: VBANKS
"""
import pandas as pd
import matplotlib.pyplot as plt


JPHTarget = 32
Availability = 95.00
HoursAvailable = 70

SecondsInHour = 3600
SubCells = ['SubCell 1', 'SubCell 2', 'SubCell 3', 'SubCell 4', 'SubCell 5', 'SubCell 6']
CycleTimes = [90, 102, 113, 104, 107, 103]
GrossOutputPerHour = []
GrossOutputPerWeek = []
NetOutputPerHour = []
NetOutputPerWeek = []

# Create loops to fill in the blank lists which indicate outputs
j = 0
for i in SubCells:
    GrossSubOutput = SecondsInHour / CycleTimes[j]
    GrossOutputPerHour.append(GrossSubOutput)
    j = j + 1
print(GrossOutputPerHour)
k = 0
for i in SubCells:
    GrossSubWeekly = HoursAvailable * GrossOutputPerHour[k]
    GrossOutputPerWeek.append(GrossSubWeekly)
    k = k + 1
print(GrossOutputPerWeek)
l = 0
for i in SubCells:
    NetSubOutput = GrossOutputPerHour[l] / 100 * Availability
    NetOutputPerHour.append(NetSubOutput)
    l = l + 1
print(NetOutputPerHour)
m = 0
for i in SubCells:
    NetSubWeekly = GrossOutputPerWeek[m] / 100 * Availability
    NetOutputPerWeek.append(NetSubWeekly)
    m = m + 1
print(NetOutputPerWeek)

#Convert data into a DataFrame using pandas

df = pd.DataFrame(list(zip(SubCells, CycleTimes, GrossOutputPerHour, GrossOutputPerWeek, NetOutputPerHour, NetOutputPerWeek)),
                columns = ['SubCells', 'CycleTimes', 'GrossOutputPerHour', 'GrossOutputPerWeek', 'NetOutputPerHour', 'NetOutputPerWeek'])

print(df)



