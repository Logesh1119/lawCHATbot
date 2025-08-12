import pathlib

folder = pathlib.Path("ipc_vector_db")
if folder.exists and folder.is_dir():
    print("folder exist")
else:
    print("no")