import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import spacy.cli
spacy.cli.download("en_core_web_sm")
