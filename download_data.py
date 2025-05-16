import gdown

# X_train =
# X_test = https://drive.google.com/file/d/16c5Ca2rxCLm5hDzgMc_9TUfs4y9agEjD/view?usp=sharing
# y_age_train = https://drive.google.com/file/d/1loFfZJCsxURFKBYdw3tusdhtcACu4Isn/view?usp=sharing
# y_age_test = https://drive.google.com/file/d/1JNt4Iq08tMq-0ISOfb1C8EbvaRUOnwQS/view?usp=sharing
# y_gender_train = https://drive.google.com/file/d/1ch3PrECIb--qBV6MevKPMEhJx5LSeVFe/view?usp=sharing
# y_gender_test = https://drive.google.com/file/d/1df1bTyx5c3t5a6d7mwY9evO1JSYaUANc/view?usp=sharing

# age_gender_model.h5 = https://drive.google.com/file/d/1blbf8TmFyQgUyQF0lxE8KQV1PGI1eERg/view?usp=sharing

# Download X_train.npy
gdown.download(
    "https://drive.google.com/uc?id=",
    "X_train.npy",
    quiet=False,
)

# Download X_test.npy
gdown.download(
    "https://drive.google.com/uc?id=16c5Ca2rxCLm5hDzgMc_9TUfs4y9agEjD",
    "X_test.npy",
    quiet=False,
)

# Download y_age_train.npy
gdown.download(
    "https://drive.google.com/uc?id=1loFfZJCsxURFKBYdw3tusdhtcACu4Isn",
    "y_age_train.npy",
    quiet=False,
)

# Download y_age_test.npy
gdown.download(
    "https://drive.google.com/uc?id=1JNt4Iq08tMq-0ISOfb1C8EbvaRUOnwQS",
    "y_age_test.npy",
    quiet=False,
)

# Download y_gender_train.npy
gdown.download(
    "https://drive.google.com/uc?id=1ch3PrECIb--qBV6MevKPMEhJx5LSeVFe",
    "y_gender_train.npy",
    quiet=False,
)

# Download y_gender_test.npy
gdown.download(
    "https://drive.google.com/uc?id=1df1bTyx5c3t5a6d7mwY9evO1JSYaUANc",
    "y_gender_test.npy",
    quiet=False,
)

# Download age_gender_model.h5
gdown.download(
    "https://drive.google.com/uc?id=1blbf8TmFyQgUyQF0lxE8KQV1PGI1eERg",
    "age_gender_model.h5",
    quiet=False,
)
