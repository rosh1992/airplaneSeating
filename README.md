# airplaneSeating
Brief Description

Steps involved:
1. First I took out the groups bigger than 2 which has window preference and added it to the finalSeating list. I also sorted internally
in the group if any has window preference.
2. Then I added any group with maximum group length in this case 4, I added to the finalSeating list.
3. Next, remaining passengers were allocated based on combiantion of 1+3,2+2,3+1 in case of 4 being the number of seats in that row.
4. And finally the output is available on finalSeating1 list.

Two scenarios were tested which worked successfully and they are named as inputFile.txt and inputFIle1.txt. 
