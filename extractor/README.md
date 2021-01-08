# Extractor
Module extracts and transforms all datasets with target format at `NAS` directory.

# Execution 
```bash
- get help:
$ python -m extractor.handler --help

- extract particular dataset
$ python -m extractor.handler --datatset <DATASET NAME> 
    e.g.: python -m extractor.handler --datatset CICIDS 
```

## Supposed chain of executions
```bash 
$ python -m extractor.handler -d CICIDS  
$ python -m extractor.handler -d NET
$ python -m extractor.handler -d NONVPN
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