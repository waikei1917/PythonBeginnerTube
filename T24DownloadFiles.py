from urllib import request

goog_url = 'http://chart.finance.yahoo.com/table.csv?s=GOOG&a=1&b=18&c=2017&d=2&e=18&f=2017&g=d&ignore=.csv'

def download_stock_data(csv_url):
    responses = request.urlopen(csv_url)

    csv = responses.read()
    print(csv)

    csv_str = str(csv)
    print(csv_str)

    dest_url = r'goog.csv'
    print(dest_url)

    lines = csv_str.split("\\n")
    fx = open(dest_url,'w')
    for line in lines:
        fx.write(line+"\n")
    fx.close()

download_stock_data(goog_url)