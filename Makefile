NAME = marina-portfolio

build:
	docker build -t marina-portfolio .

run:
	docker run -it --env-file .env/env.list -p 8000:8000 \
     -e DJANGO_SUPERUSER_USERNAME=os.getenv("admin_user", admin) \
     -e DJANGO_SUPERUSER_PASSWORD=os.getenv("admin_passw") \
     -e DJANGO_SUPERUSER_EMAIL=os.getenv("admin_email")\
     marina-portfolio
	

logs:
	docker logs -f $(NAME)

stop:
	docker stop $(NAME)
