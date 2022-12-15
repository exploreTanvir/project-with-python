import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

number="+8801312591010"
numbers_country=phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(numbers_country,"en"))

numbers_operator=phonenumbers.parse(number,"RO")
print(carrier.name_for_number(numbers_operator,"en"))

numbers_timezone=phonenumbers.parse(number,"GB")
print(timezone.time_zones_for_number(numbers_timezone))
