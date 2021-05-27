ours = open("lemmatizer_test_output.csv", "r")
theirs = open("lemmatizer_test_output_theirs.csv", "r")

our_mistakes = []
their_mistakes = []
common_mistakes = []

#import pdb; pdb.set_trace();

for our_line in ours:
    their_line = theirs.readline()
    
    our_split = our_line.split(",")
    their_split = their_line.split(",")

    if "failed" == our_split[-1][:-1]:
        if "failed" == their_split[-1][:-1]:
            common_mistakes.append(our_split[0])
        else:
            our_mistakes.append(our_split[0])
    elif "failed" == their_split[-1][:-1]:
        if "failed" == our_split[-1][:-1]:
            common_mistakes.append(our_split[0])
        else:
            their_mistakes.append(their_split[0])

print("Number of our mistakes: {}".format(len(our_mistakes)))
print("Number of their mistakes: {}".format(len(their_mistakes)))
print("Number of common mistakes: {}".format(len(common_mistakes)))

if len(our_mistakes) == 0:
    total_mistakes = max(len(our_mistakes),len(their_mistakes)) + len(common_mistakes)
    print("Improvement: {:.1f}%".format(abs(len(their_mistakes) - len(our_mistakes))/total_mistakes * 100))
else:
    print("We've made different errors.")
    print("See mistake.csv for more information.")