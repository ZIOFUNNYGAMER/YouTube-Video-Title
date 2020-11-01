import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
print("Tool Made By ZIOFUNNYGAMER")
def changeVideoTitle(id):
    title = input("Enter Title: ")
    CLIENT_SECRET_FILE = 'client_secret.json'
    SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
    credentials = flow.run_console()
    youtube = build('youtube', 'v3', credentials=credentials)
    
    request = youtube.videos().update(
        part="snippet",
        body={
          "id": id,
          "snippet": {
            "categoryId": 27,
            "title": title
          },
        }
    )
    response = request.execute()
    print("The Title of the video has been changed Successfully!")
changeVideoTitle("put-id-here")
