import random as r

# determine what kb is 
kilobyte  = (2 ** 10) - 1

min_size = 5
max_size = 12

min_off_sz = min_size - 4  + 10
max_off_sz = max_size - 4 + 10

# Randomly decide number of page frames in memory unit
frame_seed = r.randrange(min_size, max_size)
frame_bits = len(bin(frame_seed)[2:])
no_of_frames = int(frame_bits * '1',2) + 1

offset_bits = r.randrange(min_off_sz, max_off_sz) # off_sz KB is size of page
size_of_frame = int(offset_bits * '1',2)
size_of_frame_in_kb = size_of_frame / kilobyte 
total_bits = frame_bits + offset_bits
size_of_physical_unit = int(total_bits * '1', 2) / kilobyte

print ('Random frame seed', frame_seed)
print ('No of frames', no_of_frames)
print('Size of a physical frame', str(size_of_frame_in_kb) + 'KB')   
print('Size of physical memory', str(size_of_physical_unit) + 'KB')
print ("Bits needed for Page frame number", frame_bits) 
print ("Bits needed for offset", offset_bits)
print("Total bits for physical address" , total_bits)

if frame_bits != 0:
	logical_addr_bits = r.randrange(offset_bits + 1,  total_bits + 5) 
else:
	print ('got 0 bit frame address') #This accounts for testing
	logical_addr_bits = offset_bits

if logical_addr_bits > frame_bits:
	big_process = True
else:
	big_process = False
logical_pages_bits = logical_addr_bits - offset_bits #Number of bits to represent logical pages in process.
number_of_logical_pages = int(logical_pages_bits * '1',2) + 1
size_of_logical_addr_space = int(logical_addr_bits * '1', 2) / kilobyte

print('Size of logical address space', str(size_of_logical_addr_space) + 'KB')
print('Bits in logical address', logical_addr_bits)
print('Number of bits to represent logical pages' , logical_pages_bits)
print('Number of pages in logical address', number_of_logical_pages)

#Populating page table
#1) Available page frames
available_physical_page_frames = range(no_of_frames)
page_table = {}

formater_phy = '0' + str(frame_bits) + 'b'
formater_logical = '0' + str(logical_pages_bits) + 'b'
print ('formaters', formater_phy, formater_logical)
#allocate a physical page frame to process page 
for f in range(number_of_logical_pages):
	f_bin = format(f, formater_logical) 
	if available_physical_page_frames:
		if f_bin not in page_table.keys():
			physical_page = r.choice(available_physical_page_frames)
			available_physical_page_frames.remove(physical_page)
			l_bin = format(physical_page, formater_phy)
			page_table[f_bin] = l_bin
	else:
		print('No more physical pages available')
		break

print ('Page table')
print (page_table)

print ("Available pages")
available_pages_for_alloc = [format(x, formater_phy) for x in available_physical_page_frames]
print (available_pages_for_alloc)
	
#Address Translation
formater_phy_addr = '0' + str(total_bits) + 'b'
formater_log_addr = '0' + str(logical_addr_bits) + 'b'
random_logical_addr = format(r.getrandbits(logical_addr_bits), formater_log_addr)
print ('Some logical addr', random_logical_addr)

logical_pn = random_logical_addr[:logical_pages_bits] 
print('logical page number', logical_pn)

#Look up page table -
if logical_pn in page_table: 
	physical_frame_no = page_table[logical_pn]
	print ('physical frame number', physical_frame_no)

	physical_address = physical_frame_no + random_logical_addr[logical_pages_bits:]
	print("physical address", physical_address)
	print ("bits in physical address", len(physical_address))
else:
	print('Page fault {} not in memory'.format(random_logical_addr))
