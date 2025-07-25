from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 15,00,000'
}, {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary': 'Rs. 12,00,000'
}, {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'Bangalore, India',
    'salary': 'Rs. 12,00,000'
}]


@app.route("/")
def hello():
    return render_template('home.html', jobs=JOBS, company_name='Job Adda')


#creating an API route
@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


#creating route for job page
@app.route("/apply/<title>")
def apply(title):
    return render_template('apply.html', title=title, company_name='Job Adda')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
