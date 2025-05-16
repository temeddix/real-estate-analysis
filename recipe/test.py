import paramiko


def download_sftp_file_as_string(url: str) -> str:
    # Parse the URL to extract hostname, port, and file path
    parts = url.split("/")
    hostname = parts[2].split(":")[0]
    port = int(parts[2].split(":")[1])
    remote_path = "/".join(parts[3:])

    # Establish an SFTP connection
    transport = paramiko.Transport((hostname, port))
    transport.connect(username="anonymous", password="")  # Anonymous access

    sftp = paramiko.SFTPClient.from_transport(transport)

    if sftp is None:
        return ""

    # Read the file contents as a string
    with sftp.open(remote_path, "r") as remote_file:
        file_contents = remote_file.read().decode("utf-8")

    # Close the connection
    sftp.close()
    transport.close()

    return file_contents


url = "sftp://kdhns.synology.me:5022/KDHPF/test_file.txt"
file_contents = download_sftp_file_as_string(url)
print("File Contents:")
print(file_contents)
