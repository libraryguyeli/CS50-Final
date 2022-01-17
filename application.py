from flask import Flask, render_template, request
import datetime as dt


# Configure application
app = Flask(__name__)


# Home page
@app.route("/")
def index():
    return render_template("index.html")


# Calculates the cost of the chosen products and services
@app.route("/calculator", methods=["GET", "POST"])
def calculator():
   # Prices for all services
    adbook_price = 130
    adcard_price = 30
    minbook_price = 100
    mincard_price = 15
    expedite_price = 60
    overnight_price = 17.56

    if request.method == "POST":
        # Variables for all user-entered numbers
        total_applicants = int(request.form.get("total_applicants"))
        adult_books = int(request.form.get("adult_books"))
        adult_cards = int(request.form.get("adult_cards"))
        minor_books = int(request.form.get("minor_books"))
        minor_cards = int(request.form.get("minor_cards"))
        expedite = int(request.form.get("expedite"))
        overnight = int(request.form.get("overnight"))

        # Calculate State Department costs
        total_passports = (adbook_price * adult_books) + (adcard_price * adult_cards) + (minbook_price * minor_books) + (mincard_price * minor_cards)
        total_expedite = expedite_price * expedite
        total_overnight = overnight_price * overnight
        total_cost = total_passports + total_expedite + total_overnight

        # Calculate acceptance facility cost
        processing_cost = total_applicants * 35

        return render_template("calculated.html", total_applicants = total_applicants, adult_books = adult_books,
                                adult_cards = adult_cards, minor_books = minor_books, minor_cards = minor_cards,
                                expedite = expedite, overnight = overnight,
                                processing_cost = usd(processing_cost), total_cost = usd(total_cost))
    else:
        return render_template("calculator.html")


# Calculates 5, 7, 8, 11 weeks out from today
@app.route("/eta")
def eta():
    # Variables for each date calculated based on today
    thisDay = dt.date.today()
    fiveWeeks = dt.timedelta(weeks = 5) + thisDay
    fiveWeeks = fiveWeeks.strftime("%m/%d/%y")
    sevenWeeks = dt.timedelta(weeks = 7) + thisDay
    sevenWeeks = sevenWeeks.strftime("%m/%d/%y")
    eightWeeks = dt.timedelta(weeks = 8) + thisDay
    eightWeeks = eightWeeks.strftime("%m/%d/%y")
    elevenWeeks = dt.timedelta(weeks = 11) + thisDay
    elevenWeeks = elevenWeeks.strftime("%m/%d/%y")
    thisDay = thisDay.strftime("%m/%d/%y")

    return render_template("eta.html", today = thisDay, five = fiveWeeks, seven = sevenWeeks,
                            eight = eightWeeks, eleven = elevenWeeks)

# Checklist for documents needed for applying
@app.route("/requirements", methods = ["GET", "POST"])
def requirements():
    if request.method == "POST":
        return render_template("checklist.html")
    else:
        return render_template("requirements.html")


# Format value as a U.S. dollar (Thanks, C$50!)
def usd(value):
    return f"${value:,.2f}"