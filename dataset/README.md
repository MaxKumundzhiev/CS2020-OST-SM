# Dataset Handler
**It is entrypoint of the OST-SM application.**  
The module allows to retrieve and transform data at target format.

**Data target format**
* results
  * DATASET_NAME_ANNOTATION_LEVEL
    * TRAIN_DATA.csv
    * CLASS_LABEL_PAIR.json
    * TRAIN_IDS.json 

where:
- CLASS_LABEL_PAIR - denotes particular task target pair of class and value
   -  `e.g.: {"benign": 0, "malware": 1}` 

- TRAIN_IDS - denotes particular task target list of ids
   -  `e.g.: [5665772, 3745782, 6111057, 9812453, 8279555, 6418585, 1387558, ... , 1387634]`
- TRAIN_DATA - denotes particular task target set of features  
   - `e.g.: columns: [feature_1, feature_2, feature_3, ... , feature_4, y]`
   - `e.g.: row: [value_1, value_2, value_3, ... , value_4, y_target]`

# IMPORTANT
Transformed data will be saved at folder of second step -- `spark` within described folder structure. 

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

