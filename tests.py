import requests
import json

headers = {
    'Authorization': 'Token 7c88b5a22bf24706f473d5c9b457698f4be293c1'
}
url = "http://0.0.0.0:8000/"
auth_res = requests.get(url, headers=headers)
if auth_res.status_code == 200:
    print("Authentication Successful")
else:
    print("Authentication failed!")

url = "http://0.0.0.0:8000/UploadedFiles/"
form_data = {
    "file": open("uploader_app/sample.txt", "rb"),
}
uploading_req = requests.post(url, files=form_data, headers=headers)
print(uploading_req.text)

if uploading_req.ok:
    print('Uploaded successfully')
    file_json = json.loads(uploading_req.text)
    file_id = file_json['id']

    url = "http://0.0.0.0:8000/UploadedFiles/" + str(file_id) + "/"
    uploadedfiles_res = requests.get(url, headers=headers)
    file_json = json.loads(uploadedfiles_res.text)
    dl_link = file_json['file']
    print('File successfully added to django admin panel.')
    print('Download link from minIO: '+dl_link)
else:
    print('Please upload the file again.')


url = "http://0.0.0.0:8000/UploadedFiles/"
uploadedfiles = requests.get(url, headers=headers)
if uploadedfiles.ok:
    uploadedfiles_json = json.loads(uploadedfiles.text)
    print('Here are all uploaded files in json: ')
    print(uploadedfiles_json)
else:
    print('Somthing is wrong is showing all uploaded files.')



url = "http://0.0.0.0:8000/UploadedFiles/"
form_data = {
    "file": open("uploader_app/sample.txt", "rb"),
}
uploading_req = requests.post(url, files=form_data, headers=headers)
if uploading_req.ok:
    file_json = json.loads(uploading_req.text)
    file_id = file_json['id']
    print('Your file uploaded with this id: '+str(file_id))

    url = "http://0.0.0.0:8000/UploadedFiles/" + str(file_id) + "/"
    deletedfile_res = requests.delete(url, headers=headers)
    print('Your file deleted with this id: '+str(file_id))

    url = "http://0.0.0.0:8000/UploadedFiles/"
    uploadedfiles = requests.get(url, headers=headers)
    if uploadedfiles.ok:
        uploadedfiles_json = json.loads(uploadedfiles.text)
        print(uploadedfiles_json)

else:
    print('Please upload the file again.')
