# kylin-manage

## Usage

python kylin_manager.py  --help

```
usage: kylin_manager.py [-h] --host HOST [--port PORT] --username USERNAME
                        --password PASSWORD
                        {exception-job} ...

positional arguments:
  {exception-job}
    exception-job      get jobs which status is error or duration time exceed
                       the max-duration

optional arguments:
  -h, --help           show this help message and exit
  --host HOST
  --port PORT
  --username USERNAME
  --password PASSWORD
```

python kylin_manager.py  exception-job --help

```
usage: kylin_manager.py exception-job [-h] --max-duration MAX_DURATION

optional arguments:
  -h, --help            show this help message and exit
  --max-duration MAX_DURATION
                        filter the job which duration time exceed this value
                        in seconds
```
