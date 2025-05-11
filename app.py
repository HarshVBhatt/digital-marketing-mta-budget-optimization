import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

df = pd.read_csv("channel_conversions.csv")

st.title("Marketing Channel Budget Optimizer Simulator")

conv_type = st.selectbox("Select Conversion Attribute Type", ["First", "Last", "Linear", "Markov Chain"])
if conv_type != "Markov Chain":
    conversion_type = f"{conv_type.lower()}_touch_conversions"
else:
    conversion_type = "mma_conversions"

objective_type = st.selectbox("Select Optimization Objective", ["Linear", "Non-linear"])

ideal_rate_dict = {"Facebook": "0.00015-0.0002",
                   "Instagram": "0.0001-0.00013",
                   "Online Display": "0.00007-0.0001",
                   "Online Video": "0.00006-0.00009",
                   "Paid Search": "0.00018-0.00025"}

default_vals = {"Facebook": 0.0002,
                "Instagram": 0.0001,
                "Online Display": 0.00007,
                "Online Video": 0.000067,
                "Paid Search": 0.00025}

decay_rates = {}
if objective_type == 'Non-linear':
    st.markdown("#### Enter Decay Rates for Each Channel")
    for channel in df["channel_name"].unique():
        decay_rates[channel] = st.number_input(
            f"Decay rate for {channel} (Ideal Range: {ideal_rate_dict[channel]})",
            min_value=0.0, max_value=1.0, value=default_vals[channel], step=0.00001, format = "%f"
        )

budget = st.slider(
    "Select Total Budget",
    min_value=5000, max_value=100_000, value=10_000, step=1_000
)


if st.button("Run Optimization"):
    # Select relevant conversion data
    channels = df["channel_name"].to_list()
    conversions = df[conversion_type].to_list()
    attributions = [np.round(c / 100,2) for c in conversions]

    if objective_type == "Non-linear":
        rates = []
        for c in channels:
            rates.append(float(decay_rates[c]))
        rates = np.array(rates)

    def lin_objective(x):
        # Negative sign because minimize() minimizes, but we want to maximize
        return -np.sum(attributions * (x / budget))

    def non_lin_objective(x):
        # x is budget allocation array
        return -np.sum(attributions * (1 - np.exp(-rates * x)))

    def allocate_budget(objective, budget_total = 10000):
        constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - budget_total})

        # Bounds: no negative allocations, no channel gets more than total budget
        bounds = [(0, budget_total) for _ in channels]

        # Initial guess: equal allocation
        x0 = np.array([budget_total / len(channels)] * len(channels))

        # Solve
        if objective == "Non-linear":
            use_objective = non_lin_objective
        else:
            use_objective = lin_objective

        result = minimize(use_objective, x0, bounds=bounds, constraints=constraints)
        optimized_budgets = result.x

        budget_dict = {}
        # Print results
        for ch, alloc in zip(channels, optimized_budgets):
            print(f"Channel: {ch}, Allocated Budget: ${alloc:,.2f}")
            budget_dict[ch] = np.round(alloc, 2)
        
        return budget_dict

    allocated_budgets = allocate_budget(objective=objective_type, budget_total=budget)

    fig, ax = plt.subplots()
    channels = list(allocated_budgets.keys())
    allocations = list(allocated_budgets.values())
    ax.bar(channels, allocations, color='#17c3e2')
    ax.set_xlabel('Channel')
    ax.set_ylabel('Allocated Budget')
    ax.set_title('Budget Allocation per Channel')
    for i in range(len(channels)):
        ax.text(i, allocations[i], allocations[i], ha='center')
    st.pyplot(fig)
    
    # Display allocation as a table
    st.write(pd.DataFrame({
        'Channel': channels,
        'Allocated Budget (in $)': allocations
    }))