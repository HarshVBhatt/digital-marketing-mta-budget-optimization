# Multi-Touch Attribution Analysis Budget Optimization for Digital Marketing Channels

## Overview

This project implements a comprehensive marketing attribution analysis framework to evaluate the effectiveness of different marketing channels and optimize budget allocation. Using a [dataset](https://www.dropbox.com/scl/fo/jrw7atq517jxzqrn2gxz5/ALfzBkRA90d2z7UmLcLqQRs?rlkey=6qg8wfcdrwuy9kfya6kejcq11&e=3&dl=0) of 586,737 customer interactions from 240,108 unique users, the analysis applies various attribution models to determine how different marketing channels contribute to conversions. A streamlit-based app allows users to simulate the budget allocation for various attributions and objectives

## Problem Statement

In digital marketing, customer journeys typically involve multiple touchpoints across various channels before conversion. This project addresses the challenge of accurately attributing conversion credit to each touchpoint in a user's journey, enabling data-driven decisions about resource allocation and marketing investment.

## Features

- **Multi-touch Attribution Models**: Implementation of various attribution methodologies:
  - Heuristic models (First-touch, Last-touch, Linear, Position-based)
  - Probabilistic models (Markov Chain)
  
- **Data Transformation Pipeline**: Processes raw impression and conversion data into structured customer journey paths

- **Visualization Dashboard**: Comparative analysis of different attribution models using Seaborn and Plotly

- **Budget Optimization Algorithm**: SciPy-based optimization to maximize conversion rates while respecting budget constraints

- **Non-linear Conversion Modeling**: Accounts for diminishing returns in marketing spend with channel-specific response rates
- 
## Installation

```bash
# Clone the repository
git clone https://github.com/HarshVBhatt/digital-marketing-mta-budget-optimization.git
cd marketing-attribution

# Install required packages
pip install ChannelAttribution pandas numpy matplotlib seaborn plotly scipy streamlit
```

## Usage

The main analysis is contained in analysis.ipynb that walks through:

1. Data loading and preprocessing
2. Manual implementataion of attribution models
3. Advanced attribution using the ChannelAttribution library
4. Visualization of attribution results
5. Budget optimization

The app.py file runs a simulation to allocate optimal budget for various channels by changing various aspects such as attribution type, objective, decay rates for channels and total budget to be allocated. Navigate to the local repo where the jupyter notebook and the app.py files are located and enter the following command in terminal to run the app:

```bash
streamlit run app.py
```

Various parameters can be adjusted in the simulation to analyze how they impact budget optimization

## Visualizations

The project includes several visualizations:
- Comparison of attribution models across channels
- Transition probability heatmaps
- Budget allocation recommendations

## Future Work

- Implement more sophisticated attribution models (e.g., Shapley value)
- Incorporate time decay factors in attribution
- Develop a dynamic budget allocation system that adapts to changing channel performance
- Add A/B testing framework to validate attribution findings
