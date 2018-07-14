import random as r


# determine what kb is 
kilobyte  = 2 ** 10

min_size = 4
max_size = 8

min_off_sz = min_size - 2
max_off_sz = max_size - 2

# Randomly decide number of page frames in memory unit
no_of_physical_pages = r.randrange(min_size, max_size)
print ("No of pages frames", no_of_physical_pages)

# What shall be the page size? offset:
off_sz = r.randrange(min_off_sz, max_off_sz) # off_sz KB is size of page
print('No of bits for offset in physical frame', str(off_sz) + 'KB')   
print('Size of physical memory', str(off_sz * no_of_physical_pages) + 'KB')
print ("Bits needed for pf", len(bin(no_of_physical_pages)[2:])) 
