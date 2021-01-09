#!/usr/bin/env python
# coding: utf-8

# In[3]:


import csv
import os


# In[23]:


csvpoll = os.path.join('election_data.csv')
exportpoll = os.path.join('election_data.txt')


# In[29]:


total_votes = 0
win_count = 0
candidate = []
candidate_votes = { }


with open(csvpoll) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
   

    
    for i in csvreader:
        total_votes = total_votes + 1
        candidate_name = i[2]
        if candidate_name not in candidate:
            candidate.append(candidate_name)
            candidate_votes[candidate_name]=0
        candidate_votes[candidate_name] = candidate_votes[candidate_name]  + 1
   

with open(exportpoll,"w") as txt_file:
    
    summary = (
    f"\nElection Results\n"
    f"-----------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-----------------------\n"

    )

    txt_file.write(summary)
    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percnt = float(votes) / float(total_votes)*100
        
        if(votes > win_count):
            win_count = votes
            winning_candidate = candidate
        voter_output = f"{candidate}:{vote_percnt:.3f}% ({votes})\n"
        txt_file.write(voter_output)
      
    summary = (
    f"-----------------------\n"
    f"Winning Candidate: {winning_candidate}\n"
    f"-----------------------\n"
    )
    print(summary)
    txt_file.write(summary)
    


# In[ ]:




