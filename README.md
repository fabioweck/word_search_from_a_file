# word_search_from_a_file
This program opens and reads a dictionary in a local file and checks the words given by user.

A dot . means that any single character is acceptable in its place. For example, ca. would yield words like cat and car, 
p.ng would yield words like ping and pong, and .a.e would yield words like sane, care and late.
An asterisk * at the end of the search term means that any word which begins with the search term is acceptable. 
An asterisk at the beginning of the search term means that any word which ends with the search term is acceptable. 
For example, ca* would yield words like california, cat, caring and catapult, while *ane would yield words like crane, insane and aeroplane. 
There can only ever be a single asterisk in the search term.
If there are no wildcard characters in the search term, only words which match the search term exactly are returned.
