"""Routes for stock apis."""
import yfinance as yf
from flask import Blueprint, flash, redirect, render_template, request, url_for, jsonify
from flask_login import current_user, login_user
from .models import User, db
from . import login_manager
from .forms import LoginForm, SignupForm

# Blueprint Configuration
stock_bp = Blueprint(
    'stock_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


# API Route for pulling the stock quote
@stock_bp.route('/quote', methods=['GET'])
def display_quote():
	# get a stock ticker symbol from the query string
	# default to AAPL
	symbol = request.args.get('symbol', default="AAPL")

	# pull the stock quote
	quote = yf.Ticker(symbol)

	#return the object via the HTTP Response
	return jsonify(quote.info)

# API route for pulling the stock history
@stock_bp.route("/history", methods=['GET'])
def display_history():
	#get the query string parameters
	symbol = request.args.get('symbol', default="AAPL")
	period = request.args.get('period', default="1y")
	interval = request.args.get('interval', default="1mo")

	#pull the quote
	quote = yf.Ticker(symbol)	
	#use the quote to pull the historical data from Yahoo finance
	hist = quote.history(period=period, interval=interval)
	#convert the historical data to JSON
	hist.reset_index(inplace=True)

	data = hist.to_json()
	#return the JSON in the HTTP response
	return data