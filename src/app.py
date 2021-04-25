#!/usr/bin/python3
from flask import Flask, render_template, Response, request, redirect, url_for
from scheduler.schedule import Schedule

app = Flask(__name__)
sc = Schedule()

@app.route('/')
def show_main():
    return render_template('index.html')

@app.route("/schedules/new/", methods=['POST'])
def new_schedule():
    return render_template('new_schedule.html')

@app.route("/schedule/remove/<id>/")
def remove_schedule(id):
    return sc.test(id)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
