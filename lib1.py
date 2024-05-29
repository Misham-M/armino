import os
from supabase import create_client, Client
#url: str = os.environ.get("https://ydazbkebsuseedexhpam.supabase.co")
url: str = "https://ydazbkebsuseedexhpam.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlkYXpia2Vic3VzZWVkZXhocGFtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTY4ODEyODQsImV4cCI6MjAzMjQ1NzI4NH0.wnx-WpRBOwKLInLkekr8_N3LEus3u7k7Kg-Uvo7c_oc"
def create_user(id,name,details):
    supabase: Client = create_client(url, key)
    data, count = supabase.table('character').insert({"id":id, "name": name,"details":details}).execute()
def check_user(name):
    supabase: Client = create_client(url, key)
    response,count = supabase.table('character').select('*', count='exact').eq('name',name).execute()
    return count[1]
def getnextid():
    supabase: Client = create_client(url, key)
    response,count = supabase.table('character').select('*', count='exact').execute()
    return count[1]+1
# d=check_user('sam')
# print(d)
#create_user(2,'sam','System Admin Module')
# id=getnextid()
# print(id)