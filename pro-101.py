import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BGNrya96lMAeV4Yta9_tsauZvgiL4CzhPRtKT62UR40EOFLJ9LMzZituq_zQ1jwexrDAITy3AQw9Gh7Tpw70w0-mqyJuvJws_IQxywrJcDlfbd8Df9G-iP4XpHOrf_gjiYPFI4Q'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ")  
    
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()