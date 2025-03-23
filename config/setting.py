import os

# Set API keys
#AIzaSyAPPSOFwJ-IxbaJKXsTmKsP9FnlgwFD8js  key for ravindrasingh446
os.environ["GOOGLE_API_KEY"] = "AIzaSyDF8-5ZZQAfKlziIBEVrHlySxvI17HDDXE"
#AIzaSyDF8-5ZZQAfKlziIBEVrHlySxvI17HDDXE  ravi dotnet
# print(os.environ.keys())
print(os.environ.get("HomePath"))

def get_google_api_key():
    api_key = "AIzaSyCwONkNOue8EMeSsb5VWva9jn0WfArTIjo"
    os.environ["GOOGLE_API_KEY"] = api_key
    print("get key"+ os.environ.get("GOOGLE_API_KEY"))
    return os.environ.get("GOOGLE_API_KEY")