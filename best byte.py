# todo-1: Ask the user for input

# name = input("what is your neme?:")
# Price = int(input("what is your vid?: $"))


#todo-2: Save data into dictionary {name: price}
# bids[name] = Price

#todo-3: Whther is new bids need to be added

#todo-4: Compare in dictionary 
def find_highest_bidder(bidding_dictionary):
    winner =""
    highest_bid =0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder


    print(f"The winner is {winner} with a bid of ${highest_bid} .")


bids = {}
continue_bidding = True
while continue_bidding:
    name = input("what is your neme?:")
    Price = int(input("what is your vid?: $"))
    bids[name] = Price
    should_continue = input("Are there any other bidders? Type 'yes' or'no'.\n")
    if should_continue =="no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)
