a10_cgnv6_fixed_nat_inside_ipv6address_ex:
  a10.delete:
    - a10_obj: cgnv6_fixed_nat_inside_ipv6address 
    - inside_netmask: 64
