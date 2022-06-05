import pandas as pd
list = ['epam', 'system', 'inc', 'nyse', 'epam', 'item', 'leading', 'digital', 'transformation', 'service', 'product', 'engineering', 'company', 'today', 'announced', 'it', 'ha', 'established', 'epam', 'ukraine', 'assistance', 'fund', 'assistance', 'fund’', 'support', 'charitable', 'aid', 'organization', 'provide', 'direct', 'relief', 'those', 'vulnerable', 'situation', 'across', 'ukraine', 'fund', 'separate', 'addition', '100', 'million', 'humanitarian', 'commitment', 'epam', 'announced', 'march', '4', '2022', 'company’s', 'previously', 'established', 'relief', 'program', 'donation', 'work', 'epam', 'volunteer', 'the', 'ground', 'more', '14', '000', 'ukrainian', 'employee', 'many', 'epam', 'global', 'location', 'originated', 'ukraine', 'extensive', 'network', 'more', '50', '000', 'family', 'member', 'friend', 'are', 'deeply', 'affected', 'the', 'crisis', 'ukraine', 'personal', 'connection', 'give', 'u', 'item', 'unique', 'perspective', 'what', 'really', 'needed', 'the', 'ground', 'customer', 'partner', 'have', 'overwhelmed', 'u', 'their', 'outpouring', 'support', 'their', 'direct', 'request', 'contribute', 'effort', 'help', 'the', 'people', 'ukraine', 'response', 'such', 'request', 'by', 'using', 'our', 'insight', 'ability', 'act', 'the', 'ground', 'established', 'the', 'epam', 'ukraine', 'assistance', 'fund', 'together', 'with', 'our', 'customer', 'partner', 'are', 'enabling', 'people', 'organization', 'around', 'the', 'world', 'to', 'help', 'ukraine', 'and', 'the', 'people', 'ukraine', 'said', 'arkadiy', 'dobkin', 'ceo', 'president', 'epam']
str = pd.Series(list)
pd.get_dummies(str)
wordfreq = {}
for token in list:
    if token not in wordfreq.keys():
        wordfreq[token] = 1
    else:
        wordfreq[token] += 1
output = pd.Series(wordfreq)
print(pd.get_dummies(output))
