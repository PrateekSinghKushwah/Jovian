from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id' : 1,
        'Title' : 'Data Engineer',
        'Location' : 'Remote',
        'Salary' : '$120,000'
    },
    {
        'id' : 2,
        'Title' : 'Cloud Engineer',
        'Location' : 'Remote',
        'Salary' : '$120,000'
    },
    {
        'id' : 3,
        'Title' : 'Software Engineer',
        'Location' : 'Remote',
        
    },
    {
        'id' : 4,
        'Title' : 'Cloud Consultant',
        'Location' : 'Remote',
        'Salary' : '$120,000'
    },
    {
        'id' : 5,
        'Title' : 'Business Analyst',
        'Location' : 'Remote',
        'Salary' : '$120,000'
    },
]

@app.route('/')
def hello():
  return render_template('home.html', jobs = JOBS, company_name = 'Getraise Technologies')

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host = '0.0.0.0' ,debug=True)