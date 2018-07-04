import pandas as pd

data= pd.read_csv("./data/CRDC2013_14.csv", encoding="Latin-1")

data["total_enrollment"] = data["TOT_ENR_M"] + data["TOT_ENR_F"]
all_enrollment = data["total_enrollment"].sum()

races = ["HI", "AM", "AS", "HP", "BL", "WH", "TR"]
genders = ["F", "M"]

totals = {}
gender_race = {}

for race in races:
    race_f = "SCH_ENR_" + race + "_" + genders[0]
    race_m = "SCH_ENR_" + race + "_" + genders[1]
    total_race = "total_" + race
    
    race_enrollment = data[race_m].sum() + data[race_f].sum()
    
    totals[total_race] = 100 *(race_enrollment / all_enrollment)
    
    gender_label = [race_f, race_m]
    for label in gender_label:
        gender_race[label] = 100 * (data[label].sum()/race_enrollment)

for k,v in totals.items():
     print(k,v)
    
for k, v in sorted(gender_race.items()):
    print(k,v)