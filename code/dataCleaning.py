
#  Data cleaning, aim to see occupancy rate in this dataset
df['reviews_per_month']=df['reviews_per_month'].fillna(0)

df


# Menambahkan kolom okupansi kedalam dataset
df['Occupied'] = 365 - df['availability_365']


# Mengisi item NaN pada kolom last_review dengan "No Review"
df['last_review'].fillna('No Review', inplace=True)

df

df.info()
