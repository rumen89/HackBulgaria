#lyulin_city.py

def how_many_blocks_can_see(blocks):
    if len(blocks) == 0:
        return 0

    seen = 1
    current_max = blocks[0]
    for block in blocks:
        if block > current_max:
            current_max = block
            seen += 1
    return seen

#result = how_many_blocks_can_see([1,3,5,2,7,4])
#print(result)


n = input("Enter number: ")
n = int(n)

start = 1
block_height = []

while start <= n:
    height = input("Enter block height: ")
    height = int(height)

    block_height += [height]

    start += 1

# print("I can see " + str(how_many_blocks_can_see(block_height)) + " blocks")
