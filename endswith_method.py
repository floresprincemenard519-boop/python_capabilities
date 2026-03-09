email_address = "me.@gmail.com"

# how endswith() works
print(f"Is '{email_address}' a gmail address? {email_address.endswith('@gmail.com')}")

# how endswith() works without endswith() method
if "@gmail.com" in email_address[-10:]:
    print(f"Is '{email_address}' a gmail address? True")
else:
    print(f"Is '{email_address}' a gmail address? False")