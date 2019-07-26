#!/usr/bin/python3

from jinja2 import Environment, FileSystemLoader
import os
import sys
import yaml

#Load data from YAML into Python dictionary
config_data = yaml.safe_load(open('data.yaml'))
#print("config_data value is: ", config_data)

#Load Jinja2 template
filesToBeParsed = ['crypto-config', 'configtx', 'docker-compose-base', 'docker-compose-e2e-template', 'script', 'utils']

env = Environment(loader = FileSystemLoader('.'), trim_blocks=True, lstrip_blocks=True)
for i in filesToBeParsed:
    print("\n\n ####### Reading file: ", i, " #########\n\n")
    if "script" in i or "utils" in i:
        template = env.get_template(i + ".sh.in")
    else:            
        template = env.get_template(i + ".yaml.in")

    #Render the template with data and print the output
    finalData = (template.render(config_data))
    print(finalData)

    # Putting data to above file
    extension = ".yaml"
    if 'docker-compose-base' in i:
        path = "../base/"
    elif "script" in i or "utils" in i:
        path = "../scripts/"
        extension = ".sh"    
    else:
        path = "../" 
           
    with open(path + i + extension, 'w') as outfile:
        #yaml.safe_dump(finalData, outfile, default_flow_style=False)
        outfile.write(finalData)

