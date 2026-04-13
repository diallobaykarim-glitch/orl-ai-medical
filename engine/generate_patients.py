import random
import pandas as pd
import os

output_path = os.path.join("data", "patients_1111.csv")

def generate_patient(i):
    age = random.randint(20, 85)
    cancer = random.choice([0, 1])

    larynx = 1 if cancer == 1 and random.random() > 0.3 else 0
    parotide = 1 if cancer == 1 and random.random() > 0.5 else 0
    ethmoide = 1 if cancer == 1 and random.random() > 0.6 else 0

    score = age // 20 + cancer + larynx + parotide + ethmoide

    if score >= 5:
        classe = "Malin"
    elif score >= 3:
        classe = "Suspect"
    else:
        classe = "Benin"

    return {
        "id": i,
        "age": age,
        "cancer": cancer,
        "larynx": larynx,
        "parotide": parotide,
        "ethmoide": ethmoide,
        "classe": classe,
        "score": score
    }

data = [generate_patient(i) for i in range(1, 1112)]

df = pd.DataFrame(data)

df.to_csv(output_path, index=False)

print("✅ 1111 patients générés :", output_path)