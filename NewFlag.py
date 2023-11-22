import datetime, argparse, re, fileinput
from requests import get

class RedFlagDomain:
    daily_url = "https://dl.red.flag.domains/daily/"
    all_domain = "https://dl.red.flag.domains/red.flag.domains.txt"

def banner():
    print("NewRedflag --- by 0xlildoudou\n")

def download_all(output):
    print('Download all domains')

    with open(output, 'a') as file:
        file.write(get(RedFlagDomain.all_domain).text)
    file.close()

def download_date(output, date):
    print('Download domain for: ' + str(date))

    daily_file = RedFlagDomain.daily_url + str(date) + '.txt'
    with open(output, 'a') as file:
        file.write(get(daily_file).text)
    file.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--latest","-l", help="latest list", action="store_true")
    parser.add_argument("--day","-d", help="Day of list")
    parser.add_argument("--all","-A", help="All list", action="store_true")
    parser.add_argument("--output","-o", help="Output file")
    parser.add_argument("--dns", help="Output format option for create DNS redirect")
    args = parser.parse_args()

    if args.all:
        output = args.output or "all.txt"
        download_all(output)

    if args.latest:
        date = datetime.date.today() - datetime.timedelta(days=1)
        output = args.output or str(date) + ".txt"
        download_date(output, date)

    if args.day:
        regex_global = re.compile('[-@_!#$%^&*()<>?/\|}{~:]')
        if (regex_global.search(args.day) == None):
            date = datetime.date.today() - datetime.timedelta(days=int(args.day))
            output = args.output or str(date) + ".txt"
            download_date(output, date)
        else:
            if (re.compile('-').search(args.day)):
                input_date = str(datetime.datetime.strptime(args.day, '%Y-%m-%d'))
                date = str(input_date.split(' ')[0])
                output = args.output or str(date) + ".txt"
                download_date(output, date)
            elif (re.compile('/').search(args.day)):
                input_date = str(datetime.datetime.strptime(args.day, '%Y/%m/%d'))
                date = str(input_date.split(' ')[0])
                output = args.output or str(date) + ".txt"
                download_date(output, date)
            else:
                print('Date not valid ! Pls use format : Year-month-day')

    if args.dns:
        dns_entry = '   CNAME   ' + str(args.dns)
        with fileinput.FileInput(output, inplace=True) as dns_file:
            first_line = True
            for line in dns_file:
                if first_line:
                    first_line = False
                    continue

                newline = line.rstrip() + dns_entry
                print(newline)