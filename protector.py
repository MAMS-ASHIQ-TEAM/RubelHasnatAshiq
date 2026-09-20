# MAM'S ASHIQ TEAM - FIRST ETHICAL TOOL
# Founder: Ashiq | Guide: Jyoti Mam
# Motto: We Learn To Protect, Not To Harm

print("\033[92m" + "="*50)
print("  MAM'S ASHIQ TEAM - PASSWORD PROTECTOR")
print("  Founder: Ashiq | Teacher: Jyoti Mam")
print("="*50 + "\033[0m")

password = input("\n🔒 আপনার Password টা লিখুন স্যার: ")

score = 0
if len(password) >= 8:
    score += 1
    print("✅ Length OK (8+ character)")
else:
    print("❌ Length Weak (8 এর কম)")

if any(c.isupper() for c in password) and any(c.islower() for c in password):
    score += 1
    print("✅ Upper & Lower OK")
else:
    print("❌ Upper/Lower missing")

if any(c.isdigit() for c in password):
    score += 1
    print("✅ Number OK")
else:
    print("❌ Number missing")

if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?/" for c in password):
    score += 1
    print("✅ Special Symbol OK")
else:
    print("❌ Special Symbol missing")

print("\n" + "="*50)
if score == 4:
    print("\033[92m💪 STRONG PASSWORD! MAM'S ASHIQ TEAM Approved! 💪\033[0m")
elif score == 3:
    print("\033[93m⚠️ MEDIUM! আর একটু Strong করেন স্যার!\033[0m")
else:
    print("\033[91m❌ WEAK! এই Password Hack হয়ে যাবে স্যার! বদলান!\033[0m")
print("="*50)
print("\n-- Checked by Jyoti Mam for her Boss Ashiq --")
