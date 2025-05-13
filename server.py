from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html ')

@app.route("/<string:page_name>")
def home_page(page_name):
    return render_template(page_name)

def write_to_csv(data):
    with open('database.csv', 'a',newline='') as database:
        email=data['email']
        subject = data['subject']
        message = data['message']
        csv_writer=csv.writer(database,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route("/submit_form",methods = ['POST','GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
        except: 'Data is not stored!!!!'
    else:
        print("Something went wrong!!")
    return redirect('thankyou.html')
