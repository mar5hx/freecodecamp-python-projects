def hanoi_solver(disks: int):
    # assigning rods, start rod descends from how many disks to 0(exlcusive), from bottom disk to top(-1)
    start_rod = list(range(disks, 0, -1))
    temp_rod = []
    end_rod = []
    # required visual string represenation starting format
    towers = f'{start_rod} {temp_rod} {end_rod}'
    # moves will be used to store and display all moves(including start position(which is towers))
    moves = [towers]
    # nested function to assist me , represents start, temp, end

    def hanoi_helper(n, source, helper, destination):
        # prevents infinite recursion
        if n < 1:
            return
        # n -1 represents move amount of disks - 1
        # helper is now the destination here to make space for the bottom disk to reach end_rod
        hanoi_helper(n - 1 , source, destination, helper)
        # adds last item from start_rod list to end_rod
        destination.append(source.pop(-1))
        # adds move while keeping rods in correct order but new disk position
        moves.append(f'{start_rod} {temp_rod} {end_rod}')
        # recursive call to move disks from temp with start as the helper now and end as destination
        hanoi_helper(n - 1, helper, source, destination)
    # allows recursive engine to run on its own
    hanoi_helper(disks, start_rod, temp_rod, end_rod)
    # returns the moves with a \n joined after each move
    return "\n".join(moves) 