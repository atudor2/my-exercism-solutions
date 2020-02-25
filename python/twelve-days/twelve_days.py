def recite(start_verse, end_verse):
    days = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']

    result = list()

    for i in range(start_verse, end_verse + 1):
        day = days[i - 1]

        result.append("On the {} day of Christmas my true love gave to me: {}.".format(day, make_verse_list(i)))        

    return result

def make_verse_list(end_verse):
    verses = [                    
        'twelve Drummers Drumming',
        'eleven Pipers Piping',
        'ten Lords-a-Leaping', 
        'nine Ladies Dancing', 
        'eight Maids-a-Milking', 
        'seven Swans-a-Swimming', 
        'six Geese-a-Laying',
        'five Gold Rings', 
        'four Calling Birds',
        'three French Hens', 
        'two Turtle Doves', 
        'a Partridge in a Pear Tree'
    ]

    start = end_verse * -1
    slice = verses[start:]

    if len(slice) == 1:
        return slice[0]

    v = ", ".join(slice[:-1])
    v += ", and " + slice[-1]
    return v
