!pip install seaborn scikit-learn > /dev/null 2>&1
import pandas as pd
import numpy as np


MODEL_EXPORT_FOLDER = 'models'
from pathlib import Path
export_path = Path(MODEL_EXPORT_FOLDER)
export_path.mkdir(parents=True, exist_ok=True)

data_path = 'data/data_features.csv'
titanic_data = pd.read_csv(data_path)
titanic_data.head()

y=titanic_data['Survived']
x=titanic_data.iloc[:,1:]
x.drop('Name',axis=1,inplace=True)

tr_x, cv_x, tr_y, cv_y   = train_test_split(x, y, test_size = 0.30,stratify=y)
print(tr_x.head())
print(tr_y.head())

#The Machine learning alogorithm
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier()
rf.fit(tr_x, tr_y)

# save the model file for downstream tasks
from joblib import dump
dump(rf, '{}/model.joblib'.format(MODEL_EXPORT_FOLDER))

# also save a few example rows
np.save('data/test_rows.npy', cv_x[:10])
