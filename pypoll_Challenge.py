#Module 3 CHALLENGE

#Adding to the Module 3 pypoll.py file:
#1) Breakdown votes and percentage by county
#2) Determine the largest county turnout


#import dependencies
import csv
import os

#Assign a variable for the file, and define it's path using OS
file_to_load = os.path.join("Resources","election_results.csv")

#Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

#initialize a vote counter
total_votes = 0

#list the candidates
candidate_options = []

#count candidate votes (dictionary)
candidate_votes = {}

#list the counties (CHALLENGE)
county_options = []

#count county votes (CHALLENGE)
county_votes = {}

#winning candidate / winning vote count tracker
winning_candidate = " "
winning_count = 0
winning_percentage = 0

#winning county
winning_county = " "
county_winning_count = 0
county_winning_percentage = 0

#open election results file:
with open(file_to_load) as election_data:

    #To Do: perform analysis
    file_reader = csv.reader(election_data) #3.4.3

    #print the header
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        #add to total vote count
        total_votes += 1 

        #print the candidate for each row * and print counties
        candidate_name = row[2]
        county_name = row[1] #(CHALLENGE)

        #look for unique candidates
        if candidate_name not in candidate_options:
            #append to candidate options list
            candidate_options.append(candidate_name)

            #initialize vote count for that candidate
            candidate_votes[candidate_name] = 0

        #add votes for each candidate
        candidate_votes[candidate_name] += 1

        #look for unique counties (CHALLENGE)
        if county_name not in county_options:
            county_options.append(county_name)

            county_votes[county_name] = 0
        county_votes[county_name] += 1


#save the results to a text file (3.6)  
with open(file_to_save, "w") as txt_file:

# Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n")
    print(election_results, end="")

    # Save the final vote count to the text file.
    txt_file.write(election_results)

##### challenge section - counting county stats    

    # Determine the percentage of votes for each county by looping through the counts.
    # 1. Iterate through the county list.
    for county in county_votes:
        # 2. Retrieve vote count of a county.
        countyvotes = county_votes[county]
        # 3. Calculate the percentage of votes.
        countyvote_percentage = float(countyvotes) / float(total_votes) * 100
        
        #save as a variable: results to print each candidate's name, vote count, and percentage 
        county_results = (f"{county}: {countyvote_percentage:.1f}% ({countyvotes:,})\n")
        
        # Print each candidate, their voter count, and percentage to the terminal.
        print(county_results)
        # Save the candidate results to our text file.
        txt_file.write(county_results)

        #determine winning vote count - set equal to winning candidate:
        if(countyvotes>county_winning_count) and (countyvote_percentage>county_winning_percentage):
            #if true, set winning count = vote count and winning percentage = vote percentage
            county_winning_count = countyvotes
            county_winning_percentage = countyvote_percentage
            winning_county = county

    #To Do: print out winning candidate's name, vote count, and percentage to TERMINAL
    winning_county_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"-------------------------\n")
    
    #print winning candidate summary to terminal and text file
    print(winning_county_summary)

    txt_file.write(winning_county_summary)  
#### end challenge section

    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        
        #save as a variable: results to print each candidate's name, vote count, and percentage 
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        # Save the candidate results to our text file.
        txt_file.write(candidate_results)

        #determine winning vote count - set equal to winning candidate:
        if(votes>winning_count) and (vote_percentage>winning_percentage):
            #if true, set winning count = vote count and winning percentage = vote percentage
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate

    #To Do: print out winning candidate's name, vote count, and percentage to TERMINAL
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    
    #print winning candidate summary to terminal and text file
    print(winning_candidate_summary)

    txt_file.write(winning_candidate_summary)   


    
#close file
election_data.close()