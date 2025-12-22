
# Quick Lab — Know Your Health




<!-- Project tech badges -->
[![](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white&style=for-the-badge)](https://www.python.org/) [![](https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=white&style=for-the-badge)](https://flask.palletsprojects.com/) [![](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikitlearn&logoColor=white&style=for-the-badge)](https://scikit-learn.org/)

[![](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white&style=for-the-badge)](https://pandas.pydata.org/) [![](https://img.shields.io/badge/numpy-013243?logo=numpy&logoColor=white&style=for-the-badge)](https://numpy.org/) [![](https://img.shields.io/badge/joblib-2F2F2F?style=for-the-badge&logo=data:image/png;base64,)](https://joblib.readthedocs.io/)

[![](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white&style=for-the-badge)](https://developer.mozilla.org/en-US/docs/Web/HTML) [![](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white&style=for-the-badge)](https://developer.mozilla.org/en-US/docs/Web/CSS) [![](https://img.shields.io/badge/Tailwind_CSS-38B2AC?logo=tailwindcss&logoColor=white&style=for-the-badge)](https://tailwindcss.com/)

A Flask-based web app providing quick, easy-to-use health prediction tools and calculators with pre-trained ML models.

Live demo: https://quick-lab.onrender.com/

---

## **About**
- **Quick Lab** bundles lightweight ML-powered endpoints and pages so users can check common health indicators quickly from a browser.
- The app includes calculators and prediction pages for BMI, diabetes, heart attack risk, and cancer risk plus a simple chatbot helper.

---

## **Features**
- **BMI Calculator** — Calculate BMI and show category (Underweight / Normal / Overweight / Obese).
- **Heart Attack Prediction** — Predict risk using age, sex, blood pressure, cholesterol, and other inputs.
- **Diabetes Prediction** — Predicts diabetes likelihood using a trained diabetes model.
- **Cancer Prediction** — Predicts cancer risk using a pre-trained `cancer.pkl` model placed in the `models` folder.
- **Chatbot Helper** — Simple chat interface for guidance and information.
- **User Auth (basic)** — Register / Login pages to manage simple user profiles.
- **Clean responsive UI** — Templates in the `templates/` folder and styles in `static/CSS/`.

---

## **Project Structure (high level)**
- `app.py` — Flask app entrypoint and app factory.
- `routes/` — Flask route handlers (e.g. `heart_routes.py`, `cancer_routes.py`, `diabetes_routes.py`).
- `models/` — Saved ML models and helper code. Example files:
	- `cancer.pkl` — cancer prediction model (loaded by `models/cancer_model.py`).
	- `diabetes.joblib` — diabetes model.
	- `heart_atack_model.pkl` — heart model.
- `dataset/` — CSV datasets used for training and reference (not required for running the site).
- `static/` — CSS, images and front-end assets.
- `templates/` — HTML templates for pages (home, BMI, diabetes, heart, cancer, chatbot, login, profile).

---

## **How the cancer model is loaded**
The app loads the cancer model from the `models` directory. Example code (already used in `models/cancer_model.py`):

```py
import os
import joblib

current_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(current_dir, "cancer.pkl")
model = joblib.load(path)
```

This ensures the code finds `cancer.pkl` regardless of the working directory when the app is started.

---

## **Tech stack & libraries**
- Python 3.10+ (tested in local venv)
- Flask — web framework
- scikit-learn, pandas, numpy — ML + data handling
- joblib — model serialization

See `requirements.txt` for full dependency list.

---

## **Local setup & run**
1. Create and activate a Python virtual environment (Windows example):

```powershell
python -m venv myenv
.\myenv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Run the app locally:

```powershell
python app.py
# or set FLASK_APP and use flask run
```

3. Open `http://127.0.0.1:5000` in your browser.

---

## **Notes & tips**
- Ensure the `models/cancer.pkl` and other model files remain in the `models/` folder. If you move them, update the load path accordingly.
- To update or retrain models, use the notebooks in the `train/` folder and then export the trained model files into `models/`.

---

## **Contributing / Next steps**
- Add tests for prediction endpoints.
- Improve model explainability (show feature importance).
- Add Dockerfile for consistent deployment.

---

If you'd like, I can also:
- generate a polished hero image and place it at `static/images/hero.png` to match the screenshot theme you uploaded,
- or add badges and a compact project card section like the screenshot.



