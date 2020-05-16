root@trooper:/home/kubernetes-vault# kubectl logs vault-0
==> Vault server configuration:

             Api Address: http://10.48.0.6:8200
                     Cgo: disabled
         Cluster Address: https://vault-0.vault-internal:8201
              Listener 1: tcp (addr: "[::]:8200", cluster address: "[::]:8201", max_request_duration: "1m30s", max_request_size: "33554432", tls: "disabled")
               Log Level: info
                   Mlock: supported: true, enabled: false
           Recovery Mode: false
                 Storage: consul (HA available)
                 Version: Vault v1.4.0

==> Vault server started! Log data will stream in below:

2020-05-15T17:41:43.892Z [INFO]  proxy environment: http_proxy= https_proxy= no_proxy=
2020-05-15T17:41:43.892Z [WARN]  storage.consul: appending trailing forward slash to path
2020-05-15T17:41:48.499Z [INFO]  core: seal configuration missing, not initialized

Unseal Key 1: 0DR9B4itM19gqiw63XVDCK0sSomgsCxTvBcqWbi90No=

Initial Root Token: s.MKeqHjzutBwvOeahnVzDxV90

Key                    Value
---                    -----
Seal Type              shamir
Initialized            true
Sealed                 false
Total Shares           1
Threshold              1
Version                1.4.0
Cluster Name           vault-cluster-7eacaf4e
Cluster ID             a038b957-29c8-f298-eb10-3b5a120db223
HA Enabled             true
HA Cluster             https://vault-0.vault-internal:8201
HA Mode                standby
Active Node Address    http://10.48.0.6:8200

Success! You are now authenticated. The token information displayed below
is already stored in the token helper. You do NOT need to run "vault login"
again. Future Vault requests will automatically use this token.

Key                  Value
---                  -----
token                s.MKeqHjzutBwvOeahnVzDxV90
token_accessor       nRUrRYUR9imoypnK0xYKx7kl
token_duration       ∞
token_renewable      false
token_policies       ["root"]
identity_policies    []
policies             ["root"]

Path      Type     Accessor               Description
----      ----     --------               -----------
token/    token    auth_token_23c01bc2    token based credentials

oot@trooper:/home/kubernetes-vault# kubectl exec -it vault-2 -- vault read otus/otus-ro/config
Key                 Value
---                 -----
refresh_interval    768h
password            asajkjkahs
username            otus

Path           Type          Accessor                    Description
----           ----          --------                    -----------
kubernetes/    kubernetes    auth_kubernetes_1c1fd651    n/a
token/         token         auth_token_23c01bc2         token based credentials

/otus/otus-rw/config accessed for write after the policy was updated with update capability

root@trooper:/home/kubernetes-vault# kubectl exec -it vault-2 -- vault write pki_int/issue/example-dot-ru common_name="gitlab.devlab.ru" ttl="24h"
Key                 Value
---                 -----
ca_chain            [-----BEGIN CERTIFICATE-----
MIIDnDCCAoSgAwIBAgIUQ0Sq05hyCDY8Z/7rSjREd+age1cwDQYJKoZIhvcNAQEL
BQAwFTETMBEGA1UEAxMKZXhhbXBsZS5ydTAeFw0yMDA1MTYxNTI0NTVaFw0yNTA1
MTUxNTI1MjVaMCwxKjAoBgNVBAMTIWV4YW1wbGUucnUgSW50ZXJtZWRpYXRlIEF1
dGhvcml0eTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMtE0fVi3I9T
V08v6dN6TSoBiDqM31kkQSxyeBVtQ+hNl/TN8pdi9bY/TWGmL2jftsWXDiuwJez+
8TyhNFHYH3buyhFXjsmFIkGJbuoXSMlkhoakoaFF3HUVcixclXmBPQBmRhJQiNFx
mo8jTUP9ptO4zXcinVWIIIfo5wg1sEij5MvSR+/7XQNrtx/zFsR6y7EXENeW4nDv
LoDSUGBTs1+9r0jeoGBHS3u1XxY79h7cMKoB2ZQf4JQ/qBmzWg+3uDjYIy246oGq
5ASxmE1V4U6i/YstItwrDsg7qJvShyYKBihcmYCKz/8SN697UXi7HfAjC5BgdjgA
UNTXtOAw7r8CAwEAAaOBzDCByTAOBgNVHQ8BAf8EBAMCAQYwDwYDVR0TAQH/BAUw
AwEB/zAdBgNVHQ4EFgQU33+qV21RaxWMnNzcelYVh7MmBuQwHwYDVR0jBBgwFoAU
7uEeTcmleH7fp1uXe7bFrvl9GegwNwYIKwYBBQUHAQEEKzApMCcGCCsGAQUFBzAC
hhtodHRwOi8vdmF1bHQ6ODIwMC92MS9wa2kvY2EwLQYDVR0fBCYwJDAioCCgHoYc
aHR0cDovL3ZhdWx0OjgyMDAvdjEvcGtpL2NybDANBgkqhkiG9w0BAQsFAAOCAQEA
FyCKNWp8KR6IpxIVNWmpjWqyxQlXHnB15UNpjozT6JLi47HOKBEiZ57kbLi1oVIn
czDiNiklSgXAcLEpnmx4RzqgL9d6jHO2x8vEUOIt3/2ue/APer7y8L2/hoIhP8yZ
hx1vhZom7uwaI1f5cXkCRdUByaD/EBPVjrebIi79yks+nKB004hT9ttJAQNcTRhQ
QllCKx2Q1OHlM/owfr2aoONUG8NqGztWNvcL3rP2I4otIhT1Pba2GLGdH83bJfvx
AWmD/XH+mZQF2HIzPdwhw/iSkymR/spL5/4wpm7EVLLgw2oNlrO+DMA7ZgJa262V
f3HxRe/hAmTiRIKwe8j1GQ==
-----END CERTIFICATE-----]
certificate         -----BEGIN CERTIFICATE-----
MIIDZTCCAk2gAwIBAgIUfywZ9t4Oc/kvVYBZsYDVkxw/jIkwDQYJKoZIhvcNAQEL
BQAwLDEqMCgGA1UEAxMhZXhhbXBsZS5ydSBJbnRlcm1lZGlhdGUgQXV0aG9yaXR5
MB4XDTIwMDUxNjE1MzQxMVoXDTIwMDUxNzE1MzQ0MFowGzEZMBcGA1UEAxMQZ2l0
bGFiLmRldmxhYi5ydTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBANoN
mimrMadIUDkAyJXmrrOz9YOhHAnFt0azmZEPXyBCcukm6Yoo1gpqFiqud3WHOecc
PajBVKgHWEhUaRHWMdwlkYTg5Qr+8na6nZwhN0Wsl/1BKre794fo+1fGmO8E9Np1
lsd4aFzdck5HsCT4p65tf2tY9J++hoE/pbwN3kUZvxIdJ2haECzmKJ3DPQGcvroc
yexqp6indYHXeEXed88UxGp4/ARIjARlI9klmv3r41AId9xMcntLtyIISLzK8ND+
PSzZ8J99nwH9zd/20UEV/et4B3KWVzqdJdegQ/zrY+ArEMsbVAlGSU3uq8EPeK/i
a3Vl6bzp/l/7DwTJCvcCAwEAAaOBjzCBjDAOBgNVHQ8BAf8EBAMCA6gwHQYDVR0l
BBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMB0GA1UdDgQWBBSc0Lk5I7VmdEffv4sW
Yaf7hVANojAfBgNVHSMEGDAWgBTff6pXbVFrFYyc3Nx6VhWHsyYG5DAbBgNVHREE
FDASghBnaXRsYWIuZGV2bGFiLnJ1MA0GCSqGSIb3DQEBCwUAA4IBAQBw2kE3NrK+
xU3MT1GUzbt5Eb613eJ8okTuh99Pi7GtI+WkhA1LYSLh1B7DgRSvcTL8AkfJV5Q+
7bzioWROHwf8BmYVM1oBT9pUVVH0faPfL6DThLkb3/SGOPVX7M3xkUw3lb7Bymr3
OVY9S+4GB7HyxYtrkb21CUWYiYzwWXu9SrUofwsxcT4fVyyB7XhMM3CgCKZSQo6c
KDLF1JTlJvJV2cYTuskfj7t0zlKqalUtmkcYhPDOlohZI5yPKFZa8wht+GuJ7Zw8
CScxA9OnBz1CrT+eRaZ1nxriZcAO3OBc7/3USN57k6IiqelnYkATJyCHaRdOMGTv
GjyiC2llL/2X
-----END CERTIFICATE-----
expiration          1589729680
issuing_ca          -----BEGIN CERTIFICATE-----
MIIDnDCCAoSgAwIBAgIUQ0Sq05hyCDY8Z/7rSjREd+age1cwDQYJKoZIhvcNAQEL
BQAwFTETMBEGA1UEAxMKZXhhbXBsZS5ydTAeFw0yMDA1MTYxNTI0NTVaFw0yNTA1
MTUxNTI1MjVaMCwxKjAoBgNVBAMTIWV4YW1wbGUucnUgSW50ZXJtZWRpYXRlIEF1
