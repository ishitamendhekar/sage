import itertools
import sqlite3

#here
'''
from collections import Counter

def get_frequency_count(data):
    flattened_lst = [item for sublist in data for item in sublist]
    return dict(Counter(flattened_lst))
'''
#to here



def apriori(data, min_support):

    items = set()    #  for all unique item in a LIST in the data
    for transaction in data:
        for item in transaction:
            items.add(item)
    

    def generate_combinations(k):    # Create a list of all possible item combinations of length k
        return list(itertools.combinations(items, k))
    

    def count_combinations(combinations):    # Count the number of occurrences of each item combination
        counts = {}
        for combination in combinations:
            for transaction in data:
                if set(combination).issubset(transaction):
                    if combination in counts:
                        counts[combination] += 1
                    else:
                        counts[combination] = 1
        return counts
    

    frequent_itemsets = {}    # Find all frequent item sets with a minimum support
    for k in range(1, len(items)):
        combinations = generate_combinations(k)
        counts = count_combinations(combinations)
        frequent_combinations = {combination: count for combination, count in counts.items() if count >= min_support}
        frequent_itemsets.update(frequent_combinations)
    
    return frequent_itemsets

    
    
#get data form sage
def getData():
    conn = sqlite3.connect('Sage.db')
    cur = conn.cursor()
    cur.execute("SELECT query FROM ActivityLogs ")
    rows = cur.fetchall()
    data = []
    for row in rows:
        data.append(list(row))
    conn.close()
    return data


data = getData()
'''print (data)
print("..............................")'''

#data=[['Tell me news', 'What is the weather like?', 'Type a message'], ['Tell me news', 'What is the weather like?', 'Launch Youtube'], ['Tell me news', 'What is the weather like?', 'Type a message', 'Launch Youtube'], ['Tell me news', 'What is the weather like?', 'Launch Youtube', 'Take a screenshot'], ['Tell me news', 'What is the weather like?', 'Launch Youtube', 'Take a screenshot', 'Type a message']]

min_support = 2
frequent_itemsets = apriori(data, min_support)
print(frequent_itemsets)
 #here
'''

frequent_itemsets = get_frequency_count(data)
print(frequent_itemsets)
'''
