#Module 3

#Pseudocode:
#Data to retrieve:
#1. Total number of votes
#2. List of candidates who received votes
#3. Percentage of votes each candidate got
#4. Total number of votes each candidate got
#5. Winner of election (popular vote)

import csv
import os

#Assign a variable for the file, and define it's path
#using OS
file_to_load = os.path.join("Resources","election_results.csv")

#open file:
with open(file_to_load) as election_data:

    #To Do: perform analysis
    file_reader = csv.reader(election_data) #3.4.3

    #print the header
    headers = next(file_reader)
    print(headers)


    #Create a filename variable to a direct or indirect path to the file.
    file_to_save = os.path.join("Analysis", "election_analysis.txt")
    
    with open(file_to_save, "w") as txt_file:
        # Write three counties to the file.
        txt_file.write("Counties in the election:\n--------------------------\n\nArapahoe\nDenver\nJefferson")

#close file
election_data.close()