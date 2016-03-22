# py3, calculates amount of modules at each level of a tetrahedral kite.
# author : BinBin
modules = 0
total = 0
level = 0
rods = 0
connectors = 0
total_num_connectors = 0

def module_calc(level):
    """calculate the amount of modules for building the specific level."""
    global modules
    global rods
    modules = level*(level-1)/2
    rods = modules*6
    return modules, rods


def total_module(level):
    """calculate the total amount of modules based on the level of the tetrahedral kite."""
    global total
    for levels in range(1, level+1):
        module_calc(levels)
        total += modules
        pass
    return total


def connectors_calc(level):
    """calculate the amount of connectors for building the specific level."""
    global connectors
    connectors = level*(level+1)/2
    return connectors


def total_connectors(level):
    """calculate the total amount of connectors based on the level of the tetrahedral kite."""
    global total_num_connectors
    for levels in range(1, level+1):
        connectors_calc(levels)
        total_num_connectors += connectors
        pass
    return total_connectors


def main():
    """ask for the intended level of the tetrahedral and applied formula to find amount of materials needed to build it."""
    level = int(input('What level/height are you building it up to? accurate for positive integers only >>>'))
    module_calc(level)
    print(str(modules) + " modules on that level" + " " + "and" + " " + str(rods) + " rods")
    total_module(level)
    print(str(total) + " modules total")
    connectors_calc(level)
    print(str(connectors) + " connectors on that level")
    total_connectors(level)
    print(str(total_num_connectors) + " " + "connectors total")
    pass
