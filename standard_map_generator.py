from random import randint, choice, uniform

def generate_chunk(biome):

    biome = biome

    if biome == "deep_forest":
        terrain = []
        rest = []
        for i in range(45):
            x = []
            y = []
            for e in range(65):
                x.append(round(uniform(0, 0.2), 1))
                if randint(0, 2) == 0 or randint(0, 2) == 1:
                    y.append(round(uniform(50, 50.4), 1))
                elif randint(0, 2) == 2:
                    y.append(51.0)                    
                else:
                    y.append(99.0)
            terrain.append(x)
            rest.append(y)
        return biome, terrain, rest

    if biome == "plains":
        terrain = []
        rest = []
        for i in range(22):
            x = []
            y = []
            for e in range(35):
                x.append(round(uniform(0, 0.2), 1))
                if randint(0, 5) == 0:
                    y.append(round(uniform(51, 51.2), 1))
                elif randint(0, 10) == 0:
                    y.append(round(uniform(50, 50.2), 1))
                elif randint(0, 12) == 0:
                    y.append(round(uniform(51.3, 51.5), 1))
                else:
                    y.append(99.0)
            terrain.append(x)
            rest.append(y)
        return biome, terrain, rest

    if biome == "swamp":
        terrain = []
        rest = []
        for i in range(22):
            x = []
            y = []
            for e in range(35):
                if round(uniform(4, 4.3), 1) != 4.3:
                    x.append(round(uniform(4, 4.2), 1))
                    if randint(0, 45) == 1:
                        y.append(round(uniform(52, 52.2), 1))
                    elif randint(0, 45) == 1:
                        y.append(round(uniform(52.3, 52.5), 1))
                    elif randint(0, 25) == 1:
                        y.append(52.6)
                    elif randint(0, 25) == 1:
                        y.append(52.7)                        
                    else:
                        y.append(99.0)
                else:
                    x.append(4.3)
                    if randint(0, 3) == 0:
                        y.append(52.8)
                    else:
                        y.append(99.0)
            terrain.append(x)
            rest.append(y)
        return biome, terrain, rest

    if biome == "corruption":
        terrain = []
        rest = []
        for i in range(45):
            x = []
            y = []
            for e in range(45):
                x.append(round(uniform(5, 5.3), 1))
                if randint(0, 10) == 0:
                    y.append(round(uniform(53, 53.5), 1))
                else:
                    y.append(99.0)
                
            terrain.append(x)
            rest.append(y)
        return biome, terrain, rest


    if biome == "demo":
        terrain = []
        rest = []
        for i in range(22):
            x = []
            y = []
            for e in range(35):
                x.append(round(uniform(53, 53.2), 1))
            terrain.append(x)
            rest.append(y)
        return biome, terrain, rest
    


    # TODO BIOMES
    if biome == "lake":
        terrain = []
        rest = []
        for i in range(45):
            x = []
            y = []
            for e in range(45):
                x.append(round(uniform(1, 1.1), 1))
                if randint(0, 2) == 0 or randint(0, 2) == 1:
                    y.append(round(uniform(50, 50.4), 1))
                else:
                    y.append(99.0)
            terrain.append(x)
            rest.append(y)
        return biome, terrain, rest


test_map = [[0.0, 0.1, 0.2, 0.1, 0.0, 0.2, 0.1, 0.0, 0.0, 0.1],
 [0.0, 0.1, 0.2, 0.1, 0.0, 0.2, 0.1, 0.0, 0.0, 0.1],
 [0.0, 0.1, 0.2, 0.1, 0.0, 0.2, 0.1, 0.0, 0.0, 0.1],
 [0.0, 0.1, 0.2, 0.1, 0.0, 0.2, 0.1, 0.0, 0.0, 0.1],
 [0.0, 0.1, 0.2, 0.1, 0.0, 0.2, 0.1, 2.0, 2.0, 2.1],
 [0.0, 0.1, 0.2, 0.1, 0.0, 0.2, 0.1, 2.0, 1.0, 1.1],
 [0.0, 0.1, 0.2, 0.1, 0.0, 0.2, 0.1, 2.0, 1.0, 1.1],
 [0.0, 0.1, 0.2, 0.1, 0.0, 0.2, 0.1, 2.0, 1.0, 1.1],
 [0.0, 0.1, 0.2, 0.1, 0.0, 0.2, 0.1, 2.0, 2.0, 2.1],
 [0.0, 0.1, 0.2, 0.1, 0.0, 0.2, 0.1, 0.0, 0.0, 0.1]
]