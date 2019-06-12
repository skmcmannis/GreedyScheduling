#Schedules activities supplied via an input file (act.txt), and outputs the scheduled activities to the
# terminal. Uses a greedy algorithm to select the activity that is last to start from the activities
# remaining to be scheduled.
#Author: Shawn McMannis
#Last mod date: 4/27/19

from __future__ import print_function
from itertools import islice

#Number of events
numEv  = 0

#Counter used to track the numer of sets of activities to be scheduled
counter = 0

#Array to store events
evTemp = []

#Array to store the events after initial processing
events = []

#Array to store the events after scheduling
results = []

#main

#Open import file 'act.txt'
with open("act.txt", "r") as importFile:
    for line in importFile:
        #If numEv has been reset, the next line will be the number of activities in the next set
        if numEv == 0:
            numEv = int(line)
        #Otherwise the next line is just the next activity in the set
        else:
            line = line.strip()
            evTemp.append(line)

        #If the number of activities in the list is equal to numEv
        if numEv == len(evTemp):

            #Convert the event strings in evTemp to int tuples for easier processing
            for i in range(len(evTemp)):
                temp = evTemp[i].split()
                events.append(temp)

                for j in range(len(events[i])):
                    events[i][j] = int(events[i][j])

                events[i] = tuple(events[i])

            #Sort the list of activities by event start time, latest first
            #Code idea from: https://stackoverflow.com/questions/3121979/how-to-sort-list-tuple-of-lists-tuples
            events.sort(key=lambda tup: tup[1], reverse=True)

            #Greedy scheduling algorithm
            results.append(events[0])

            i = 0
            m = 1

            for m in range(len(events)):
                if events[i][1] >= events[m][2]:
                    results.append(events[m])
                    i = m

            results.sort(key=lambda tup: tup[1])

            counter += 1

            #Print the results to the console
            print("Set ", counter)
            print("Number of activities selected: ", len(results))
            print("Activities: ", end='')
            for i in range(len(results)):
                print(results[i][0], " ", end='')
            print("\n")

            #Reset numEv
            numEv = 0

            #Clear arrays
            evTemp = []
            events = []
            results = []