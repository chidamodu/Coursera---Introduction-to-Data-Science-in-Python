import pandas as pd
df = pd.read_csv('olympics.csv', index_col=0, skiprows=1) #reading the file 'olympics.csv' by setting the column at 0th position as index column and skipping the first row
for col in df.columns: #looping through columns to replace column names
    if col[:2]=='01': #checking if first two characters are equal to '01'. If yes then go to next step of renaming the column name
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True) #the first four characters, starting from 0th position to ending at 3rd position, are replaced with 'Gold' and the remaining characters are added to the new first four characters. inplace means:reciprocate the change in the dataset rather than returning a copy
    if col[:2]=='02':#checking if first two characters are equal to '02'. If yes then go to next step
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True) #as explained above the first four characters of the corresponding column name get substituted
    if col[:2]=='03':#checking if first two characters are equal to '01'. If yes then go to next step
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True) #similar procedure as explained above
    if col[:1]=='№':#similar procedure as explained above but only one character is verified equal or not to a specified value
        df.rename(columns={col:'#'+col[1:]}, inplace=True) #only the first character is replaced with '#' and the remaining characters are added to the new, chnaged, character

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index) 
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)
df = df.drop('Totals') #column 'Totals' is dropped off the dataset, but not deleted though
df['Country']=df.index #Country values in the index column is preserved as a separate column with a name 'Country'. So there will be two columns of similar contents: one under column name 'Country' and another as index column
df=df.set_index('Country') #here 'Country' column is made as the index column
df=df.reset_index() #by resetting index, column 'Country' is made as the first column starting at 0th position 
df.head(5) #the first 5 records are displayed
