a10_gslb_service_ip_port_ex:
  a10.delete:
    - a10_obj: gslb_service_ip_port 
    - port_proto: tcp