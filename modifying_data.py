import pandas as pd

df = pd.read_csv('dataset_1.csv', index_col=0)

df = df[df['Name'].notna()]
df = df[df['Distance (light years)'].notna()]
df = df[df['Mass (Jupiter mass)'].notna()]
df = df[df['Radius (Jupiter Radius)'].notna()]

df['Radius (Jupiter Radius)'] = pd.to_numeric(df['Radius (Jupiter Radius)'])
df['Mass (Jupiter mass)'] = pd.to_numeric(df['Mass (Jupiter mass)'])

df['Radius (Jupiter Radius)'] = df['Radius (Jupiter Radius)']*0.102763
df['Mass (Jupiter mass)'] = df['Mass (Jupiter mass)']*0.000954588

df = df.rename({
    'Radius (Jupiter Radius)': 'Radius (Solar radius)',
    'Mass (Jupiter mass)': 'Mass (Solar mass)'
}, axis='columns')

df.to_csv('dataset_1_modified.csv')