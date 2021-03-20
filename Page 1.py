from flask import Flask, render_template, request

app = Flask(__name__)


def load_model(RnD, Administration, Marketing, State):
    file = open("model.pkl", "rb")

    import pickle
    model = pickle.load(file)
    # print(model)

    prediction = model.predict([[RnD, Administration, Marketing, State]])
    return prediction[0]


@app.route("/data", methods=["POST"])
def post_submit():
    # print("inside post data")
    RnD = request.form.get("RnD")
    Administration = request.form.get("Administration")
    Marketing = request.form.get("Marketing")
    State = request.form.get("State")
    Profit = f"{load_model(RnD, Administration, Marketing, State):0.2f}"
    # print(f"Profit = {Profit}")
    # print(f"RnD: {RnD}")
    # print(f"Administration: {Administration}")
    # print(f"Marketing: {Marketing}")
    # print(f"State: {State}")
    return render_template("result.html", RnD=RnD, Administration=Administration, Marketing=Marketing, Profit=Profit)


@app.route("/", methods=["GET"])
def root():
    return render_template("index.html")


@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")


@app.route("/contact_us", methods=["GET"])
def contact_us():
    return render_template("contact_us.html")


app.run(debug=True)
