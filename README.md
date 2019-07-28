# Python3-Jinja2-templating
### Designed for HLF files specifically
##### All the variables stored in data.yaml files hence reading the var values from data.yaml file
##### Taking a template input like crypto-config.yaml.in
##### Output crypto-config.yaml file with rendered data
#### configuring below files
##### 1. crypto-config.yaml
##### 2. configtx.yaml
##### 3. docker-compose-base.yaml
##### 4. docker-compose-e2e-template.yaml
##### 5. script.sh under script folder in byfn
##### 6. utils.sh in byfn  
##### 7. byfn.sh 

### Requisites
###### 1. Python3
###### 2. Jinja2: Use command "sudo apt install make curl python3-jinja2" to install this package.

## STEPS TO USE
###### 1. clone this repo under "github.com/hyperledger/ProjectName/networks/ directory
###### 2. create script folder under network directory
###### 3. Edit data.yaml file accordingly. This file is used to read the variables and then putting those variables in the config files.
###### 3. go to Python-Jinja2-templating directory and run the command "./jinja.py" and you are all set. 
###### 4. export COMPOSE_PROJECT_NAME=ProjectName or anyname
###### 5. Now go to networks directory and use "./byfn.sh generate -f docker-compose-e2e-template.yaml -i HLF_Version" 
###### 6. Now use command "./byfn.sh up -f docker-compose-e2e.yaml -i 1.4.1" command 


#### NOTES
###### 1. Tested with HLF 1.4.1 only
###### 2. This is a quick hack for those wants to use their own organisation names instead of predefined names in byfn.sh script in first-network directory under fabric-samples. 
###### 3. This will create a docker-compose.yaml file(under base directory), docker-compose-e2e-template.yaml, crypto-config.yaml, configtx.yaml, byfn.sh, utils.sh and scripts.sh under scripts directory.

#### Reference 
https://github.com/hyperledger/fabric-samples/tree/release-1.4/first-network 


