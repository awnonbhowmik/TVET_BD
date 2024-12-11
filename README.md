# TVET Survey Analysis

This repository contains scripts and resources for analyzing the **State of Technical and Vocational Education and Training (TVET) in Bangladesh** dataset. The analysis focuses on understanding trends, identifying correlations, and visualizing data to provide insights into educational qualifications, training completion rates, teaching methods, and departmental trends.

## Features

- **Data Cleaning**: Removes redundant or unnecessary columns for streamlined analysis.
- **Descriptive Analysis**: Summarizes key variables and their distributions.
- **Visualization**:
  - Pie charts for educational qualifications.
  - Bar charts for training completion trends.
  - Heatmaps for correlations.
- **Departmental Comparisons**: Identifies differences in practices like blended learning usage.

## Dataset
The dataset includes responses from TVET teachers and staff in Bangladesh. Key fields include:

- **Educational Qualification**: Highest degree earned (e.g., Bachelor's, Master's).
- **Training and Certifications**: Details of completed workshops and certifications.
- **Institution**: Affiliated institution of respondents.
- **Teaching Practices**: Usage of Bloom's Taxonomy and blended learning methods.
- **Department**: Department type (e.g., Non-Technical, Chemical).

## Repository Structure
```
TVET-Analysis/
├── data/
│   ├── TVET_Teachers.xlsx            # Original dataset
├── scripts/
│   ├── analysis.py                   # Statistical and descriptive analysis
├── images/                           # Output visualizations
├── README.md                         # Project overview and setup instructions
```

## Getting Started

### Prerequisites
- Python 3.8+
- Required libraries:
  - `pandas`
  - `matplotlib`
  - `seaborn`

Install dependencies using:
```bash
pip install -r requirements.txt
```

### Running the Scripts

1. **Data Cleaning**:
   ```bash
   python scripts/data_cleaning.py
   ```

2. **Generate Visualizations**:
   ```bash
   python scripts/visualization.py
   ```

3. **Statistical Analysis**:
   ```bash
   python scripts/analysis.py
   ```

## Example Visualizations
- **Educational Qualification Distribution**:
  A pie chart with coolwarm color palette and annotations inside slices.
- **Training Completion Trends**:
  Bar chart showing rates of training participation across departments.

## Future Work
- Incorporate predictive analysis to forecast training needs.
- Develop dashboards for interactive exploration of results.
- Integrate additional datasets for cross-sectional analysis.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License.
