a10_slb_server_port_ex:
  a10.delete:
    - a10_obj: slb_server_port 
    - protocol: tcp
    - port_number: 443
