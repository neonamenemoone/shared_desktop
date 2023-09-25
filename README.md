# shared_desktop

docker build -t shared_desktop_backend .
docker run --name shared_desktop_backend_container --rm -p 80:80 shared_desktop_backend