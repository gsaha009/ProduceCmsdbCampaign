# Simple instructions
# to produce cmsdb campaigns

## To setup environment

```bash
# uncomment the commented line to create the env (1st time only)
source setup.sh
```

Install the dependencies using `requirements.txt`,\
need `python > 3.9`

`pip install -r requirements.txt`


## Prepare the yaml with dataset name and nfiles & nevents

`python produce_nentries.py -c <main_config.yaml>`

## Prepare the campaign

`python main.py -c <main_config.yaml> -u nFiles_nEvents.yml`

> And, the campaign is READY !!!
