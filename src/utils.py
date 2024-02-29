import os
import sys

import numpy as np 
import pandas as pd
import dill
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.execeptions import CustomException

def save_object(file_path, obj):
    # try:

    # File path to save the pickle file
    # file_path_test = 'C:\\Projects\\GitLabPublic\\ML-OPS\\mlops-demo1\\src\\componenets\\artifacts'
    file_path_test = 'src\\componenets\\artifacts'

    # Save data to pickle file
    with open(file_path_test, 'wb') as f:
        pickle.dump(data, f)

    dir_path = os.path.dirname("C:\\Projects\\GitLabPublic\\ML-OPS\\mlops-demo1\\src\\componenets\\artifacts\\model.pkl")
    print("working")
    os.makedirs(dir_path, exist_ok=True)

    with open(file_path, "wb") as file_obj:
        pickle.dump(obj, file_obj)

    # except Exception as e:
    #     raise CustomException(e, sys)
    
def evaluate_models(X_train, y_train,X_test,y_test,models,param):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para=param[list(models.keys())[i]]

            gs = GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            #model.fit(X_train, y_train)  # Train model

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)
    
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)