The purpose of this project is an attempt to read the latest set of lottery numbers from "https://www.national-lottery.co.uk/results/euromillions/draw-history/".

The result is then scrapped to recover a current set of lottery numbers, this data is then cached in a 'pickle' which is basically a localised cache.

When Python (version 3) is run with 'run.py' the script will attempt to look at the numbers, factors and make a probable guess of which the next set of numbers are in sequence. It will attempt to consider the frequency and likelihood of individual factors with a view to deducing a result.

