# aws-api

```sh
pip install --platform manylinux1_x86_64 --target ./reqs --implementation cp --python-version 3.10 --only-binary=:all: --upgrade Flask aws-wsgi

rm rf python; mkdir python; pip install -r requirements.txt -t python; rm python.zip; zip -qr python.zip python
```

