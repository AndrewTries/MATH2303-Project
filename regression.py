import pandas as pd

file_path = "Kidney_Organ_SupplyChain_RawDataset.csv"
df = pd.read_csv(file_path)

Donor_Medical_Approval = []
for i in df['Donor_Medical_Approval']:
    Donor_Medical_Approval.append(i.replace(i, str(1 if i == 'Yes' else 0)))
Match_Status = []
for i in df['Match_Status']:
    Match_Status.append(i.replace(i, str(1 if i == 'Yes' else 0)))
Organ_Condition_Alert = []
for i in df['Organ_Condition_Alert']:
    Organ_Condition_Alert.append(i.replace(i, str(1 if i == 'Yes' else 0)))
    
df_clean = df
df_clean['Donor_Medical_Approval'] = Donor_Medical_Approval
df_clean['Match_Status'] = Match_Status
df_clean['Organ_Condition_Alert'] = Organ_Condition_Alert

columns_to_drop = ['Organ_Required', 'Organ_Donated', 'Donor_Min_Age', 'Donor_Max_Age', 'Donor_Min_Weight', 'Donor_Max_Weight']
df_clean.drop(columns=columns_to_drop, inplace=True)


dummie_columns = ['Patient_BloodType', 'Donor_BloodType', 'Diagnosis_Result', 'Organ_Status']
df_clean = pd.get_dummies(df_clean, columns=dummie_columns, dtype=int)
print(df_clean.head)
    
    
# print(df['Patient_ID', 'Patient_Age', 'Patient_Weight', 'Patient_BMI',
#        'Patient_BloodType', 'Organ_Required', 'Diagnosis_Result',
#        'Biological_Markers', 'Organ_Status', 'Donor_ID', 'Donor_Age',
#        'Donor_Weight', 'Donor_BloodType', 'Organ_Donated',
#        'Donor_Medical_Approval', 'Donor_Min_Age', 'Donor_Max_Age',
#        'Donor_Min_Weight', 'Donor_Max_Weight', 'Match_Status',
#        'RealTime_Organ_HealthScore', 'Organ_Condition_Alert',
#        'Predicted_Survival_Chance', 'Organ_Tracking_ID',
#        'Timestamp_Organ_Scanned'])

