import dropbox

dbx = dropbox.Dropbox("ACCESS TOKEN HERE")
incoming = "/Dropbox/Incoming/folder/here/"
outgoing = "/Dropbox/Outgoing/folder/here/"

files = dbx.files_list_folder(
                            incoming,
                            recursive=False,
                            include_media_info=False,
                            include_deleted=False,
                            include_has_explicit_shared_members=False,
                            include_mounted_folders=True,
                            limit=None,
                            shared_link=None,
                            include_property_groups=None,
                            include_non_downloadable_files=True
                            )

def download_files():
        for file in files.entries:
            try:
                name = (file.name)
                from_path = incoming + f"{name}"
                to_path = outgoing + f"{name}"
                print(f"Downloading {name}")
                with open(f"{name}", "wb") as f:
                    metadata, res = dbx.files_download(from_path)
                    f.write(res.content)
                print(f"Download complete, moving {name} to Outgoing")
                dbx.files_move(from_path, to_path, allow_shared_folder=False, autorename=False, allow_ownership_transfer=False)
            except ApiError as e:
                print(e)


if __name__ == '__main__':
    download_files()
