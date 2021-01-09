# Models Hub
Models Hub provides python interface to train 2 types of 3 dedicated models.   

## Models
1. Logistic Regression Classifier 
2. Decision Tree Classifier
3. Random Forest Classifier

Each model utilized 2 types of task: `binary classficication` and `multiclass classficication`

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
List of available models names:
- logistic-regressor
- decision-tree
- random-forest
```

```bash
List of available tasks names:
- binary-class
- multi-class
```

```bash
$ python -m services.ml_kit.train -d <DATASET NAME> -t <TYPE OF TASK> -m <MODEL NAME>

For example:
$ python -m services.ml_kit.train -d SELECTED_CICIDS -t binary-class -m logistic-regressor 
```



     
