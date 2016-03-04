import os.path


def sendMessage(message="Hello, World!", filename="index", save_path="/var/www/html/"):
    full_address = os.path.join(save_path, filename+".html")
    file_to_save = open(full_address, "w")
    file_to_save.write(message)
    file_to_save.close()

if __name__ == "__main__":
    sendMessage()
