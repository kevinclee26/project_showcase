from flask import Flask, render_template, redirect, jsonify
import pymongo
import csv
import random

app=Flask(__name__)

default_image_links=['https://images.prismic.io/meltwater/5456e736-ea88-4f21-82bf-5132326cbd99_eng-0303-BONUS+Data+Visualization+Designed+for+PR+and+Comms+Professionals.png?auto=compress,format&rect=0,20,596,397&w=1920&h=1280', 
					 'https://sm.pcmag.com/pcmag_in/feature/1/10-free-da/10-free-data-visualization-tools_5un4.jpg', 
					 'https://boostlabs.com/wp-content/uploads/2019/09/10-types-of-data-visualization-1.jpg']

with open('static/data/projects.csv', 'r', encoding='utf-8-sig') as f: 
	csv_reader=csv.DictReader(f)
	project_list=[]
	for row in csv_reader: 
		project=dict(row)
		if not project['thumbnail']: 
			project['thumbnail']=random.choice(default_image_links)
		project_list.append(project)

@app.route('/')
def index(): 
	return render_template('index.html', data_from_flask=project_list)

if __name__=='__main__': 
	app.run(debug=True)