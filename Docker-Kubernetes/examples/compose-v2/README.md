### Commands

docker compose build (build container)
docker compose up -d (run app)
docker compose ps (list containers)
docker compose logs -f web-fe (look at the db container logs)

### Deploy a second version using diff name

docker compose -p test up -d (deploy version with name test)

### Cleanup

docker compose down
docker compose ls
docker compose -p test down
docker compose ls
