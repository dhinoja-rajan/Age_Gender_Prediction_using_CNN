import gdown

# X_train = https://drive.google.com/file/d/1FQfOUFpbE3nHZmLYWXiXbK_c4N7NfgkW/view?usp=sharing
# X_test = https://drive.google.com/file/d/16c5Ca2rxCLm5hDzgMc_9TUfs4y9agEjD/view?usp=sharing
# y_age_train = https://drive.google.com/file/d/1loFfZJCsxURFKBYdw3tusdhtcACu4Isn/view?usp=sharing
# y_age_test = https://drive.google.com/file/d/1JNt4Iq08tMq-0ISOfb1C8EbvaRUOnwQS/view?usp=sharing
# y_gender_train = https://drive.google.com/file/d/1ch3PrECIb--qBV6MevKPMEhJx5LSeVFe/view?usp=sharing
# y_gender_test = https://drive.google.com/file/d/1df1bTyx5c3t5a6d7mwY9evO1JSYaUANc/view?usp=sharing

# age_gender_model.h5 = https://drive.google.com/file/d/1blbf8TmFyQgUyQF0lxE8KQV1PGI1eERg/view?usp=sharing

# File mapping: filename → Google Drive file ID
files_to_download = {
    "X_train.npy": "1FQfOUFpbE3nHZmLYWXiXbK_c4N7NfgkW",
    "X_test.npy": "16c5Ca2rxCLm5hDzgMc_9TUfs4y9agEjD",
    "y_age_train.npy": "1loFfZJCsxURFKBYdw3tusdhtcACu4Isn",
    "y_age_test.npy": "1JNt4Iq08tMq-0ISOfb1C8EbvaRUOnwQS",
    "y_gender_train.npy": "1ch3PrECIb--qBV6MevKPMEhJx5LSeVFe",
    "y_gender_test.npy": "1df1bTyx5c3t5a6d7mwY9evO1JSYaUANc",
    "age_gender_model.h5": "1blbf8TmFyQgUyQF0lxE8KQV1PGI1eERg",
}

# Download each file
for filename, file_id in files_to_download.items():
    url = f"https://drive.google.com/uc?id={file_id}"
    print(f"⬇️ Downloading {filename}...")
    gdown.download(url, filename, quiet=False)

print("\n✅ All files downloaded successfully.")
