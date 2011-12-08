import flatland


Enum_abc = flatland.Enum.valued('A', 'B', 'C')

class Species(flatland.Form):
    code = flatland.Integer
    name = flatland.String
    population_resident = flatland.String
    population_migratory_repro = flatland.String
    population_migratory_winter = flatland.String
    population_migratory_transit = flatland.String
    site_population = Enum_abc
    site_conservation = Enum_abc
    site_isolation = Enum_abc
    site_global = Enum_abc
