def allowed_or_not(status):
    match status:
        case 401 | 403 | 404:
            return "Not allowed"
        case _:
            return "Allowed"

print(allowed_or_not(401))
print(allowed_or_not(403))
print(allowed_or_not(404))
print(allowed_or_not(200))