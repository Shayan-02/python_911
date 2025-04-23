class Pedarbozorgpedari:
    pass


class Madarbozorgpedari:
    pass


class Pedarbozorgmadari:
    pass


class Madarbozorgmadari:
    pass


class Pedar(Pedarbozorgpedari, Madarbozorgpedari):
    pass


class Madar(Pedarbozorgmadari, Madarbozorgmadari):
    pass


class Bache(Pedar, Madar):
    pass
