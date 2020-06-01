#Module 3

#Pseudocode:
#Data to retrieve:
#1. Total number of votes
#2. List of candidates who received votes
#3. Percentage of votes each candidate got
#4. Total number of votes each candidate got
#5. Winner of election (popular vote)

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

#winning candidate / winning vote count tracker
winning_candidate = " "
winning_count = 0
winning_percentage = 0

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

        #print the candidate for each row
        candidate_name = row[2]
        
        #look for unique candidates
        if candidate_name not in candidate_options:
            #append to candidate options list
            candidate_options.append(candidate_name)

            #initialize vote count for that candidate
            candidate_votes[candidate_name] = 0

        #add votes for each candidate
        candidate_votes[candidate_name] += 1

#save the results to a text file (3.6)  
with open(file_to_save, "w") as txt_file:

# Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file.
    txt_file.write(election_results)

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