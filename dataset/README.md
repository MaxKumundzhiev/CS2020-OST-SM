# Dataset Handler
It is entrypoint of the application.  
`The module allows to retrieve and transform data at target format.`

# Requirements
It is assumed user have already fetched github repository and accomplished step `0` described in main readme.    

# Prepare Dataset
```bash
- retrieve and transform particular dataset
$ python dataset.handler --datatset <PATH TO DATSET> --annotation <LEVEL OF ANNOTATION> 
e.g.: python dataset.handler --datatset dataset/CICIDS2017 --annotation fine 

- get help:
$ python -m dataset.handler --help
```
# Supposed chain of executions
```bash
# CICIDS2017
$ python dataset.handler --datatset dataset/CICIDS2017 --annotation fine
$ python dataset.handler --datatset dataset/CICIDS2017 --annotation top

# NetML
$ python dataset.handler --datatset dataset/NetML --annotation fine
$ python dataset.handler --datatset dataset/NetML --annotation top

# non-vpn2016
$ python dataset.handler --datatset dataset/non-vpn2016 --annotation fine
$ python dataset.handler --datatset dataset/non-vpn2016 --annotation mid
$ python dataset.handler --datatset dataset/non-vpn2016 --annotation top
```

# Resulting structure
* results
  * CICIDS2017_fine
    - class_label_pair.json
    - train_ids.json
    - X_train.csv
  * CICIDS2017_top
    - class_label_pair.json
    - train_ids.json
    - X_train.csv
  * NetML_fine
    - class_label_pair.json
    - train_ids.json
    - X_train.csv
  * NetML_top
    - class_label_pair.json
    - train_ids.json
    - X_train.csv
  * non-vpn2016_fine
    - class_label_pair.json
    - train_ids.json
    - X_train.csv
  * non-vpn2016_mid
    - class_label_pair.json
    - train_ids.json
    - X_train.csv
  * non-vpn2016_top
    - class_label_pair.json
    - train_ids.json
    - X_train.csv

