import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import os

# Get the directory of the Python script
directory = os.path.dirname(os.path.abspath(__file__))

# Define the relative path to the shapefile within the "Province" folder
shapefile_path = os.path.join(directory, "Province", "Province_Boundary_GCS.shp")

# Define the relative path to the CSV file within the "Province" folder
point_path = os.path.join(directory, "Province", "Province_Boundary_GCS.csv")

def main ():
	# Load shapefile of Indonesian provinces
	provinces = gpd.read_file(shapefile_path)

	# Load dataset of capital cities
	capital_cities = pd.read_csv(point_path)

	# Merge data of point and shapefile
	merged_data = provinces.merge(capital_cities, how='left', left_on='PROVINSI', right_on='PROVINSI')

	# Plot the map
	# Create the plot
	fig, ax = plt.subplots(figsize=(10,10))

	# Plot province boundaries
	provinces.plot(ax=ax, color='lightgray', edgecolor= 'black')

	# Plot capital cities
	merged_data.plot(ax=ax, color='honeydew', marker='o', markersize=50)

	# Annotate each point with the name of the province
	for idx, row in merged_data.iterrows():
		centroid_x, centroid_y = row['geometry'].centroid.x, row['geometry'].centroid.y
		plt.annotate(text=row['PROVINSI'], xy=(centroid_x, centroid_y), color='grey', fontsize=4)
		plt.scatter(centroid_x, centroid_y, color='gold', marker='.', s=5)

	# Add title and labels
	plt.title = ('Capital Cities of Indonesian Provinces')
	plt.xlabel= ('Longitude')
	plt.ylabel= ('Latitude')

	# Save the plot to an image file
	plt.savefig('indonesian_province_capital_cities.png', dpi=300, bbox_inches='tight')


	# Show the plot
	plt.show()

if __name__ == "__main__":
	main()