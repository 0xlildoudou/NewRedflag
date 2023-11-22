![https://red.flag.domains/](.github/rfd.png)
# NewRedflag
Basic Python script for download/create wordlist from https://red.flag.domains/

## Install
```shell
git clone https://github.com/0xlildoudou/NewRedflag.git
cd NewRedFlag
pip3 install -r requirements.txt
```

## Usage

### Download all domains flagged 
```shell
python3 NewFlag.py -A
```

### Download last domains flagged
```shell
python3 NewFlag.py --latest
```

### Download specific date

> 3 day before
```shell
python3 NewFlag.py --day 3
```
> Specific date
```shell
python3 NewFlag.py --day 2023-11-11
```
*Supported format: Year-month-day or Year/month/day*

### Output name
```shell
python3 NewFlag.py -A --output sample.txt
```

### Dns entry output
```shell
python3 NewFlag.py -A --dns 127.0.0.1
```

## Support
<img src=".github/buymeacoffe.png" href="https://www.buymeacoffee.com/0xlildoudou/" width="200">