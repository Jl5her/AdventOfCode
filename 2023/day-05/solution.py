import re

with open('input.txt') as f:
    inp = " ".join(f.readlines()).replace("\n", "")

nums_exp = "([\d ]*)"
exp = "seeds:" + nums_exp
exp += "seed-to-soil map:" + nums_exp
exp += "soil-to-fertilizer map:" + nums_exp
exp += "fertilizer-to-water map:" + nums_exp
exp += "water-to-light map:" + nums_exp
exp += "light-to-temperature map:" + nums_exp
exp += "temperature-to-humidity map:" + nums_exp
exp += "humidity-to-location map:" + nums_exp

e = re.compile(exp)
[seeds, seed_soil, soil_fert, fert_water, water_light, light_temp, temp_humid, humid_loc] = [i.strip() for i in
                                                                                             e.findall(inp)[0]]


def map_sets(str):
    sets = str.split(' ')
    map = {}
    for set in zip(*[sets[i::3] for i in range(3)]):



    return map


seed_soil_map = map_sets(seed_soil)
soil_fert_map = map_sets(soil_fert)
fert_water_map = map_sets(fert_water)
water_light_map = map_sets(water_light)
light_temp_map = map_sets(light_temp)
temp_humid_map = map_sets(temp_humid)
humid_loc_map = map_sets(humid_loc)
