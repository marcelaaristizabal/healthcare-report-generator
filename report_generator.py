import csv

def read_patients(filename):
    patients = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            patients.append(row)
    return patients

def generate_report(patients):
    total = len(patients)
    
    # Calcular promedio de edad
    ages = [int(p['age']) for p in patients]
    avg_age = sum(ages) / len(ages)
    
    # Contar por género
    males = len([p for p in patients if p['gender'] == 'M'])
    females = len([p for p in patients if p['gender'] == 'F'])
    
    # Diagnóstico más común
    diagnoses = [p['diagnosis'] for p in patients]
    most_common = max(set(diagnoses), key=diagnoses.count)
    
    print("="*50)
    print("HEALTHCARE REPORT")
    print("="*50)
    print(f"Total patients: {total}")
    print(f"Average age: {avg_age:.1f} years")
    print(f"Gender distribution: {males} males, {females} females")
    print(f"Most common diagnosis: {most_common}")
    print("="*50)

if __name__ == "__main__":
    patients = read_patients('data/patients.csv')
    generate_report(patients)