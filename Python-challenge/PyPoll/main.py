import os
import csv

# Get the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Specify the relative path to the CSV file
election_csv = os.path.join(script_dir, "Resources", "election_data.csv")


analysis_folder = os.path.join(script_dir, "analysis")

# Read the CSV file
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    next(csvreader)

    # Initialize variables to store results
    total_votes = 0
    candidates = {}
    winner = {"name": "", "votes": 0}

    # Iterate through each row in the file
    for row in csvreader:
        # Count total votes
        total_votes += 1

        # Extract candidate name
        candidate_name = row[2]

        # Update candidate votes count
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1

    # Find the winner
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        print(f"{candidate}: {percentage:.3f}% ({votes} votes)")

        # Update the winner
        if votes > winner["votes"]:
            winner["name"] = candidate
            winner["votes"] = votes

    # Print the output of the election
    print("\nElection Result\n")
    print("\n--------------------------------\n")
    print(f"\nTotal Votes: {total_votes}\n\n")
    print("--------------------------------")
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        print(f"\n{candidate}: {percentage:.3f}% ({votes} votes)")
    print("\n--------------------------------\n")
    print(f"\nWinner: {winner['name']}\n\n")
    
    print("--------------------------------")

     # Export result to a text file in the 'analysis' folder
    output_path = os.path.join(analysis_folder, "Election_analysis.txt")
    with open(output_path, "w") as output_file:
      output_file.write("\nElection Result\n")
      output_file.write("\n--------------------------------\n")
      output_file.write(f"\nTotal Votes: {total_votes}\n\n")
      output_file.write("--------------------------------\n")
      for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        output_file.write(f"\n{candidate}: {percentage:.3f}% ({votes} votes)\n")
      output_file.write("\n--------------------------------\n")
      output_file.write(f"\nWinner: {winner['name']}\n\n")
      output_file.write("--------------------------------")
