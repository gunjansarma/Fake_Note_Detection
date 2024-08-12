# Banknote Authentication Dataset Analysis

## Overview

This project focuses on analyzing the Banknote Authentication dataset using unsupervised learning techniques to identify patterns and classify banknotes. The primary goal is to evaluate the effectiveness of K-Means clustering in separating genuine banknotes from counterfeit ones. The analysis includes clustering the data, visualizing the results, and providing recommendations for improving authentication systems.

## Contents

- [Project Description](#project-description)
- [Data](#data)
- [Methods](#methods)
- [Results](#results)
- [Recommendations](#recommendations)
- [Usage](#usage)
- [Installation](#installation)
- [License](#license)

## Project Description

This project leverages the Banknote Authentication dataset to perform clustering analysis with K-Means. The dataset features attributes related to banknote images, which are used to group banknotes into clusters to identify patterns indicative of authenticity. The project aims to improve the accuracy of banknote authentication systems by analyzing clustering results.

## Data

The Banknote Authentication dataset includes the following attributes:
- **Variance**: Dispersion of pixel values in the banknote image.
- **Skewness**: Asymmetry of the pixel value distribution.
- **Curtosis**: Peakedness of the pixel value distribution.
- **Entropy**: Randomness in the pixel value distribution.

For this project, we focused on the Variance and Skewness attributes to perform clustering analysis.

## Methods

1. **Data Preparation**:
   - Extracted relevant features from the dataset.
   - Constructed a feature matrix with Variance and Skewness.

2. **Clustering Analysis**:
   - Applied K-Means clustering with a specified number of clusters (2).
   - Visualized clusters and cluster centers using scatter plots.

3. **Evaluation**:
   - Calculated silhouette scores to assess clustering quality.
   - Analyzed cluster separation and overlap through visual inspection.

## Results

- **Silhouette Score**: The clustering analysis yielded a silhouette score of approximately 0.43, indicating moderate separation between clusters.
- **Visualization**: Clusters were visualized based on Variance and Skewness, showing reasonable separation with some overlap.

## Recommendations

1. **Refinement of Clustering Approach**:
   - Experiment with different numbers of clusters for improved results.

2. **Additional Features**:
   - Incorporate features like Curtosis and Entropy to enhance clustering performance.

3. **Alternative Algorithms**:
   - Explore other clustering algorithms (e.g., DBSCAN, Agglomerative Clustering) for comparison.

4. **Validation**:
   - Perform supervised validation if true labels are available for assessing clustering accuracy.

## Usage

To run the analysis, use the provided Python scripts and Jupyter notebooks in this repository. Make sure to install the required dependencies listed in `requirements.txt`.

