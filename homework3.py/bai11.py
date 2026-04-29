# Hệ thống phân quyền RBAC
def can_access(role, resource, action, rbac):
    if role not in rbac:
        return False
    
    if resource not in rbac[role]:
        return False
    
    if action not in rbac[role][resource]:
        return False
    
    return True

rbac = {
"admin": {"products": ["read","create","update","delete"],
"orders": ["read","update","delete"]},
"seller": {"products": ["read","create","update"],
"orders": ["read"]},
"customer": {"orders": ["read","create"]},
}
can_access("seller", "products", "delete", rbac) 
can_access("admin", "orders", "delete", rbac)
can_access("customer", "products", "read", rbac) 

print(can_access("admin", "orders", "delete", rbac))