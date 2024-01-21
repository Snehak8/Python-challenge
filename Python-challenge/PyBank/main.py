import os
import csv

# Get the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Specify the relative path to the CSV file
budget_csv = os.path.join(script_dir, "Resources", "budget_data.csv")

# Checking the 'analysis' folder if it doesn't exist
analysis_folder = os.path.join(script_dir, "analysis")


# Open the CSV file
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip header
    next(csvreader)

    # Define function
    def analyze_data(csvreader):
        # Initialize variables to store results
        total_month = 0
        net_total = 0
        last_PnL = 0
        changes = []
        greatest_increase = {"date": "", "amount": float("-inf")}
        greatest_decrease = {"date": "", "amount": float("inf")}

        for row in csvreader:
            # Check if the row has at least two columns
            if len(row) >= 2:
                # Extract date and profit and loss
                date = row[0]
                profit_loss = int(row[1])

                # Calculate total number of months and profit/loss
                total_month += 1
                net_total += profit_loss

                # Calculate change
                change = profit_loss - last_PnL

                # Calculate change in profit/loss and store
                if total_month > 1:
                    changes.append(change)

                    # Update greatest increase and decrease
                    if change > greatest_increase["amount"]:
                        greatest_increase["date"] = date
                        greatest_increase["amount"] = change

                    if change < greatest_decrease["amount"]:
                        greatest_decrease["date"] = date
                        greatest_decrease["amount"] = change

                # Update last profit and loss
                last_PnL = profit_loss

        # Calculate average
        average_change = sum(changes) / len(changes) if len(changes) > 0 else 0

        # Print result to terminal
        print("Financial Analysis")
        print("--------------------------------")
        print(f"Total Months: {total_month}")
        print(f"Net Total: ${net_total}")
        print(f"Average Change: ${average_change:.2f}")
        print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
        print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")

        # Export result to a text file in the 'analysis' folder
        output_path = os.path.join(analysis_folder, "financial_analysis.txt")
        with open(output_path, "w") as output_file:
            output_file.write("Financial Analysis\n")
            output_file.write("--------------------------------\n")
            output_file.write(f"Total Months: {total_month}\n")
            output_file.write(f"Net Total: ${net_total}\n")
            output_file.write(f"Average Change: ${average_change:.2f}\n")
            output_file.write(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n")
            output_file.write(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n")

    # Call the function with csvreader
    analyze_data(csvreader)

