import datetime
import numpy as np
from sklearn.tree import DecisionTreeRegressor

# Sample data
# Format: (hour, minute, weather_condition, wait_time)
historical_data = [
    (9, 0, "sunny", 20),
    (10, 30, "sunny", 25),
    (12, 0, "sunny", 30),
    (14, 0, "sunny", 40),
    (16, 0, "sunny", 35),
    (18, 0, "sunny", 45),
    (9, 0, "rainy", 15),
    (10, 30, "rainy", 20),
    (12, 0, "rainy", 25),
    (14, 0, "rainy", 30),
    (16, 0, "rainy", 25),
    (18, 0, "rainy", 35),
    (9, 0, "cloudy", 22),
    (11, 0, "cloudy", 27),
    (13, 0, "cloudy", 33),
    (15, 0, "cloudy", 37),
    (17, 0, "cloudy", 40),
    (19, 0, "cloudy", 42),
    (9, 0, "sunny", 18),
    (11, 0, "sunny", 23),
    (13, 0, "sunny", 28),
    (15, 0, "sunny", 35),
    (17, 0, "sunny", 38),
    (19, 0, "sunny", 47),
    (9, 0, "rainy", 14),
    (11, 0, "rainy", 19),
    (13, 0, "rainy", 23),
    (15, 0, "rainy", 28),
    (17, 0, "rainy", 32),
    (19, 0, "rainy", 36),
    (9, 0, "cloudy", 20),
    (11, 0, "cloudy", 25),
    (13, 0, "cloudy", 30),
    (15, 0, "cloudy", 35),
    (17, 0, "cloudy", 38),
    (19, 0, "cloudy", 40)
]

def preprocess_data(data):
    X = []
    y = []
    for entry in data:
        hour, minute, weather, wait_time = entry
        # Convert time to fractional representation (0-1)
        time_frac = hour / 24.0 + minute / 1440.0
        # Encode weather condition
        if weather == "sunny":
            weather_encoded = 0
        else:
            weather_encoded = 1  # rainy
        X.append([time_frac, weather_encoded])
        y.append(wait_time)
    return np.array(X), np.array(y)

def train_model(X, y):
    model = DecisionTreeRegressor()
    model.fit(X, y)
    return model

def predict_wait_time(model, current_time, weather):
    # Convert current time to fractional representation
    time_frac = current_time.hour / 24.0 + current_time.minute / 1440.0
    # Encode weather condition
    if weather == "sunny":
        weather_encoded = 0
    else:
        weather_encoded = 1  
    prediction = model.predict([[time_frac, weather_encoded]])
    return prediction[0]

def main():
    # Preprocess historical data
    X, y = preprocess_data(historical_data)
    # Train machine learning model
    model = train_model(X, y)
    
    # Get current time and weather (you can integrate weather API here)
    current_time = datetime.datetime.now()
    weather = "sunny"  # Sample weather, replace with actual weather data
    
    # Predict wait time
    predicted_wait_time = predict_wait_time(model, current_time, weather)
    
    print(f"Predicted wait time for {current_time.strftime('%Y-%m-%d %H:%M')} in {weather} weather: {predicted_wait_time} minutes")

if __name__ == "__main__":
    main()