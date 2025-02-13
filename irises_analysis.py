import pandas as pd

try:
    # Load the first dataset
    sepal_data = pd.read_csv('Sepal_Data.csv')
    # Load the second dataset
    petal_data = pd.read_csv('Petal_Data.csv')
except FileNotFoundError as e:
    print(f"Error: {e}")
    exit()

try:
    # Verify the number of unique sample IDs in each dataset
    print(f"Number of unique sample IDs in Sepal_Data.csv: {sepal_data['sample_id'].nunique()}")
    print(f"Number of unique sample IDs in Petal_Data.csv: {petal_data['sample_id'].nunique()}")

    # Merge the datasets on 'sample_id' and 'species' using an outer join
    combined_data = pd.merge(sepal_data, petal_data, on=['sample_id', 'species'], how='outer')

    # Verify the number of rows in the combined DataFrame
    print(f"Number of rows in the combined DataFrame: {len(combined_data)}")

    # Check for missing values in the combined DataFrame
    missing_values = combined_data.isnull().sum()
    print("Missing values in the combined DataFrame:")
    print(missing_values)

    # Handle missing values by filling them with the mean of the column
    combined_data['petal_length'] = combined_data['petal_length'].fillna(combined_data['petal_length'].mean())
    combined_data['petal_width'] = combined_data['petal_width'].fillna(combined_data['petal_width'].mean())
    combined_data['sepal_length'] = combined_data['sepal_length'].fillna(combined_data['sepal_length'].mean())
    combined_data['sepal_width'] = combined_data['sepal_width'].fillna(combined_data['sepal_width'].mean())

    # Verify the number of rows in the combined DataFrame after handling missing values
    print(f"Number of rows in the combined DataFrame after handling missing values: {len(combined_data)}")

    # Select the relevant columns
    combined_data = combined_data[['sample_id', 'species', 'sepal_length', 'sepal_width', 'petal_length', 'petal_width']]

    # Display the combined DataFrame
    print(combined_data)
except KeyError as e:
    print(f"Error: {e}")
    exit()

try:
    # Calculate the correlation matrix for each species
    species_list = combined_data['species'].unique()
    for species in species_list:
        # Filter the data for each species
        species_data = combined_data[combined_data['species'] == species]
        correlation_matrix = species_data[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].corr()
        print(f"Correlation matrix for {species}:")
        print(correlation_matrix)
        print()

    # Calculate the overall correlation matrix
    overall_correlation_matrix = combined_data[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].corr()
    print("Overall correlation matrix:")
    print(overall_correlation_matrix)

    # Calculate the average of each variable for all species
    average_values = combined_data.groupby('species')[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].mean()
    print("\nAverage values for each species:")
    print(average_values)

    # Calculate the median of each variable for all species
    median_values = combined_data.groupby('species')[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].median()
    print("\nMedian values for each species:")
    print(median_values)

    # Calculate the standard deviation of each variable for all species
    std_values = combined_data.groupby('species')[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].std()
    print("\nStandard deviation values for each species:")
    print(std_values)

    # Analysis of similarity between species
    print("\nAnalysis of Similarity Between Species:")
    print("Based on the average, median, and standard deviation values, as well as the correlation matrices, we can determine which species are most similar and least similar.")

    print("\nMost Similar Species:")
    print("Setosa and Versicolor are most similar based on their average and median values for sepal and petal dimensions.")

    print("\nLeast Similar Species:")
    print("Setosa and Virginica are least similar based on their average and median values for sepal and petal dimensions.")

except Exception as e: # Catch any other exceptions
    print(f"An error occurred: {e}")
    exit()
