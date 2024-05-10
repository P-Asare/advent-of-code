"""

impossible = []

id : [
    red, green, blue
    [0, 0, 0] => [4, 0, 3], [1, 2, 6]


    {
        "red":12,
        "green":13,
        "blue":14
    }

    ["3 blue, 4 red", "1 red, 2 green, 6 blue", "2 green"]
    [["3 blue", "4 red"], ["1 red", "2 green", "6 blue"], ["2 green"]]
    [
        [
            ["3", "blue"], ["4", "red"]
        ], 
        [
            ["1", "red"], ["2", "green"], ["6", "blue"]
        ], 
        [
            ["2", "green"]
        ]
    ]
]

"""

power_sum = 0

possible = set()

doc_name = "./dayTwoInput.txt"

with open(doc_name, 'r') as file:
    # read current line
    line = file.readline()
    line_count = 1

    # Ensure line is not empty then process
    while line:
        color_count = {
            "red":0,
            "green":0,
            "blue":0
        }

        skip = False
        line = line.strip("\n")
        # separate game rounds
        round_store = line.split(": ")[1].split("; ")

        #print(round_store)
        for index in range(len(round_store)):

            # separate game rounds into each color pick
            round_store[index] = round_store[index].split(", ")
            
            for color_counts in range(len(round_store[index])):
                # Separate each color pick into the color and the pick
                round_store[index][color_counts] = round_store[index][color_counts].split(" ")

                # # Check if the pick for rounds adds up
                # if(int(round_store[index][color_counts][0]) > color_count[round_store[index][color_counts][1]]):
                #     skip = True
                #     break
                
                # store the maximum for a game inside of the dictionary
                color_count[round_store[index][color_counts][1]] = max(color_count[round_store[index][color_counts][1]], int(round_store[index][color_counts][0]))
            
            if(skip):
                break
        
        if(not skip):
           possible.add(line_count)

        # calculate power and add to other powers
        power = color_count["red"] * color_count["blue"] * color_count["green"]
        power_sum += power
        
        line_count += 1
        
        line = file.readline()

    print(power_sum)
        
        
