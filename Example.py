# Importing required libraries
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform

# Streamlit App Title
st.title("Uniform Continuous Distribution Visualization")

# Sidebar for user input
st.sidebar.header("Uniform Distribution Parameters")
lower_bound = st.sidebar.number_input("Lower Bound (a):", value=0, step=5)
upper_bound = st.sidebar.number_input("Upper Bound (b):", value=60, step=5)

# Ensure the upper bound is greater than the lower bound
if lower_bound >= upper_bound:
    st.error("Upper bound must be greater than lower bound.")
else:
    # Create uniform distribution with specified bounds
    uniform_dist = uniform(loc=lower_bound, scale=upper_bound - lower_bound)

    # Generate x values for plotting the distribution
    x = np.linspace(lower_bound - 1, upper_bound + 1, 1000)
    y = uniform_dist.pdf(x)

    # Plotting the Uniform Distribution
    fig, ax = plt.subplots()
    ax.plot(x, y, color="blue", lw=2, label="PDF")
    ax.fill_between(x, y, where=(x >= lower_bound) & (x <= upper_bound), color="skyblue", alpha=0.4)
    ax.axvline(lower_bound, color="red", linestyle="--", lw=1, label="Lower Bound (a)")
    ax.axvline(upper_bound, color="green", linestyle="--", lw=1, label="Upper Bound (b)")
    ax.set_title("Uniform Continuous Distribution (a, b)")
    ax.set_xlabel("x")
    ax.set_ylabel("Probability Density")
    ax.legend()

    # Display the plot
    st.pyplot(fig)

    # Display key statistics
    mean = uniform_dist.mean()
    variance = uniform_dist.var()
    st.write("### Key Statistics")
    st.write(f"Mean (μ): {mean:.2f}")
    st.write(f"Variance (σ²): {variance:.2f}")
    st.write(f"Lower Bound (a): {lower_bound}")
    st.write(f"Upper Bound (b): {upper_bound}")

    # Additional Insights
    st.write("### Insights")
    st.write("The uniform continuous distribution is defined between the lower bound (a) and the upper bound (b).")
    st.write("The probability density is constant within this interval, meaning each value is equally likely.")
