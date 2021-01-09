# Transformer
Module transforms all particular datasets.

# Execution 
```bash
- get help:
$ python -m transformer.handler --help

- transform particular dataset
$ python -m transformer.handler --datatset <DATASET NAME> 
    e.g.: python -m transformer.handler --datatset CICIDS 
```

## Supposed chain of executions
```bash 
$ python -m transformer.handler -d CICIDS  
$ python -m transformer.handler -d NET
```

# Notes
- Retrieved data will be written at created in the root of project folder -- `NAS` within described folder structure.
- After successful execution chain of steps resulting `train` & `test` data will be written to `NAS`, which is mounted for docker containers.     
   
# Resulting NAS folder structure
* NAS
  * CICIDS
    - train.csv
    - test.csv  
  * NET
    - train.csv
    - test.csv
  * TRANSFORMED_CICIDS
    - train.csv
    - test.csv
  * TRANSFORMED_NET
    - train.csv
    - test.csv
  