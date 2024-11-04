# Import Streamlit
import streamlit as st

# App Title
st.title("Project 2: Data Dashboard Project with Streamlit")

# Project Overview
st.write("""
### Project Overview
In this project, you'll create an interactive data dashboard using **Streamlit**. The goal is to showcase your ability to analyze and visualize data with an interactive web app. Choose a dataset that interests you, and build a dashboard to present insights through charts and interactive elements.
""")

# Project Requirements
st.write("""
---

### Project Requirements

Your app should meet the following requirements:

1. **Data Selection**: Choose any dataset that interests you and upload it into your Streamlit app.
2. **Dashboard Visuals**:
   - Include **at least four visualizations** to help users understand key insights from your dataset.
   - Suggested charts: line charts, bar charts, histograms, pie charts, maps, scatter plots, etc.
3. **Interactive Elements**:
   - Include **at least two advanced interactive components** (e.g., sliders, checkboxes, radio buttons, or dropdown menus).
   - These components should allow users to explore different parts of the data dynamically.
4. **Documentation and Hosting**:
   - Create a `requirements.txt` file listing all libraries your app uses.
   - Host your app on GitHub and deploy it on **Streamlit Cloud** (`share.streamlit.io`).
""")

# Steps to Complete the Project
st.write("""
---

### Steps to Complete the Project

1. **Set Up the App File**:
   - Name your main app file `app.py`.
   - Import necessary libraries (`streamlit`, `pandas`, `matplotlib`, `seaborn`, or `altair`).
   - Load and preprocess your dataset if necessary, and design the layout with visualizations and interactivity.

2. **Add Visualizations**:
   - Ensure your app has **four or more different visualizations** revealing insights from your data.
   - Label charts and add titles for clarity.

3. **Add Interactive Components**:
   - Implement at least **two interactive elements** (sliders, checkboxes, dropdowns, etc.).
   - Use these components to make your app dynamic and user-friendly.

4. **Create a Requirements File**:
   - In the root folder, create a `requirements.txt` file listing your app’s dependencies.
   
   Example:
   ```plaintext
   streamlit
   pandas
   matplotlib
   seaborn ```


5. **Host on GitHub**:

Push/upload your project files (including `app.py` and `requirements.txt`) to a public GitHub repository.

6. **Deploy on Streamlit Cloud**:

Go to Streamlit Cloud and connect it to your GitHub repository to deploy the app.
You’ll receive a shareable link to your deployed app once it's live. """)

st.write("""
### Submission Requirements
Please submit the following:

- App File (`app.py`): Your main Streamlit app file.
- Requirements File (`requirements.txt`): A file listing the app’s dependencies.
- GitHub Repository Link: The link to your public GitHub repository containing all project files.
- Streamlit Deployment Link: The link to your live app deployed on Streamlit Cloud.
- A `pdf` file containing at least four screenshots of the most important aspects of your running app.
""")

st.write("""
### Hosting and Deployment Instructions
To deploy your app on Streamlit Cloud:

- Go to Streamlit Cloud and sign in with your GitHub account.
- In Streamlit Cloud, select New App and choose your repository and branch containing app.py.
- Set the main file path to `app.py`.
- Click Deploy. Your app will be live in a few moments, and you’ll receive a shareable link.
- Important: Ensure all necessary libraries are listed in your `requirements.txt`, so your app runs correctly in the cloud environment. """)

st.write("""
### Grading Rubric

Your project will be graded based on the following criteria:

| **Criteria**                     | **Points** | **Description**                                                                                   |
|----------------------------------|------------|---------------------------------------------------------------------------------------------------|
| **Data Selection**               | 10         | Dataset is appropriate, interesting, and well-preprocessed if needed.                             |
| **Visualization Variety**        | 40         | Includes at least four clear, principally correct, well-labeled, and informative visualizations.                        |
| **Interactivity**                | 20         | At least two interactive components (sliders, checkboxes, etc.) that enhance data exploration.    |
| **Design and Layout**            | 10         | App layout is organized, easy to navigate, and visually appealing.                                |
| **Requirements File**            | 5         | Includes a `requirements.txt` file that correctly lists all dependencies.                         |
| **Hosting and Deployment**       | 5         | App is hosted on GitHub and deployed successfully on Streamlit Cloud.                             |
| **Code Quality and Documentation**| 5         | Code is well-organized, readable, and includes comments as needed.                                |
| **Overall Presentation**         | 5         | The app communicates insights effectively and engages the user.                                   |

**Total Points**: 100
""")


st.write("""
### Tips and Resources
- Explore the [Streamlit documentation](https://docs.streamlit.io/) for tutorials on adding interactivity and visualizations.
- Use visualization libraries like Matplotlib, Seaborn, or Altair to create clear and informative charts.
- Test your app thoroughly to ensure it runs smoothly before deployment.

Good luck, and enjoy building your data dashboard! """)

