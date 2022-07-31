'''
Sharon Steinke
CS 1410
Project 1: Book Recommendations

Given a text file of authors with their books, and a text file of
names with their ratings of the those books, program will
recommend books to a reader (found in the ratings file)
based on the two highest affinity scores (i.e. dot products). 
Return the readers name, their friends, and the list
of recommended books.

I declare that the following source code was written solely by me.
I understand that copying any source code, in whole or in part,
constitutes cheating, and that I will receive a zero on this project
if I am found in violation of this policy.
'''
import operator

books = r"C:\Users\picko\OneDrive\OneDrive Documents\Python Code\cs 1410\Project 1 Book Recommendations\Booklist.txt"
ratings = r"C:\Users\picko\OneDrive\OneDrive Documents\Python Code\cs 1410\Project 1 Book Recommendations\ratings.txt"

with open(books, 'r') as fin:
    '''creates a list of lists with author in a
    string at index 0 and title in a tuple at index 1'''
    book_list = []
    lines = fin.readlines()
    for line in lines:
        new_line = line.strip().split(',')
        book_list.append([new_line[0],(new_line[1],)])

with open(ratings, 'r') as fin:
    '''creates a list of strings with the 
    name in the 0 and even index, ratings in the odd index'''
    lines = fin.readlines()
    ratings_dict = {}
    rates = []
    name_count = 0
    rates_count = 1
    for line in lines:
        new_line = line.strip()
        rates.append(new_line.lower())

    length = int(len(rates)/2)
    for _ in range(length):
        ratings_dict.update({rates[name_count]:rates[rates_count].split()})
        name_count += 2
        rates_count += 2

def dotprod(x_vals, y_vals):
    '''a sum of products function.

    input: two lists of numbers
    output: the dot product of the two lists
    '''
    dot_prod = 0
    for x_val, y_val in zip(x_vals, y_vals):
        dot_prod += int(x_val) * int(y_val)
    return dot_prod

def friends(name):
    """finds the two highest affinity scores of the name entered.

    input: name of reader
    output: two other readers with highest affinity scores to original reader.
    """
    scores = []
    two_friends = []
    if name in ratings_dict:
        new_dict = ratings_dict.copy()
        new_dict.pop(name)
        reader = ratings_dict.get(name)
        other_readers = new_dict.items()
        for peep, rates in other_readers:
            affinity_score = dotprod(reader, rates)
            scores.append([peep, affinity_score])
        sorted_scores = sorted(scores, key = operator.itemgetter(1, 0), reverse = True)
        two_friends.append(sorted_scores[0][0])
        two_friends.append(sorted_scores[1][0])
        return sorted(two_friends)

    elif name not in ratings_dict:
        print(f'No such reader {name}')
        quit()

def recommend(name = ''):
    '''generates and prints a list of books that are 
    unread by reader and recommended by two friends.

    input: name of reader
    output: recommends
    '''
    name = input("Enter a reader's name: ")
    recommends = {}
    two_friends = friends(name)
    reader = ratings_dict.get(name)
    first_friend = ratings_dict.get(two_friends[0])
    second_friend = ratings_dict.get(two_friends[1])
    for reader_rate, rate_one, rate_two, titles in zip(reader, first_friend, second_friend, book_list):
        if int(reader_rate) == 0:
            if int(rate_one) >= 3 or int(rate_two) >= 3:
                if titles[0] not in recommends:
                    recommends[titles[0]] = []
                    recommends[titles[0]].append(titles[1])
                else:
                    recommends[titles[0]].append(titles[1])
            else:
                continue
        else:
            continue
    print(f'Recommendations for {name} from {two_friends[0]} and {two_friends[1]}:')
    for author, book in recommends.items():
        if len(book) > 1:
            copy_title = ''
            for title in sorted(book):
                if copy_title != title[0]:
                    print(f'{author}, {title[0]}')
                    copy_title = title[0]
                else:
                    continue
        else:
             print(f'{author}, {book[0][0]}')

    return recommends



def main():
    '''runs the function recommend

    input: name
    output: list of recommendations
    '''
    #recommends()

if __name__ == "__main__":
    main()
