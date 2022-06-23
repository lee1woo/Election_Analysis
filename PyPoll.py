# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote 

# Add our dependencies
import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv") 

#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter
total_votes =0

# Candidate Options
candidate_options=[]

# 1. Declare the empty dictionary

candidate_votes = {}

# Winning Candidate and Winning Count Tracker

winning_candidate = ""

winning_count = 0

winning_percentage = 0


# Open the election results and read the file.

with open(file_to_load) as election_data:
   
   #to do: read and analyze the data

   # Read the file object with the reader function

    file_reader = csv.reader(election_data)

    # Read and print the header row
    headers = next(file_reader)

# Print each row to the CSV file

    for row in file_reader:
        #2. Add to the total vote count

        total_votes +=1

        # Print the candidate name from each row
        candidate_name = row[2]

        #if candidate does not match existing candidate

        if candidate_name not in candidate_options:
            #Add it to list of candidates

            candidate_options.append(candidate_name)

            # 2. Begin tracking that candidate's vote count

            candidate_votes[candidate_name] =0

            # Add a vote to the candidate's count

        candidate_votes[candidate_name] += 1

#Save the results to our tet file

with open(file_to_save, "w") as txt_file:

    # After opening file, print final vote count to terminal
    election_results = (
        f"\nElection Results\n"

        f"---------------------------\n"

        f"Total Votes: {total_votes:,}\n"

        f"---------------------------\n")

    print(election_results, end="")

    # Save final vote count to the text file

    txt_file.write(election_results)

    # Iterate through the candidate list

    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate 

        votes = candidate_votes[candidate_name]

        # Calculate percentage of votes

        vote_percentage = float(votes) / float(total_votes)*100
        
        candidate_results = (
            f"{candidate_name}: {vote_percentage: .1f}% ({votes:,})\n")

        #to do: print out each candidate's name, vote count, and percentage of votes to terminal
        print(candidate_results)

        #save candidate results to txt file

        txt_file.write(candidate_results)


        # Determine winning vote count and candidate
        # Determine if votes is greater than winning count

        if (votes > winning_count) and (vote_percentage > winning_percentage):

            # if true then set winning_count = votes and winning_percent = vote_percentage

            winning_count = votes

            winning_percentage = vote_percentage

            #Set winning_candidate equal to candidate's name

            winning_candidate = candidate_name

    # Print winning candidate results to terminal
    winning_candidate_summary = (
        
        f"----------------------\n"

        f"Winner: {winning_candidate}\n"

        f"Winning Vote Count: {winning_count:,}\n"

        f"Winning Percentage: {winning_percentage:.1f}%\n"

        f"-----------------------\n")

    print(winning_candidate_summary)

    # Save winning candidate's results to txt file.


    txt_file.write(winning_candidate_summary)
    # Close the file
