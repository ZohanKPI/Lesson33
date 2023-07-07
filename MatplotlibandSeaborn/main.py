import pandas as pd

df = pd.DataFrame({
    'Car Brand': ['Toyota', 'Honda', 'BMW', 'Mercedes', 'Audi', 'Ford', 'Chevrolet', 'Nissan', 'Hyundai', 'Volkswagen',
                  'Subaru', 'Lexus', 'Kia', 'Porsche', 'Jeep', 'Cadillac', 'Maserati', 'Ferrari', 'Bentley', 'Aston Martin'],
    'Cost': [30000, 27000, 35000, 40000, 38000, 32000, 30000, 31000, 28000, 34000,
             32000, 35000, 28000, 80000, 37000, 45000, 75000, 200000, 180000, 150000],
    'Fuel Usage (mpg)': [30, 34, 25, 22, 28, 30, 31, 33, 35, 29,
                         30, 24, 36, 20, 28, 23, 18, 16, 17, 15],
    'Max Speed (mph)': [120, 124, 155, 150, 149, 130, 125, 130, 126, 140,
                        134, 150, 125, 190, 132, 145, 185, 210, 202, 200],
    'Weight Carry Limit (kg)': [800, 700, 600, 750, 650, 850, 850, 800, 750, 700,
                                850, 650, 800, 550, 900, 750, 500, 400, 600, 500]
})

df.to_excel('car_data.xls', index=False)