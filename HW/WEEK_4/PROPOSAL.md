## DATA620 Spring 2023  

### Team Members:  

Josh Iden  
Wilson Ng  

![](https://github.com/josh1den/DATA620-GROUP/blob/main/HW1/IMG/ASSIGNMENT.png)

### Proposed Data Source  

For this assignment, we propose using the **Social Network: MOOC User Action Dataset** data compiled by the Stanford Network Analysis Project (SNAP). 

Source: [https://snap.stanford.edu/data/act-mooc.html](https://snap.stanford.edu/data/act-mooc.html)

From dataset documentation:

*The MOOC user action dataset represents the actions taken by users on a popular MOOC platform. The actions are represented as a directed, temporal network. The nodes represent users and course activities (targets), and edges represent the actions by users on the targets. The actions have attributes and timestamps. To protect user privacy, we anonimize the users and timestamps are standardized to start from timestamp 0. The dataset is directed, temporal, and attributed.*

*Additionally, each action has a binary label, representing whether the user dropped-out of the course after this action, i.e., whether this is last action of the user.*

The dataset contains three files:  

**mooc_actions.tsv**, 	*Time-ordered sequence of user actions.*  
**mooc_action_features.tsv**,  	*Features associated with each action.*  
**mooc_action_labels.tsv**, 	*Binary label associated with each action, indicating whether the student drops-out after the action.*  

### Load & Analysis Plan  

Our analysis will focus on the hypothetical outcome, can degree centrality be used to predict the total number of actions taken before dropping out of the course. 

The individual data files will be loaded into pandas dataframes and combined into one master edge list containing the categorical feature, and read from pandas into a networkx Graph object. 
