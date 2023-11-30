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

#### Preparing data:

- To deal with missing data in columns you can either delete the rows with the missing column data, delete the column entirely or perform imputation.

#### General:

- Code is read way more than it is written, use conventions whenever possible.
- ALWAYS VISUALIZE DATA (Don't just trust the stats)
- matplot lib is ok, but plotly power bi or tableu (mac) are better.
- sklearn will transform things into numpy arrays which are bad for data visualization. Use pandas DataFrame to convert these for visualization purposes.
- Use an ordinal encoder when you have categories that have an order to them (ex. good, better, best). If not objectively better, use a hot encoder. Hot encoder will avoid bias.

#### Feature engineering:

- Science of using domain knowledge to create new features (columns) of data using raw data.

#### Scaling data:

- Columns with unintentionally higher values will skew calculations. Always scale your data.

#### Validation:

- Use K-Fold Cross-Validation to validate our data. This will divide out set into a specified number of folds (10) and train on 9 while testing on the last.

#### Fine Tuning:

- After picking a model you need to fine-tune the hyper paramaters (parameters unaffected by training) in order to find the ideal ones for a given model. You can use Grid Search.
- Grid Search may take a long time due to it searching every single feature in the feature space. Try randomized search for large feature space.

#### Anomaly Detection:

- Especially for image classification models, anomaly detection is a useful practice. There are several approaches to doing this but a straightforward way is to obtain latent vectors and calcuate the median for certain classes. A threshold can then be chosen to flag predictions that lie outside of said threshold.
