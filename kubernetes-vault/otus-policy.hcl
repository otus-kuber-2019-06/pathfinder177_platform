path "otus/otus-ro/*" {
    capabilities = ["read", "list"]
}

path "otus/otus-rw/*" {
    capabilities = ["read", "update", "create", "list"]
}
