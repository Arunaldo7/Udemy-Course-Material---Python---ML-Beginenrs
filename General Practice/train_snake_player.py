import pandas as pd;
import numpy as np;
from sklearn.preprocessing import OneHotEncoder, LabelEncoder;
from sklearn.compose import ColumnTransformer;
import pickle;
from sklearn.tree import DecisionTreeClassifier, export_text;
from sklearn.linear_model import LogisticRegression;
from sklearn.ensemble import RandomForestClassifier;
import sys;

from dtree_from_scratch import DecisionTree;

current_directory_path = sys.path[0] + "/";

train_dataset = pd.read_excel(current_directory_path + "game_state_dataset.xlsx");

# label_encoder_direction = LabelEncoder();
# label_encoder_direction = label_encoder_direction.fit(train_dataset["player_move_direction"]);
# train_dataset["player_move_direction"] = label_encoder_direction.transform(train_dataset["player_move_direction"]);

# one_hot_encoder = OneHotEncoder();

# enc_data = pd.DataFrame(one_hot_encoder.fit_transform(
#     train_dataset[["player_move_direction"]]).toarray());

# #Merge with main
# New_df = train_dataset.join(enc_data);
# New_df = New_df.drop(columns = ["player_move_direction"]);
# print("New_df.xols:", New_df.columns)

dependent_feature = "new_direction";

dependent_feature_values = train_dataset[dependent_feature];
independent_feature_dataset = train_dataset.drop(columns = [dependent_feature]);

categorical_features = [];
categorical_features_index = [];

all_independent_features = list(independent_feature_dataset.columns);

for feature in all_independent_features:
    if independent_feature_dataset[feature].dtype == object:
        categorical_features.append(feature);
        categorical_features_index.append(all_independent_features.index(feature));
        
        

col_transformer = ColumnTransformer(transformers =[
    ('enc', OneHotEncoder(sparse = False, drop ='first'), [0]),
], remainder ='passthrough')

col_transformer = col_transformer.fit(independent_feature_dataset);

encoded_independent_dataset = np.array(col_transformer.transform(independent_feature_dataset));

col_transformer_features_original = col_transformer.get_feature_names();

#rename encoded features

for feature_index in categorical_features_index:
    replace_string = f"enc__x{feature_index}";
    
    col_transformer_features_renamed = [feature.replace(replace_string,all_independent_features[feature_index]) for feature in 
                                                col_transformer_features_original];
    
encoded_independent_dataset = pd.DataFrame(encoded_independent_dataset, columns = col_transformer_features_renamed);

# model = DecisionTreeClassifier(random_state = 10, min_samples_split = 5);
# model = LogisticRegression();
# model = RandomForestClassifier(min_samples_split = 30);
model = DecisionTree();
model.fit(encoded_independent_dataset.values, np.array(dependent_feature_values));

# rules = export_text(model, feature_names = col_transformer_features_renamed);

# print("rules:", rules);

#dump model files
pickle.dump(col_transformer, open(current_directory_path + "col_transformer.pkl", "wb"));
pickle.dump(col_transformer_features_renamed, open(current_directory_path + "col_transformer_features.pkl", "wb"));
pickle.dump(model, open(current_directory_path + "model.pkl", "wb"));
