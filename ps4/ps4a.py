# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    # print('Sequence =>', sequence)
    # length = len(sequence)
    # permutation_list = []
    # character = sequence[0]
    # sequence1 = sequence[1:]
    
    # if len(sequence) == 1: 
    #     return [sequence]
    # else: 
        
    #     for i in range(length): 
            
    #         new_str = sequence1[0:i] + character + sequence1[i:length]
    #         permutation_list.append(new_str)
    
    #     print('permutation list', permutation_list)
    #     print('-'*50)
    #     return get_permutations(sequence1)
    
    first_letter = sequence[0]
    permutations = get_permutations(sequence[1:])
    
    permutation_list = []
    
    if len(sequence) == 1: 
        permutation_list.append(sequence)
        return permutation_list
    else: 
        for perm in permutations: 
            length = len(perm)
            for i in range(length): 
                new_str = perm[0:i] + first_letter + perm[i:length]
                permutation_list.append(new_str)
        return permutation_list         
            
    
     
    
    

    
 
if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    pass #delete this line and replace with your code here

