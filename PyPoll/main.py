import os
import csv

my_dictionary = {"Grand_total" : 0}

# Path to collect data from the Resources folder
election_data = os.path.join('Resources', 'election_data.csv')


# Open and read csv
with open (election_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

 # Skip the header
    csv_header = next (csv_file)

    
    # Read through each row of data after the header row
    # Whoever the vote is for in this row, increase the
    # Grand_total value by 1.
    # In each row,"this_name" (i.e., row[2]) will be who was voted for
    
    # Explanation of code in line 39:
    # The part "my_dictionary.get(this_name, 0)" will (i) if this_name is 
    # already a key in the my_dictionary, return the value associated with 
    # with the key this_name (i.e., how many votes this_name has gotten so far),
    # or (ii) return 0 (the alternate value after the comma) if this_name 
    # isn't yet in my_dictionary because this is the first row in which someone
    # has voted for this_name. So, the full line of code in line 39
    # "my_dictionary[this_name] = my_dictionary.get(this_name, 0) + 1" 
    # (i) adds 1 to the this_name's votes if this_name is already in
    # my_dictionary, or (ii) if this_name isn't in my_dictionary yet, adds
    # this_name as a key to my_dictionary with value 1.  
    
    
    for row in csv_reader:
        my_dictionary["Grand_total"] += 1
        this_name = row[2]
        my_dictionary[this_name] = my_dictionary.get(this_name, 0) + 1
    

# Turn the updated dictionary into a list
my_list = list( my_dictionary.items())

# Sort the list in decreasing order by the number of votes
# This will put the Grand_total line first since the total number
# of votes is always more than the votes for any single candidate
my_list.sort(key = lambda x: x[1], reverse = True)

# my_total will be the total number of votes cast
my_total = my_list[0][1]
# format my_total as an integer with commas separating thousands
formatted_total = "{: ,}".format(my_total).rjust(10)

#ouput path for writing to text file
output = os.path.join("Analysis", "analysis.txt")
txt = open(output, "w")

print(f"Total votes = {formatted_total}\n")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n")

#Write to text file
txt.write("Election Results\n")
txt.write("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n")
txt.write(f"Total Votes: {formatted_total}\n")
txt.write("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n")



for item in my_list[1:]:
    # We're looking at each row of the last after the grand total row
    # The rows are now in the order of votes received with higher amounts first
    
    name = item[0]
    # format each name as a 10 digit string so the next columns will line up properly
    formatted_name = name.ljust(10)
    
    votes = item[1]
    # format votes as an integer with commas separating thousands
    formatted_votes = "{: ,}".format(votes).rjust(10)
    
    percent = 100 * votes / my_total
    # Format percent as % with two digits after decimal point
    formatted_percent = '{:.2f}%'.format(percent).rjust(10)
    
    message = f"{formatted_name} \t {formatted_percent} \t {formatted_votes}"
    print(message)
    txt.write(f"{formatted_name} \t {formatted_percent} \t {formatted_votes}\n")

# The winner is the name in the first row of my_list following the grand_total line 
winner = my_list[1][0]
formatted_winner = winner.ljust(10)
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n")
print(f"\nThe winner is:   {formatted_winner}\n")

txt.write(f"_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n")
txt.write(f"\nThe winner is:   {formatted_winner}\n")

