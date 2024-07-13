# Universal Analytics Data Consolidation and Analysis

## Project Overview

This project focuses on consolidating and analyzing data from multiple Universal Analytics reports using Python. We leverage powerful data manipulation and visualization libraries to gain insights from the consolidated data.

## Key Features

1. Data Consolidation: Merges multiple Universal Analytics CSV reports into a single, comprehensive dataset.
2. Data Cleaning: Processes and standardizes the data for analysis.
3. Advanced Analysis: Utilizes Python libraries for in-depth data exploration and visualization.

## Technologies Used

- Python 3.x
- Pandas: For data manipulation and analysis
- Seaborn: For statistical data visualization
- Plotly: For interactive, publication-quality graphs
- Jupyter Notebook: For interactive development and data exploration

## Project Structure

- `functions.py`: Contains utility functions for data processing and consolidation.
- `UA-data-consolidation-and-analysis.ipynb`: Contains the main logic where you read, clean up and plot the data. Save the plots so that they can be used by your summary report.
- `Summary report`: Create it based on the example, add it to the Output folder and adjust the paths to match the name of your plots.
- `data/`: Directory containing the raw Universal Analytics CSV reports. THIS BRANCH IS GITIGNORED ADD YOUR OWN DATA HERE.
- `output/`: Directory where the consolidated CSV file is saved. THIS BRANCH IS GITIGNORED ADD YOUR OWN DATA HERE.

## Getting Started

1. Clone this repository.
2. Install the required Python libraries:
pip install pandas seaborn plotly jupyter
3. Place your Universal Analytics CSV reports in the `data/` directory.
4. Open the Jupyter notebook and adjust the folder names for your desired folders to import the data correctly.

## Data Analysis
The Jupyter notebooks demonstrate various analyses, including:

Trend analysis of key metrics over time
Comparison of different traffic sources
Visualization of user engagement metrics
Correlation analysis between different data points

## Customization
You can easily extend the analysis by adding new Jupyter notebooks or modifying the existing ones. The consolidated dataset provides a solid foundation for a wide range of analytical approaches.

## Contributing
Contributions to improve the data consolidation process or add new analyses are welcome. Please submit a pull request with your proposed changes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
