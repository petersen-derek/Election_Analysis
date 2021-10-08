# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who recieved votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Summary
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The Candidate rsults were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
    - Diana DeGette received 73.8% of the vote and 272,892 votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.
- The winner of the election was:
    - Diana DeGette who received 73.8% of the vote and 272,892 votes.

## Challenge Overview
The purpose of this audit was to determine the number of votes cast in each county to calculate the percent of votes by county.   

## Challenge Results
Election-Audit Results: Using a bulleted list, address the following election outcomes. Use images or examples of your code as support where necessary.

- How many votes were cast in this congressional election?
    - Total Votes: 369,711
- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
    - County Votes:
        - Jefferson: 10.5% (38,855)
        - Denver: 82.8% (306,055)
        - Arapahoe: 6.7% (24,801)
- Which county had the largest number of votes?
    - Largest County Turnout: Denver
- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
    - Candidate Votes:
        - Charles Casper Stockham: 23.0% (85,213)
        - Diana DeGette: 73.8% (272,892)
        - Raymon Anthony Doane: 3.1% (11,606)
- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
    - Winning Candidate:
        - Winner: Diana DeGette
        - Winning Vote Count: 272,892
        - Winning Percentage: 73.8%

## Challenge Summary
For future election audits, it is recommended to use the attached Python script.  This script can very quickly and cleanly summarize the results of any election as long as the data is in the same format.  If the data is not in the same format the script can quickly be modified.  Below is a snapshot of the query results followed by a couple modifications that can be made for future datasets.  
![image](https://user-images.githubusercontent.com/90879042/136629752-67f19a32-c53a-41c5-b1df-273760247c2b.png)


### Modification 1 - Column changes
If the columns are in a different order or there are additional columns in the dataset, one would just need to modify row 48 "candidate_name = row[2]".  This line of code is expecting the 3rd column to hold the candidate name field.  If the candidate name is actually in column 6 - you would change the line to be "candidate_name = row[5]".
![image](https://user-images.githubusercontent.com/90879042/136629575-d0f763bc-e24f-48d7-b470-2406d7eeb2d3.png)

### Modification 2 - Row/Heading
If there is no heading in the new dataset - you can simply comment out/delete row 39. 
![image](https://user-images.githubusercontent.com/90879042/136629605-40577c4b-9144-4298-981f-535c24fbb7a1.png)


