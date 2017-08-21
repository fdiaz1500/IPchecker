import time, urllib3

def main():
    print('[+]Fetched at: {}'.format(time.ctime()))
    http = urllib3.PoolManager()
    r = http.request('GET', 'https://api.ipify.org')
    print('[+]Status: {}'.format(r.status))
    out = str(r.data, 'utf-8')
    print('[+]IP: {}'.format(out))

if __name__ == '__main__':
    while True:
        main()
        time.sleep(30)