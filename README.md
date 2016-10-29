# brute-force-via-POST

This was made to brute force a simple web page located at http://<IPAddress>/cgi-bin/dologin using POST data and checking for the word "Sorry" in the response to see if the attempt was successful.

This is slow. Really slow. The framework for multithreading is there but I can't seem to figure out how to reliably skip every n-th iteration of the iterable within the thread and not affect the other threads.

Every 100th attempt it outputs the current attempt.

# USAGE: 

python main.py -t 192.168.1.101

python main_threaded.py -t 192.168.1.101 -n 2
