# Know Your Health - ML Model Project Structure

## 📋 Project Overview
A Flask-based web application for health risk assessment using Machine Learning. Users can assess their BMI, heart attack risk, and diabetes risk through interactive forms with ML model predictions.

---

## 📁 Project Directory Structure

```
Know_Your_Health_MLModel/
│
├── 📄 app.py                          # Main Flask application entry point
├── 📄 db_config.py                    # Database configuration
├── 📄 requirements.txt                # Python dependencies
├── 📄 README.md                       # Project documentation
│
├── 📂 dataset/                        # Machine Learning datasets
│   ├── diabetes.csv                   # Diabetes dataset for model training
│   ├── hear_dataset.csv               # Heart disease dataset for model training
│   └── Notes.txt                      # Dataset documentation
│
├── 📂 models/                         # ML models and prediction functions
│   ├── __init__.py
│   ├── bmi_calculate.py               # BMI calculation logic
│   ├── heart_model.py                 # Heart attack risk prediction function
│   ├── diabetes.joblib                # Trained diabetes model (serialized)
│   ├── HeartPred.joblib               # Trained heart attack model (serialized)
│   ├── heart_atack_model.pkl          # Heart attack model (pkl format)
│   └── __pycache__/
│
├── 📂 routes/                         # Flask route handlers (Blueprint modules)
│   ├── __init__.py
│   ├── main_routes.py                 # Home page and main navigation routes
│   ├── bmi_routes.py                  # BMI calculation routes & logic
│   ├── heart_routes.py                # Heart attack assessment routes & logic
│   ├── diabetes_routes.py             # Diabetes risk assessment routes & logic
│   ├── login_routes.py                # User authentication/login routes
│   ├── register_route.py              # User registration routes
│   ├── user_profile.py                # User profile management routes
│   ├── google_auth.py                 # Google OAuth authentication
│   └── __pycache__/
│
├── 📂 templates/                      # HTML Jinja2 templates
│   ├── base.html                      # Base template (navbar, footer, inherited by all pages)
│   ├── home.html                      # Home/landing page
│   ├── login.html                     # Login page
│   ├── register.html                  # Registration page
│   ├── profile.html                   # User profile page
│   ├── BMI.html                       # BMI assessment form & results
│   ├── heart.html                     # Heart attack assessment form & results
│   ├── diabetes.html                  # Diabetes risk assessment form & results
│   └── learnmore.html                 # Educational information page
│
├── 📂 static/                         # Static assets (CSS, images)
│   ├── 📂 CSS/                        # Stylesheet files
│   │   ├── home.css                   # Home page responsive styling
│   │   ├── navbar.css                 # Navigation bar styling
│   │   ├── login_page.css             # Login/register page styling
│   │   ├── profile.css                # User profile page styling
│   │   ├── bmi.css                    # BMI assessment page styling
│   │   ├── heart_page.css             # Heart assessment page styling
│   │   └── diabetes.css               # Diabetes assessment page styling
│   │
│   ├── 📂 images/                     # Image assets
│   │
│   ├── 📂 img/                        # Additional images
│   │   └── 📂 service/                # Service icons/images
│   │
│
├── 📂 train/                          # ML model training notebooks
│   ├── diabetes_nootebook.ipynb       # Diabetes model training Jupyter notebook
│   ├── heart.ipynb                    # Heart attack model training Jupyter notebook
│   └── (Other training scripts)
│
├── 📂 myenv/                          # Python virtual environment
│   ├── pyvenv.cfg
│   ├── 📂 Include/
│   ├── 📂 Lib/                        # Installed Python packages
│   │   └── site-packages/
│   ├── 📂 Scripts/                    # Virtual environment executables
│   │   ├── activate
│   │   ├── Activate.ps1               # PowerShell activation
│   │   ├── deactivate.bat
│   │   └── python.exe
│   │
│   └── 📂 share/
│       └── jupyter/
│
└── 📂 __pycache__/                    # Python cache files

```

---

## 🔑 Key Files Explained

### Core Application Files
| File | Purpose |
|------|---------|
| `app.py` | Main Flask app initialization, blueprint registration, server setup |
| `db_config.py` | Database connection configuration (MySQL/MySQLdb) |
| `requirements.txt` | All Python package dependencies |

### Routes (Business Logic)
| File | Functionality |
|------|--------------|
| `routes/main_routes.py` | Home page, navigation, general page routing |
| `routes/bmi_routes.py` | BMI form submission, calculation, result display |
| `routes/heart_routes.py` | Heart attack form, ML prediction, result formatting |
| `routes/diabetes_routes.py` | Diabetes risk form, ML prediction, result display |
| `routes/login_routes.py` | Login form handling, session management |
| `routes/register_route.py` | User registration, data validation |
| `routes/user_profile.py` | User profile viewing/editing |
| `routes/google_auth.py` | Google OAuth 2.0 authentication |

### ML Models
| File | Purpose |
|------|---------|
| `models/bmi_calculate.py` | BMI calculation function (no ML model) |
| `models/heart_model.py` | Loads heart attack model, provides prediction |
| `models/diabetes.joblib` | Trained diabetes classifier (RandomForest) |
| `models/heart_atack_model.pkl` | Trained heart attack classifier |

### Templates
| File | Purpose |
|------|---------|
| `templates/base.html` | Base template with navbar, footer, CSS/JS includes |
| `templates/BMI.html` | BMI form with result display and info cards |
| `templates/heart.html` | Heart attack assessment form with result card |
| `templates/diabetes.html` | Diabetes risk assessment form |
| `templates/login.html` | Clean login page with Google OAuth button |
| `templates/register.html` | User registration form |
| `templates/profile.html` | User profile and account settings |

### Styling
| File | Purpose |
|------|---------|
| `static/CSS/home.css` | Home page: hero section, service cards, responsive |
| `static/CSS/navbar.css` | Navigation bar: sticky, responsive menu |
| `static/CSS/login_page.css` | Login: white card, form inputs, Google button |
| `static/CSS/bmi.css` | BMI page: form card, result card, info section |
| `static/CSS/heart_page.css` | Heart page: organized form sections, result display |

---

## 🔄 Data Flow

### User Assessment Flow
```
1. User navigates to assessment page (BMI/Heart/Diabetes)
   ↓
2. User fills out form in HTML template
   ↓
3. Form submitted via POST to corresponding route
   ↓
4. Route extracts form data and validates
   ↓
5. Route calls ML model function with user data
   ↓
6. Model returns prediction (0 or 1, numpy array)
   ↓
7. Route converts prediction to user-friendly message
   ↓
8. Route renders template with result
   ↓
9. Result displays in Result Card on webpage
```

### Example: Heart Attack Assessment
```
user submits form → heart_routes.py → heart_model.py 
→ heart_atack_model.pkl → prediction → "High/Low Risk" 
→ heart.html result card
```

---

## 💾 Dataset & Training

### Training Notebooks Location
- **Diabetes Model**: `train/diabetes_nootebook.ipynb`
- **Heart Attack Model**: `train/heart.ipynb`

### Dataset Location
- **Diabetes Dataset**: `dataset/diabetes.csv`
- **Heart Dataset**: `dataset/hear_dataset.csv`

### Model Training Process
1. Notebooks load CSV datasets
2. Data preprocessing & feature engineering
3. Model training (RandomForest Classifier)
4. Model evaluation on test set
5. Model serialization (`.joblib` or `.pkl`)

---

## 🎨 Frontend Features

### Responsive Design
- Mobile-first approach using CSS `clamp()` for fluid scaling
- Breakpoints: 768px (tablet), 576px (mobile), 480px (small mobile)
- Grid layouts using CSS Grid and Flexbox

### Color Scheme
- **Primary**: Blue (#3b82f6) for interactive elements
- **Heart Theme**: Red (#ef4444) for heart assessment pages
- **Success**: Green (#10b981) for positive indicators
- **Warning**: Amber (#f59e0b) for caution indicators

### Form Styling
- Clean white card backgrounds
- Bordered input fields with focus states
- Gradient buttons with hover effects
- Section-based organization with headers

---

## 🔐 Authentication & Session

### User Authentication
- Flask session management
- Login/Register routes handle user credentials
- Google OAuth 2.0 integration for social login
- Session checks before accessing assessment pages

### Protected Routes
- All assessment pages require user login
- Session validation in route handlers
- Flash messages for user feedback

---

## 📦 Dependencies

Key packages used:
- **Flask**: Web framework
- **Flask-MySQLdb**: Database connectivity
- **scikit-learn**: ML model training & predictions
- **joblib**: Model serialization/deserialization
- **pandas**: Data manipulation
- **numpy**: Numerical operations
- **matplotlib**: Data visualization (training)
- **Authlib**: OAuth authentication

See `requirements.txt` for complete list.

---

## 🚀 How to Run

1. **Activate Virtual Environment**
   ```bash
   myenv\Scripts\activate.bat  # Windows Command Prompt
   # OR
   myenv\Scripts\Activate.ps1  # Windows PowerShell
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Flask App**
   ```bash
   python app.py
   ```

4. **Access Application**
   ```
   http://localhost:5000
   ```

---

## 📊 Assessment Features

### 1. BMI Assessment
- **Inputs**: Height, Weight
- **Output**: BMI category (Underweight, Normal, Overweight, Obese)
- **Location**: `/templates/BMI.html`, `/routes/bmi_routes.py`

### 2. Heart Attack Risk
- **Inputs**: 15 health parameters (age, blood pressure, cholesterol, etc.)
- **Output**: High/Low risk prediction
- **Model**: RandomForest Classifier (trained on heart disease data)
- **Location**: `/templates/heart.html`, `/routes/heart_routes.py`

### 3. Diabetes Risk
- **Inputs**: 8 health parameters (glucose, BMI, age, etc.)
- **Output**: Risk prediction
- **Model**: Trained classifier on diabetes dataset
- **Location**: `/templates/diabetes.html`, `/routes/diabetes_routes.py`

---

## 🛠️ Development Notes

### File Naming Conventions
- Routes: `*_routes.py`
- Models: `*_model.py`
- CSS: `*_page.css` or `*.css`
- Templates: `*.html` (capitalized for pages like BMI.html)

### Template Inheritance
All pages extend `base.html`:
```html
{% extends 'base.html' %}
{% block content %}
  <!-- Page-specific content -->
{% endblock %}
```

### URL Routing Examples
- Home: `/` (main_routes.py)
- Login: `/login` (login_routes.py)
- BMI Assessment: `/bmi` (bmi_routes.py)
- Heart Assessment: `/heart_attack` (heart_routes.py)
- Diabetes Assessment: `/diabetes` (diabetes_routes.py)

---

## 📝 Project Statistics

- **Total Routes**: 6+ blueprint modules
- **Templates**: 8 HTML pages
- **Stylesheets**: 6 CSS files
- **ML Models**: 2 trained models
- **Assessment Types**: 3 (BMI, Heart, Diabetes)
- **Responsive Breakpoints**: 3 (768px, 576px, 480px)

---

## ✨ Key Features Summary

✅ User authentication (Email + Google OAuth)  
✅ Three ML-based health assessments  
✅ Responsive mobile-first design  
✅ Clean white card UI with professional styling  
✅ Real-time form validation  
✅ User profile management  
✅ Database integration for user storage  
✅ Color-coded health indicators  
✅ Educational information sections  
✅ Health tips and recommendations  

---

**Last Updated**: December 8, 2025
