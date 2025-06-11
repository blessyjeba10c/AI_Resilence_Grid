import pandas as pd
import random
from datetime import datetime, timedelta


def simulate_data():
    base_time = datetime.now()
    data = []
    for i in range(20):
        timestamp = base_time + timedelta(minutes=i)
        Wind_Speed = random.randint(60, 200)  # km/h
        rainfall = random.uniform(50, 250)    # mm
        outage_risk = 1 if Wind_Speed > 120 and rainfall > 100 else 0
        power_output = 100 if outage_risk == 0 else random.uniform(10, 50)
        data.append([timestamp, Wind_Speed, rainfall, outage_risk, power_output])
    df = pd.DataFrame(data, columns=["timestamp", "wind_speed", "rainfall", "outage_risk", "power_output"])
    df.to_csv("simulated_data.csv", index=False)
    return df
