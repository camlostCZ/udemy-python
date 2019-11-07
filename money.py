'''
User enters a cost and money give, program computes number of individual values to return.
'''

MONEY_CZK = [5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
MONEY_EUR = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.2, 0.1, 0.05, 0.02, 0.01]

from decimal import Decimal

class Counter:
    '''
    Class to count number of occurences.
    '''

    def __init__(self, keys=[]):
        '''
        Constructor.

        Arguments:
        keys: list of keys

        Members:
        _data: dictionary used to count items
        '''
        self._data = {x: 0 for x in keys}

    def update(self, key, value=1):
        '''
        Update / add item in the counter.

        Arguments:
        key: the item to be updated
        value: value to be added to the counter
        '''
        if key in self._data.keys():
            self._data[key] += value
        else:
            self._data[key] = value

    def get_dict(self):
        '''
        Return collected data as a dictionary.
        '''
        return self._data


def read_price(msg):
    '''
    Read price from user displaying a message.
    '''
    finished = False
    while not finished:
        try:
            result = float(input(msg + " "))
            finished = True
        except ValueError:
            print("Error: Not a number. Please, enter a number.")
    return Decimal(result)

def compute_return(diff, money_values):
    '''
    Compute amount of individual values to return to customer.

    Arguments:
    diff: nominal value to return
    money_values: list of available money values

    Return:
    dictionary of values and their amount
    '''
    result = Counter()
    rest = diff
    idx = 0
    while rest > 0 and idx < len(money_values):
        current_value = Decimal(money_values[idx])
        if rest >= current_value:
            result.update(current_value)
            rest -= current_value
        else:
            idx += 1
    return result.get_dict()

def main():
    '''
    We love pylint! Some stupid comment. Is that what we want?
    '''
    cost = read_price("What is the cost?")
    paid = read_price("How much has been paid?")

    if paid < cost:
        print("You need to pay {} more.".format(cost - paid))
    else:
        to_return = compute_return(paid - cost, MONEY_EUR)
        if to_return:  # If to_return is not empty
            for money, amount in to_return.items():
                if amount > 0:
                    print("Value {}:  amount {}".format(money, amount))
        else:
            print("Exact price has been paid.")

main()
