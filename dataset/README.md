# Dataset Handler
**It is entrypoint of the OST-SM application.**  
The module allows to retrieve and transform data at target format.

**Data target format**
* NAS
  * <dataset_name>
    * train
      * <annotation_level> 
        * train.csv
        * class_label_pair.json
        * train_ids.json 

where:
- CLASS_LABEL_PAIR - denotes particular task target pair of class and value
   -  `e.g.: {"benign": 0, "malware": 1}` 

- TRAIN_IDS - denotes particular task target list of ids
   -  `e.g.: [5665772, 3745782, 6111057, 9812453, 8279555, 6418585, 1387558, ... , 1387634]`
- TRAIN_DATA - denotes particular task target set of features  
   - `e.g.: columns: [feature_1, feature_2, feature_3, ... , feature_4, y]`
   - `e.g.: row: [value_1, value_2, value_3, ... , value_4, y_target]`

# IMPORTANT
Transformed data will be saved at created in the root of project folder -- `NAS` within described folder structure. 

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
$ python -m dataset.handler -d dataset/CICIDS2017 -a fine 
$ python -m dataset.handler -d dataset/CICIDS2017 -a top

# NetML 
$ python -m dataset.handler -d dataset/NetML -a fine
$ python -m dataset.handler -d dataset/NetML -a top

# non-vpn2016 
$ python -m dataset.handler -d dataset/non-vpn2016 -a fine
$ python -m dataset.handler -d dataset/non-vpn2016 -a mid
$ python -m dataset.handler -d dataset/non-vpn2016 -a top
```

# Resulting structure
* NAS
  * CICIDS2017
    * train
      * fine
        - train.csv
        - class_label_pair.json
        - train_ids.json
      * top
        - train.csv
        - class_label_pair.json
        - train_ids.json
    * test
      - test.csv
  * NetML
  ...
  * non-vpn
  ...
   
