# MIT License
#
# Copyright (c) 2023 AnonymousX1025
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from googleapiclient.discovery import build

api_key = 'AIzaSyBnu63ZdfGU6WjOj8JG_P2Fn5rBZynRhIE'
youtube = build('youtube', 'v3', developerKey=api_key)

# البحث عن مقاطع الفيديو الموسيقية المتعلقة بكلمة مفتاحية
request = youtube.search().list(
    q='music keyword',  # أدخل الكلمة المفتاحية
    part='snippet',
    type='video',
    maxResults=5
)
response = request.execute()

# طباعة النتائج
for item in response['items']:
    print(f"Title: {item['snippet']['title']} - Channel: {item['snippet']['channelTitle']}")
