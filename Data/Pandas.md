---
tags:
  - Programming
---

```bash
first_sample_dict = df.iloc[0].to_dict()
first_sample_dict

# Print the unique values in the specific column and count how many samples fall under each unique value
unique_values = df['assembly_level'].value_counts()
print(unique_values)

# Filtet value
# Merge the dataframes on 'LID'
merged_df = pd.merge(str, ethnic[['LID', 'Dân tộc']], on='LID', how='inner')
```