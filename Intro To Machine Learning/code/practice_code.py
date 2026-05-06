#pandas for data vis and sklearn for the main tree and test splits
import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor


#where data ia stored
iowa_file_path = 'C:\\Users\\hp\\OneDrive\\Desktop\\house-prices-advanced-regression-techniques\\train.csv'
home_data = pd.read_csv(iowa_file_path)
#y is the target, the value that we have to teach our model to predict
y = home_data.SalePrice
#x are the features. we use trendsin in theses specific featutes to predict basocaally how x influences y
features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = home_data[features]

# Split into validation and training data
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

# Specify Model
iowa_model = DecisionTreeRegressor(random_state=1)
# Fit Model
iowa_model.fit(train_X, train_y)

# Make validation predictions and calculate mean absolute error
val_predictions = iowa_model.predict(val_X)
val_mae = mean_absolute_error(val_predictions, val_y)
print("Validation MAE: {:,.0f}".format(val_mae))

#an mae func tht checks mae my copmating predictions with known values
def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return(mae)

#given diffrset tree sizes we try to find one woht minimum mae
candidate_max_leaf_nodes = [5, 25, 50, 100, 250, 500]

scores = {}

for max_leaf_nodes in candidate_max_leaf_nodes:
    mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    scores[max_leaf_nodes] = mae

best_tree_size = min(scores, key=scores.get)


#now that we know the best tree size fromt eh above func we give that as an input to the "final model" to get minimum mae


# Fill in argument to make optimal size and uncomment
final_model = DecisionTreeRegressor(max_leaf_nodes=best_tree_size, random_state=1)

# fit the final model and uncomment the next two lines
final_model.fit(X, y)


#using the final model
predictions = final_model.predict(X.head())

print(predictions)


#Decision trees leave you with a difficult decision. A deep tree with lots of leaves will overfit because each prediction is coming from historical data from only the few houses at its leaf. But a shallow tree with few leaves will perform poorly because it fails to capture as many distinctions in the raw data.