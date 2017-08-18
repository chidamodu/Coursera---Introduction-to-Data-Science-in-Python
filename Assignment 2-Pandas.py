import pandas as pd
df = pd.read_csv('olympics.csv', index_col=0, skiprows=1) #reading the file 'olympics.csv' by setting the column at 0th position as index column and skipping the first row
for col in df.columns: #looping through columns to replace column names
    if col[:2]=='01': #checking if first two characters are equal to '01'. If yes then go to next step of renaming the column name
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True) #the first four characters, starting from 0th position to ending at 3rd position, are replaced with 'Gold' and the remaining characters are inplace means:reciprocate the change in the dataset rather than returning a copy
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index) 
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)
df = df.drop('Totals')
df['Country']=df.index
df=df.set_index('Country')
df=df.reset_index()
df.head(5)