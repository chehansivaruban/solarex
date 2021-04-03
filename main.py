import pickle
import numpy as np

with open('final_decision_Tree_model', 'rb') as f:
    model = pickle.load(f)

test_data = np.array([16, 2, 5, 1, 2021])
answer =model.predict(test_data.reshape(1, 5))
print(answer)
list = answer.tolist()
print(list[0])
