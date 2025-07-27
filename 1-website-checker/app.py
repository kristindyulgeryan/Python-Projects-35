print("🔍 WEBSITE URL CHECKER 🔍")
url = input("\nEnter a website URL: ")

if url.startswith("https://"):
    print("🔐 This website uses HTTPS(secure)")
elif url.startswith("http://"):
    print("👀 This website uses HTTPS(not secure)")
else:
    print("❌ This does't look like a complete URL")
