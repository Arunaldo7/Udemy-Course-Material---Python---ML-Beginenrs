import numpy as np;
from collections import Counter;
from sklearn.preprocessing import LabelEncoder;

class Node:
    def __init__(self, feature = None, threshold = None, left_child = None, right_child = None, *, value = None):
        self.feature = feature;
        self.threshold = threshold;
        self.left_child = left_child;
        self.right_child = right_child;
        self.value = value;
        
    
    def is_leaf_node(self):
        return self.value is not None;
    

class DecisionTree:
    def __init__(self, max_depth = 100, min_samples_per_node = 2, total_needed_features = None):
        self.total_needed_features = total_needed_features;
        self.max_depth = max_depth;
        self.min_samples_per_node = min_samples_per_node;
        self.root_node = None;
        
    def fit(self, X, y):
        total_features = X.shape[1];
        self.total_needed_features = total_features if self.total_needed_features is None else min(total_features, self.total_needed_features);
        
        # print("total_needed_features:", self.total_needed_features);
        
        self.root_node = self._grow_tree(X, y, depth = 0);
    
    def _grow_tree(self, x_samples, y_samples, depth):
        
        total_samples, total_features = x_samples.shape;
        total_unique_classes = len(np.unique(y_samples));
        
        print("depth:",depth);
        print("total_unique_classes:",total_unique_classes);
        print("total_samples:",total_samples);
        
        if (depth >= self.max_depth) or (total_samples < self.min_samples_per_node) or (total_unique_classes == 1):
            #get most common label value
            return Node(value = self._get_most_common_label(y_samples));
        #else split node based upon best split
        else:
            feature_index, threshold, left_indices, right_indices = self._find_best_split(total_features, x_samples, y_samples);
            
            print("left_indices:",len(left_indices));
            print("right_indices:",len(right_indices));
            
            left_child = self._grow_tree(x_samples[left_indices, :], y_samples[left_indices], depth + 1);
            right_child = self._grow_tree(x_samples[right_indices, :], y_samples[right_indices], depth + 1);
            
            return Node(feature = feature_index, threshold = threshold, left_child = left_child, right_child = right_child);
            
    def _split_node(self, x_samples, feature_index, threshold):
        x_col_values = x_samples[:, feature_index];
        
        left_indices = np.argwhere(x_col_values <= threshold).flatten();
        right_indices = np.argwhere(x_col_values > threshold).flatten();
                
        return left_indices, right_indices;        
            
    def _find_best_split(self, total_features, x_samples, y_samples):
        best_gain = -1;
        
        split_feature, split_threshold = None, None;
        split_left_indices, split_right_indices = None, None;
        
        selected_feature_indices = np.random.choice(total_features, self.total_needed_features, replace = False);
        
        for feature_index in selected_feature_indices:
            x_col_values = x_samples[:, feature_index];
            threshold_list = np.unique(x_col_values);
            
            # print("threshold_list:",threshold_list.shape)
            
            for threshold in threshold_list:
                
                left_indices, right_indices = self._split_node(x_samples, feature_index, threshold);
                
                inf_gain = self._calc_inf_gain(y_samples, left_indices, right_indices);
                # print("inf_gain:",inf_gain);
                
                if inf_gain > best_gain:
                    best_gain = inf_gain;
                    split_feature = feature_index;
                    split_threshold = threshold;
                    split_left_indices = left_indices;
                    split_right_indices = right_indices;
            
        
        return split_feature, split_threshold, split_left_indices, split_right_indices;
                
                
    def _calc_inf_gain(self, y_samples, left_indices, right_indices):
        total_left_indices = len(left_indices);
        total_right_indices = len(right_indices);
        
        
        if total_left_indices == 0 or total_right_indices == 0:
            return 0;
        else:
            #parent entropy
            parent_entropy = self._calc_entropy(y_samples);
            
            #children entropy
            # print("y_samples:",y_samples)
            left_child_entropy  = self._calc_entropy(y_samples[left_indices]);
            right_child_entropy  = self._calc_entropy(y_samples[right_indices]);
            
            weighted_left_child_entropy = left_child_entropy  * (total_left_indices / len(y_samples));
            weighted_right_child_entropy = right_child_entropy *  (total_right_indices / len(y_samples));
            
            #total inf gain
            total_inf_gain = parent_entropy - weighted_left_child_entropy - weighted_right_child_entropy;
            
            return total_inf_gain;
    
    def _calc_entropy(self, y_samples):
        # lebel_encoder = LabelEncoder();
        # lebel_encoder.fit_transform(y_samples);
        counter = Counter(y_samples);
        count_samples = [count for __, count in counter.most_common()]
        total_samples = len(y_samples);
        # hist = np.bincount(y_samples);
        
        # hist = [value for value in hist if value > 0];
        
        entropy = np.sum([[-(value / total_samples) * np.log2(value / total_samples)] for value in count_samples]);
        
        return entropy;
        
    
    def _get_most_common_label(self, y):
        counter = Counter(y);
        
        return counter.most_common()[0][0];
    
    def predict(self, x):
        return [self._traverse(x_sample, self.root_node) for x_sample in x];
    
    def _traverse(self, x_sample, node):
        # print("Node feature: ", node.feature)
        # print("Node threshold: ", node.threshold)
        if node.is_leaf_node():
            return node.value;
        else:
            if x_sample[node.feature] <= node.threshold:
                return self._traverse(x_sample, node.left_child);
            else:
                return self._traverse(x_sample, node.right_child);
        