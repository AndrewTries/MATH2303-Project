import kagglehub

# Download latest version
path = kagglehub.dataset_download("zoya77/kidney-organ-transplantation-patient-donor-data")

print("Path to dataset files:", path)