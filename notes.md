# Machine Learning notes

### A place to jot down any important best practices, tips, or interesting information along the way

#### Inspecting / Exploring the data:

- Use horiztonal histograms when possible
- It is important to thoroughly check out the data before jumping right into training in order to fully understand the data.

#### Visualization must haves:

- run histograms on the entire data set
- run histograms on columns you are most interested in
- plot any geographic data
- correlation matrix (preferred)

#### Training / Test sets:

- ~66% train and ~33% test is reccomended (Or ~80% train and 20% test)
- visualize train and test set to ensure they are similar. Very important that they are not signifigantly different. Use a stratified split if this is hard to achieve (gets you even distribution).
- Look at test set as little as possible, you want to be unbiased.

#### General:

- Code is read way more than it is written, use conventions whenever possible.
- ALWAYS VISUALIZE DATA (Don'e just trust the stats)
- matplot lib is ok, but plotly power bi or tableu (mac) are better.
