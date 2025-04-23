
---

## 📌 Objectives

- Collect and prepare real-world SpaceX launch data from **REST APIs**, **web scraping**, and **SQL databases**.
- Analyze launch trends, booster performance, and orbit outcomes via **EDA & visualization**.
- Create **interactive maps** using `Folium` and dashboards using `Plotly Dash`.
- Build and evaluate **machine learning classification models** to predict launch success.

---

## 🔍 Data Sources

- **SpaceX REST API**
- **Wikipedia (launch history) – Web Scraping**
- **CSV/SQLite** database for cleaned and structured analysis

---

## 🧪 Key Techniques

- **Data Collection & Wrangling:** API access, BeautifulSoup scraping, and SQL queries
- **Exploratory Data Analysis:** Pandas, Matplotlib, Seaborn, Plotly
- **Interactive Mapping:** `folium` for launch site proximity and outcomes
- **Dashboarding:** `Dash by Plotly` for real-time analytics
- **Machine Learning Models:** Logistic Regression, Decision Trees, KNN, SVM

---

## 📈 Results Highlights

- **KSC LC-39A** has the **highest launch success rate (~77%)**.
- Most successful missions target **SSO and GEO** orbits.
- Booster versions **F9 B5** and payload range **2000–6000kg** have strong success patterns.
- Predictive models reached **92%+ accuracy** on unseen test data.

---

## 🗺️ Visual Demos

> Screenshots from the dashboard and interactive map:
- 📊 Pie charts of launch success per site
- 🌐 Folium maps showing site proximity to roads, railways, and coastlines
- 📈 EDA visualizations for payload correlation and orbit success

---

## 🛠️ Technologies Used

- Python (Pandas, NumPy, Scikit-learn)
- Plotly Dash, Matplotlib, Seaborn
- SQLite, SQLAlchemy
- Folium, Geopy
- JupyterLab

---

## 📎 References

- [SpaceX API Documentation](https://github.com/r-spacex/SpaceX-API)
- [Coursera: IBM Data Science Professional Certificate](https://www.coursera.org/professional-certificates/ibm-data-science)

---

## 🚀 Live Demo / Deployment

> _To run the Dash app locally:_

```bash
python spacex-dash-app.py
