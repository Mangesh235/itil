from flask import Flask, jsonify

app = Flask(__name__)


ditiss_modules = ["Security concepts", "COSA", "ITIM & Devops" ,"NDC" ]

prn = "75782"
name = "Mangesh Lasrekar"
phone_number = "7276118292"

@app.route('/')
def welcome():
    return "Welcome to ITIL!"

@app.route('/modules')
def get_modules():
    return jsonify(ditiss_modules)

@app.route('/info')
def get_info():
    info = f"PRN: {prn}, Name: {name}, Phone Number: {phone_number}"
    return info

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True)

