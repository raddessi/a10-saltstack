a10_slb_template_tcp_proxy_ex:
  a10.delete:
    - a10_obj: slb_template_tcp_proxy 
    - name: my_tcp-proxy