captains_values = (('Enterprise', 'Picard'),('Voyager', 'Janeway'), ('Defiant', 'Sisko'))
captains = dict(captains_values)
if "Enterprise" not in captains:
    captains["Enterprise"] = "unknown"
if "Discovery" not in captains:
    captains["Discovery"] = "unknown"
    
for ship, captain in captains.items():
    print(f"The {ship} is captained by {captain}. ")

del captains["Discovery"]

