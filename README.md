# AI Customer Subscription Predictor (Streamlit)

A Streamlit web app that uses a trained scikit-learn model to predict whether a customer is likely to subscribe based on shopping behavior.

## Project Structure

- [`app.py`](app.py) — Streamlit UI + inference logic
- [`subscription_prediction_model.pkl`](subscription_prediction_model.pkl) — trained model (Joblib format)
- [`requirements.txt`](requirements.txt) — Python dependencies
- [`TODO.md`](TODO.md) — notes / tasks

## Features

- Modern Streamlit UI (two-column form layout)
- Real-time prediction on button click
- Displays prediction probabilities (YES / NO) with metrics + progress bars
- Styled result banner for final output

## Requirements

- Python 3.10+ recommended (works with Python 3.12 if your environment supports installed wheels)
- Dependencies listed in [`requirements.txt`](requirements.txt)

## Setup

Create and activate a virtual environment (recommended), then install dependencies:

````sh
python -m venv .venv
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1
pip install -r [requirements.txt](http://_vscodecontentref_/0)