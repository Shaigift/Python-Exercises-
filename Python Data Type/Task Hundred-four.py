def mix_up(y, z):
    new_y = z[:2] + y[2:]
    new_z = y[:2] + z[2:]

    return new_y + new_z
print(mix_up("ase" , "cdt"))

