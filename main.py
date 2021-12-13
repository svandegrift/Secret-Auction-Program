#!/usr/bin/env python3
import os
import art

def clear_console():
	os.system('clear')
clear_console()
bidders = {}
bidding = True

print(art.logo)
print('Welcome to the secret auction program.')

def check_bids():
	top_bid = 0
	winner = ""
	for key in bidders:
		if bidders[key] > top_bid:
			winner = key
			top_bid = bidders[key]
	print(f'The winner is {winner} with a bid of ${top_bid}')

while(bidding):
	name = input('Enter your name: ')
	bid = int(input('Enter your bid: $'))
	bidders[name] = bid
	still_bidding = input("Are there any other bidders? Type 'yes' or 'no'.\n")
	if still_bidding == 'yes':
		clear_console()
	else:
		bidding = False
		check_bids()


	