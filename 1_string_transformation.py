import re
booking = "   EVT-2026 | alice_wong | Room-305 | 14:30 | alice.wong@UniMail.edu | VIP-VIP   "
parts = [p.strip() for p in booking.split("|")]

event_code = parts[0]
username = parts[1]
room = parts[2]
time = parts[3]
email = parts[4]
vip_field = parts[5]

name_display = username.title()
room_display = room.upper()
email_domain = email.split("@")[1].lower()
vip_count = vip_field.count("VIP")

valid_event_code = bool(re.fullmatch(r"[A-Z]{3}-\d{4}", event_code))
valid_username = bool(re.fullmatch(r"[a-z_]+", username))
valid_room = bool(re.fullmatch(r"[A-Za-z]+-\d+", room))
valid_time = bool(re.fullmatch(r"(?:[01]\d|2[0-3]):[0-5]\d", time))
valid_email = bool(re.fullmatch(r"[\w.+-]+@[\w-]+\.[\w.-]+", email))

print("Event code:", event_code)
print("Name:", name_display)
print("Room:", room_display)
print("Time:", time)
print("Email domain:", email_domain)
print("VIP tag count:", vip_count)
print("Valid event code:", valid_event_code)
print("Valid username:", valid_username)
print("Valid room:", valid_room)
print("Valid time:", valid_time)
print("Valid email:", valid_email)