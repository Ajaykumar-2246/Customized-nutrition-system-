document.getElementById('generateButton').addEventListener('click', async function () {
    const age = document.getElementById('age').value;
    const height = document.getElementById('height').value;
    const weight = document.getElementById('weight').value;
    const gender = document.getElementById('gender').value;
    const activity = document.getElementById('activity').value;
    const plan = document.getElementById('plan').value;

    const response = await fetch('http://localhost:5000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ age: parseInt(age), height: parseInt(height), weight: parseInt(weight), gender: parseInt(gender), activity: parseInt(activity), plan: parseInt(plan) }),
    });

    const result = await response.json();
    
    const mealBoxes = document.getElementById('mealBoxes');
    mealBoxes.classList.remove('hidden');

    document.getElementById('breakfastContent').innerText = `${result.breakfast.Recipe_name}`;
    document.getElementById('lunchContent').innerText = `${result.lunch.Recipe_name}`;
    document.getElementById('dinnerContent').innerText = `${result.dinner.Recipe_name}`;
});
