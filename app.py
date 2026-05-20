# =========================================================
# ADVANCED AI CUSTOMER SUBSCRIPTION PREDICTOR
# PROFESSIONAL STREAMLIT WEB APP
# =========================================================

import streamlit as st
import pandas as pd
import joblib
import time

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI Subscription Predictor",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# LOAD MODEL
# =========================================================

model = joblib.load("subscription_prediction_model.pkl")

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

/* Main Background */
.stApp {
    background: linear-gradient(to right, #141E30, #243B55);
    color: white;
}

/* Main Title */
.main-title {
    font-size: 55px;
    font-weight: bold;
    text-align: center;
    color: white;
    margin-bottom: 10px;
}

/* Subtitle */
.sub-title {
    text-align: center;
    font-size: 22px;
    color: #d1d5db;
    margin-bottom: 40px;
}

/* Card Design */
.card {
    background: rgba(255,255,255,0.08);
    padding: 25px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
    margin-bottom: 25px;
}

/* Metric Cards */
.metric-card {
    background: rgba(255,255,255,0.08);
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.2);
}

/* Button */
.stButton>button {
    width: 100%;
    height: 60px;
    font-size: 22px;
    font-weight: bold;
    border-radius: 15px;
    border: none;
    background: linear-gradient(to right, #00C9FF, #92FE9D);
    color: black;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.03);
}

/* Prediction Box */
.prediction-box {
    padding: 30px;
    border-radius: 20px;
    text-align: center;
    font-size: 30px;
    font-weight: bold;
    margin-top: 30px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #111827;
}

/* Hide Streamlit Footer */
footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">🛍️ AI Customer Subscription Predictor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Predict customer subscription behavior using Machine Learning</div>',
    unsafe_allow_html=True
)

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("📌 Navigation")

menu = st.sidebar.radio(
    "Go To",
    [
        "Prediction",
        "About Project"
    ]
)

# =========================================================
# ABOUT PROJECT
# =========================================================

if menu == "About Project":

    st.markdown("## 📖 About This Project")

    st.info("""
    This AI-powered application predicts whether a customer
    is likely to subscribe based on their shopping behavior.

    ### 🚀 Technologies Used
    - Python
    - Streamlit
    - Machine Learning
    - Scikit-learn
    - Random Forest Classifier

    ### 📊 Features
    ✅ Real-time prediction  
    ✅ Probability analysis  
    ✅ Interactive dashboard  
    ✅ AI-based analytics  
    """)

# =========================================================
# PREDICTION PAGE
# =========================================================

if menu == "Prediction":

    # -----------------------------------------------------
    # INPUT SECTION
    # -----------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.subheader("👤 Customer Information")

        age = st.slider(
            "Age",
            18,
            70,
            25
        )

        gender = st.selectbox(
            "Gender",
            ["Male", "Female"]
        )

        item_purchased = st.selectbox(
            "Item Purchased",
            [
                "Blouse",
                "Sweater",
                "Jeans",
                "Sandals",
                "Shirt",
                "Dress",
                "Shoes",
                "Handbag",
                "Jacket",
                "Jewelry"
            ]
        )

        category = st.selectbox(
            "Category",
            [
                "Clothing",
                "Footwear",
                "Accessories",
                "Outerwear"
            ]
        )

        purchase_amount = st.number_input(
            "Purchase Amount (USD)",
            min_value=1,
            max_value=1000,
            value=120
        )

        location = st.selectbox(
            "Location",
            [
                "California",
                "Texas",
                "Florida",
                "New York",
                "Nevada",
                "Kentucky",
                "Maine"
            ]
        )

        size = st.selectbox(
            "Size",
            ["S", "M", "L", "XL"]
        )

        st.markdown('</div>', unsafe_allow_html=True)

    with col2:

        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.subheader("🛒 Shopping Information")

        color = st.selectbox(
            "Color",
            [
                "Black",
                "Blue",
                "Red",
                "White",
                "Green",
                "Gray",
                "Maroon"
            ]
        )

        season = st.selectbox(
            "Season",
            [
                "Spring",
                "Summer",
                "Autumn",
                "Winter"
            ]
        )

        review_rating = st.slider(
            "Review Rating",
            1.0,
            5.0,
            4.5
        )

        shipping_type = st.selectbox(
            "Shipping Type",
            [
                "Free Shipping",
                "Express",
                "Store Pickup",
                "Next Day Air"
            ]
        )

        discount_applied = st.selectbox(
            "Discount Applied",
            ["Yes", "No"]
        )

        promo_code_used = st.selectbox(
            "Promo Code Used",
            ["Yes", "No"]
        )

        previous_purchases = st.number_input(
            "Previous Purchases",
            min_value=0,
            max_value=100,
            value=40
        )

        payment_method = st.selectbox(
            "Payment Method",
            [
                "Credit Card",
                "Debit Card",
                "PayPal",
                "Cash",
                "Venmo"
            ]
        )

        frequency_of_purchases = st.selectbox(
            "Frequency of Purchases",
            [
                "Weekly",
                "Fortnightly",
                "Monthly",
                "Quarterly",
                "Annually"
            ]
        )

        st.markdown('</div>', unsafe_allow_html=True)

    # =====================================================
    # PREDICTION BUTTON
    # =====================================================

    if st.button("🚀 Predict Subscription"):

        with st.spinner("Analyzing customer behavior..."):

            time.sleep(2)

            # -------------------------------------------------
            # CREATE DATAFRAME
            # -------------------------------------------------

            input_data = pd.DataFrame({

                "Age": [age],
                "Gender": [gender],
                "Item Purchased": [item_purchased],
                "Category": [category],
                "Purchase Amount (USD)": [purchase_amount],
                "Location": [location],
                "Size": [size],
                "Color": [color],
                "Season": [season],
                "Review Rating": [review_rating],
                "Shipping Type": [shipping_type],
                "Discount Applied": [discount_applied],
                "Promo Code Used": [promo_code_used],
                "Previous Purchases": [previous_purchases],
                "Payment Method": [payment_method],
                "Frequency of Purchases": [frequency_of_purchases]

            })

            # -------------------------------------------------
            # MODEL PREDICTION
            # -------------------------------------------------

            prediction = model.predict(input_data)[0]

            probabilities = model.predict_proba(input_data)[0]

            no_probability = round(probabilities[0] * 100, 2)

            yes_probability = round(probabilities[1] * 100, 2)

        # =====================================================
        # RESULTS
        # =====================================================

        st.markdown("---")

        st.subheader("📊 Prediction Analytics")

        metric1, metric2 = st.columns(2)

        with metric1:

            st.metric(
                "YES Probability",
                f"{yes_probability}%"
            )

            st.progress(int(yes_probability))

        with metric2:

            st.metric(
                "NO Probability",
                f"{no_probability}%"
            )

            st.progress(int(no_probability))

        # =====================================================
        # BAR CHART
        # =====================================================

        chart_data = pd.DataFrame({
            "Prediction": ["YES", "NO"],
            "Probability": [yes_probability, no_probability]
        })

        st.bar_chart(
            chart_data.set_index("Prediction")
        )

        # =====================================================
        # CUSTOMER INSIGHTS
        # =====================================================

        st.subheader("💡 AI Customer Insights")

        if previous_purchases > 30:
            st.info("⭐ Loyal customer detected.")

        if purchase_amount > 100:
            st.info("💰 High spending behavior identified.")

        if review_rating > 4:
            st.info("🌟 Customer gives excellent reviews.")

        if frequency_of_purchases == "Weekly":
            st.info("🛒 Frequent shopper detected.")

        # =====================================================
        # FINAL RESULT
        # =====================================================

        if prediction == "Yes":

            st.markdown(
                """
                <div class="prediction-box"
                style="background: linear-gradient(to right, #11998E, #38EF7D);">
                ✅ Customer is likely to Subscribe!
                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                """
                <div class="prediction-box"
                style="background: linear-gradient(to right, #FF416C, #FF4B2B);">
                ❌ Customer is NOT likely to Subscribe.
                </div>
                """,
                unsafe_allow_html=True
            )

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown(
    """
    <center>
        <h4>🚀 Built with Streamlit + Machine Learning</h4>
    </center>
    """,
    unsafe_allow_html=True
)
