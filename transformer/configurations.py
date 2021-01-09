# ------------------------------------------
# 
# Program created by Maksim Kumundzhiev
#
#
# email: kumundzhievmaxim@gmail.com
# github: https://github.com/KumundzhievMaxim
# -------------------------------------------

import logging

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger("Source Data Transformer")

DROP_COLUMNS_CICIDS = ['pld_ccnt',
                       'ack_psh_rst_syn_fin_cnt',
                       'dns_query_class',
                       'sa',
                       'rev_pld_ccnt',
                       'dns_query_type',
                       'rev_hdr_ccnt',
                       'dns_answer_ttl',
                       'rev_intervals_ccnt',
                       'hdr_ccnt',
                       'dns_answer_ip',
                       'da',
                       'intervals_ccnt',
                       'rev_ack_psh_rst_syn_fin_cnt',
                       'dns_query_name',
                       'dns_query_name_len',
                       'tls_ext_types',
                       'tls_svr_ext_types',
                       'tls_svr_cs',
                       'tls_cs',
                       'tls_len',
                       'tls_svr_len',
                       'http_host',
                       'http_uri',
                       'http_content_type',
                       ]

DROP_COLUMNS_NET = ['sa',
                    'intervals_ccnt',
                    'rev_pld_ccnt',
                    'rev_ack_psh_rst_syn_fin_cnt',
                    'rev_intervals_ccnt',
                    'hdr_ccnt',
                    'ack_psh_rst_syn_fin_cnt',
                    'rev_hdr_ccnt',
                    'pld_ccnt',
                    'da',
                    'dns_query_type',
                    'dns_query_class',
                    'dns_query_name_len',
                    'dns_query_name',
                    'tls_len',
                    'tls_svr_len',
                    'tls_svr_cs',
                    'tls_ext_types',
                    'tls_svr_ext_types',
                    'tls_cs',
                    'dns_answer_ip',
                    'dns_answer_ttl',
                    'http_uri',
                    'http_host',
                    'http_content_type'
                    ]