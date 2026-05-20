# =========================================================
# ADVANCED AI CUSTOMER SUBSCRIPTION PREDICTOR
# BEAUTIFUL STREAMLIT UI
# =========================================================

import streamlit as st
import pandas as pd
import joblib

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
    background: linear-gradient(to right, #141e30, #243b55);
    color: white;
}

/* Title */
.main-title {
    font-size: 48px;
    font-weight: bold;
    text-align: center;
    color: white;
    margin-bottom: 10px;
}

/* Subtitle */
.sub-title {
    text-align: center;
    color: #d1d1d1;
    font-size: 20px;
    margin-bottom: 40px;
}

/* Card Design */
.card {
    background-color: rgba(255,255,255,0.08);
    padding: 25px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
    margin-bottom: 20px;
}

/* Prediction Box */
.prediction-box {
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    font-size: 30px;
    font-weight: bold;
    margin-top: 20px;
}

/* Button */
.stButton>button {
    width: 100%;
    height: 60px;
    font-size: 22px;
    font-weight: bold;
    border-radius: 15px;
    border: none;
    background: linear-gradient(to right, #00c6ff, #0072ff);
    color: white;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.03);
    background: linear-gradient(to right, #0072ff, #00c6ff);
}

/* Sidebar */
.css-1d391kg {
    background-color: #111827;
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

st.sidebar.title("📌 About")

st.sidebar.info(
    """
    This AI model predicts whether a customer is likely
    to subscribe based on shopping behavior.

    ✅ Machine Learning Model  
    ✅ Streamlit Web App  
    ✅ Real-time Prediction
    """
)

# =========================================================
# INPUT SECTION
# =========================================================

col1, col2 = st.columns(2)

with col1:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    age = st.slider("Age", 18, 70, 25)

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    item_purchased = st.selectbox(
        "Item Purchased",
        [
            "Blouse", "Sweater", "Jeans", "Sandals",
            "Shirt", "Dress", "Shoes",
            "Handbag", "Jacket", "Jewelry"
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
        1,
        1000,
        120
    )

    location = st.selectbox(
        "Location",
        [
            "California",
            "Texas",
            "New York",
            "Florida",
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
        0,
        100,
        40
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

# =========================================================
# PREDICTION BUTTON
# =========================================================

if st.button("🚀 Predict Subscription"):

    try:

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

        # Prediction
        prediction = model.predict(input_data)[0]

        # Probability
        probabilities = model.predict_proba(input_data)[0]

        no_probability = round(probabilities[0] * 100, 2)
        yes_probability = round(probabilities[1] * 100, 2)

        # =========================================================
        # RESULTS
        # =========================================================

        st.markdown("---")

        st.subheader("📊 Prediction Analytics")

        result_col1, result_col2 = st.columns(2)

        with result_col1:
            st.metric(
                "YES Probability",
                f"{yes_probability}%"
            )

            st.progress(int(yes_probability))

        with result_col2:
            st.metric(
                "NO Probability",
                f"{no_probability}%"
            )

            st.progress(int(no_probability))

        # =========================================================
        # FINAL RESULT
        # =========================================================

        if prediction == "Yes":

            st.markdown(
                f"""
                <div class="prediction-box"
                style="background: linear-gradient(to right, #11998e, #38ef7d);">
                ✅ Customer is likely to Subscribe!
                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                f"""
                <div class="prediction-box"
                style="background: linear-gradient(to right, #ff416c, #ff4b2b);">
                ❌ Customer is NOT likely to Subscribe.
                </div>
                """,
                unsafe_allow_html=True
            )

    except Exception as e:

        st.error(f"Error: {e}")

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown(
    """
    <center>
    <h4>💡 Built with Streamlit + Machine Learning</h4>
    </center>
    """,
    unsafe_allow_html=True
)