# Election_Analysis

## Overview of Election Audit: 
- An election commision in Colorado tasked Seth, Tom, and me to submit election audit results that includes: the winner of the election, how many votes each candidate received, the voter turnout of each county, the percentage of votes from each county out of the total number of votes cast, and the county with the highest turnout. 

## Results and Analysis

![screenshot](https://user-images.githubusercontent.com/102992388/175430754-30a19e19-525f-48e4-b315-d01be20712eb.png)

- How many votes were cast in this congressional election?
  - 369,711 votes were cast in this congressional election.
- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
  - Residents in 3 counties (Jefferson, Denver, and Arapahoe) casted votes in this election.
    - There were 38,855 votes in Jefferson County, comprising 10.5% of the total vote
    - There were 306,055 votes in Denver County, comprising 82.8% of the total vote
    - There were 24,801 votes in Arapahoe County, comprising 6.7% of the total vote
-  Which county had the largest number of votes?
  - Denver County 
- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
  - There were 3 candidates in this election: Charles Casper Stockham, Diana DeGette, Raymon Anthony Doane.
    - Charles Casper Stockham received 85,213 votes, comprising 23.0% of the total vote
    - Diana DeGette received 272,892 votes, comprising 73.8% of the total vote
    - Raymon Anthony Doane received 11,606 votes, comprising 3.1% of the total vote   
- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
  - Diana DeGette won the election, with 272,892 votes cast and 73.% of the total vote
- Election-Audit Summary: In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.
  -  This exact script can be used for any election as long as you sort the dataset to match the code (or you can modify your code slightly). If any dataset gives you a voter's county and candidate-choice information, you would be able to quickly sort that dataset to run this code. If the county information is in a different column, you would just need to adjust the following code:

```
county_name = row[1]
```
  
  -   and replace the number in the bracket.
  -   If the candidate name information is in a different column, you would adjust the following code:

```
candidate_name = row[2]
```

  -  You would also have to ensure your data file is in the proper resource folder. As long as your text file's name is edited in lieu of "election_results.csv", you would also be able to directly edit the file within the code as well.
