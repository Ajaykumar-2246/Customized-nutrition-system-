# Customized Nutrition Recommendation System
This app was developed to help people create personalized dietary plans. It can help create a plan to use for daily meals keeping in mind the nutritional requirements of the individual. The app includes higher degree of personalization than other apps, being able to customize the diet according to age, gender, bmi, etc.

## Architecture
**Frontend:** HTML / CSS / JS\
**Backend:** FastAPI, Python\
**Data:**
* *User Nutritional Requirements dataset _(CSV Format)_*
* *Recipes dataset _(CSV Format)_*

## Methodology
This application uses `RandomForest` to find and create a diet plan for individual needs using the provided inputs.
The model has been trained on user data with the required parameters with inputs such as "Age", "Gender", "Height", "Weight", "Physical exercise" and "Meal Plans", and it predicts outputs for "Calories", "Protein", "Carbs", "Fats".
When a new user inputs their data, the model predicts the nutritional requirements of the individual.
This output is used to identify the food items and recipes which will provide the required nutrients to the individual.

## Features
Current features in the app:
* Adding your data to get a meal plan based on your personal requirements.
* Age, gender, weight, height, physical exercise and diet plan as inputs.
* Creates a daily-based meal plan with breakfast, lunch and dinner.

## Future Plans
Future plans include:
* Adding more features and inputs to the model to personalize the diets even more.
* Ability to rate the recommendations from dislike to like. Allows the model to add/remove suggestions based on individual ratings.
* Adding allergies and dietary restrictions selector.
