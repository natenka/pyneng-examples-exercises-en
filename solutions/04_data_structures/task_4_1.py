# -*- coding: utf-8 -*-


nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"

nat_gig = nat.replace("Fast", "Gigabit")
print(nat_gig)
