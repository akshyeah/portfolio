from flask import Flask, render_template, request, redirect
import csv

from werkzeug.utils import send_file
app = Flask(__name__)
print(__name__)

@app.route('/' or '')
def index():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    #path = './static/assets/resume/Akshay_Resume.pdf'
    if page_name == '/static/assets/resume/Akshay_Resume.pdf':
        return send_file(page_name, as_attachment=True)
    return render_template(page_name)

#@app.route('/')
#def download_file():
#    
#    return send_file(path, as_attachment=True)

def write_to_csv(data):
    with open('database.csv', mode = 'a', newline='') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

# def write_to_file(data):
#     with open('database.txt', mode = 'a') as database:
#         email = data["email"]
#         subject = data["subject"]
#         message = data["message"]
#         file = database.write(f'\n{email},{subject},{message}')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database!'
    else:
        return 'something went wrong'