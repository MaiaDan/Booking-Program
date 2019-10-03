
# Get the Max luck

 def luckBalance(k, contests):
    luck= 0
    contests.sort(reverse = True)  # sort the contests to have the big values and their importance first
    for c in contests:            # loop through the contests line by line
        if c[1] == 0:             # get the 2nd item of the line and check if it is zero
            luck += c[0]          # then it is not an important contest to lose so just add it
        elif k > 0:                # loses no more than k
            luck += c[0]           # add k more contest values (bcz they are te biggest)
            k-=1 # decrease the k
        else:
            luck -= c[0]            #subtract the least ones
    return luck                    # give back the total luck


