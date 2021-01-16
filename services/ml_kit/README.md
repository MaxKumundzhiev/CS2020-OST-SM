# Models Hub
Models Hub provides python interface to train 2 types of 3 dedicated models.   

## Models
1. Logistic Regression Classifier 
2. Decision Tree Classifier
3. Random Forest Classifier

Each model utilized 2 types of task: `binary classficication` and `multiclass classficication`
Trained models will be saved at `checkpoints/<DATASET NAME>/<PREDICTION TASK>/model.pkl` 

## Training
To train particular model on particular dataset it should be executed:
```bash
List of available datasets names:
- SELECTED_CICIDS
- SELECTED_NET
```

```bash
List of available models names:
- logistic-regressor
- decision-tree
- random-forest
```

```bash
List of available tasks names:
- binary_class
- multi_class
```

```bash
$ python -m services.ml_kit.train -d <DATASET NAME> -t <TYPE OF TASK> -m <MODEL NAME>

For example:
$ python -m services.ml_kit.train -d SELECTED_CICIDS -t binary_class -m logistic-regressor 
```

## Possible chain of ALL executions
```bash
# CICIDS Binary Classification
$ python -m services.ml_kit.train -d SELECTED_CICIDS -t binary_class -m logistic-regressor
$ python -m services.ml_kit.train -d SELECTED_CICIDS -t binary_class -m decision-tree
$ python -m services.ml_kit.train -d SELECTED_CICIDS -t binary_class -m random-forest

# CICIDS Multiclass Classification
$ python -m services.ml_kit.train -d SELECTED_CICIDS -t multi_class -m logistic-regressor
$ python -m services.ml_kit.train -d SELECTED_CICIDS -t multi_class -m decision-tree 
$ python -m services.ml_kit.train -d SELECTED_CICIDS -t multi_class -m random-forest

# NET Binary Classification
$ python -m services.ml_kit.train -d SELECTED_NET -t binary_class -m logistic-regressor
$ python -m services.ml_kit.train -d SELECTED_NET -t binary_class -m decision-tree
$ python -m services.ml_kit.train -d SELECTED_NET -t binary_class -m random-forest

# NET Multiclass Classification
$ python -m services.ml_kit.train -d SELECTED_NET -t multi_class -m logistic-regressor
$ python -m services.ml_kit.train -d SELECTED_NET -t multi_class -m decision-tree 
$ python -m services.ml_kit.train -d SELECTED_NET -t multi_class -m random-forest
``` 

Checkpoints folder structure:
```
.
├── TRANSFORMED_CICIDS
│   ├── binary_class
│   │   ├── decision-tree
│   │   │   └── model.pkl
│   │   ├── logistic-regressor
│   │   │   └── model.pkl
│   │   └── random-forest
│   │       └── model.pkl
│   └── multi_class
│       ├── decision-tree
│       │   └── model.pkl
│       ├── logistic-regressor
│       │   └── model.pkl
│       └── random-forest
│           └── model.pkl
└── TRANSFORMED_NET
    ├── binary_class
    │   ├── decision-tree
    │   │   └── model.pkl
    │   ├── logistic-regressor
    │   │   └── model.pkl
    │   └── random-forest
    │       └── model.pkl
    └── multi_class
        ├── decision-tree
        │   └── model.pkl
        ├── logistic-regressor
        │   └── model.pkl
        └── random-forest
            └── model.pkl
``` 
     
