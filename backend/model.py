import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import pickle
import os

MODEL_PATH = 'backend/model.pkl'
recipes_df = pd.read_csv("data/All_Diets.csv")

def train_model():
    user_data = pd.read_csv('data/user_nutritional_data.csv')
    
    X = user_data[['Age', 'Weight', 'Height', 'Gender', 'Physical exercise', 'Daily meals frequency']]
    y = user_data[['Calories', 'Proteins', 'Fats', 'Carbs']]

    preprocessor = ColumnTransformer(transformers=[
        ('num', StandardScaler(), ['Age', 'Weight', 'Height'])
    ])

    model_pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
    ])

    model_pipeline.fit(X, y)

    with open(MODEL_PATH, 'wb') as f:
        pickle.dump(model_pipeline, f)

    return model_pipeline

def load_model():
    with open(MODEL_PATH, 'rb') as f:
        return pickle.load(f)

if os.path.exists(MODEL_PATH):
    model = load_model()
else:
    model = train_model()

def predict_nutrition(age, weight, height, gender, activity, meal_frequency):
    input_data = np.array([[age, height, weight, gender, activity, meal_frequency]])
    input_df = pd.DataFrame(input_data, columns=['Age', 'Height', 'Weight', 'Gender', 'Physical exercise', 'Daily meals frequency'])

    predicted_nutrition = model.predict(input_df)[0]

    return {
        'calories': predicted_nutrition[0],
        'protein': predicted_nutrition[1],
        'fat': predicted_nutrition[2],
        'carbs': predicted_nutrition[3],
        'meals': get_meal_recommendations(predicted_nutrition),
    }

def get_meal_recommendations(predicted_nutrition):
    recipes_df['calorie_diff'] = (recipes_df['Calories'] - predicted_nutrition[0]).abs()
    recipes_df['protein_diff'] = (recipes_df['Protein(g)'] - predicted_nutrition[1]).abs()
    recipes_df['fat_diff'] = (recipes_df['Fat(g)'] - predicted_nutrition[2]).abs()
    recipes_df['carb_diff'] = (recipes_df['Carbs(g)'] - predicted_nutrition[3]).abs()
    
    recipes_df['total_diff'] = (recipes_df['calorie_diff'] + 
                                 recipes_df['protein_diff'] + 
                                 recipes_df['fat_diff'] + 
                                 recipes_df['carb_diff'])

    closest_recipes = recipes_df.nsmallest(3, 'total_diff')
    meals = closest_recipes.sample(frac=1).reset_index(drop=True)

    return {
        'breakfast': meals.iloc[0].to_dict(),
        'lunch': meals.iloc[1].to_dict(),
        'dinner': meals.iloc[2].to_dict(),
    }

def calculate_calories(protein_grams, fat_grams, carb_grams):
    calories_from_protein = protein_grams * 4
    calories_from_fat = fat_grams * 9
    calories_from_carb = carb_grams * 4
    
    total_calories = calories_from_protein + calories_from_fat + calories_from_carb
    return total_calories
