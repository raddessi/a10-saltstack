a10_overlay_tunnel_vtep_source_ip_address_ex:
  a10.delete:
    - a10_obj: overlay_tunnel_vtep_source_ip_address 
    - ip_address: 10.0.0.1