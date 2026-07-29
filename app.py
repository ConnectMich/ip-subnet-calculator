from flask import Flask, render_template, request, url_for, redirect, flash
from calculator import calc

app = Flask(__name__)
app.secret_key = "35f51c83"


@app.route("/", methods=["GET"])
def home():
    return render_template("home.html", ip_error=None, subnet_error=None, error=None)


@app.route("/results", methods=["POST"])
def results():
    get_ip = request.form.get("ip_address")
    get_subnet = request.form.get("subnet_mask")
    network_info = calc(get_ip, get_subnet)
    if network_info == "IP Error":
        flash("Invalid IP Address", "ip_error")
        return redirect(url_for("home"))
    elif network_info == "Subnet Error":
        flash("Invalid Subnet Mask", "subnet_error")
        return redirect(url_for("home"))
    elif network_info == "Error":
        flash("Incorrect Values", "error")
        return redirect(url_for("home"))
    else:
        return render_template("result.html", result=network_info)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)
