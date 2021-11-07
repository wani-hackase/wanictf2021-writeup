FROM nginx:1.20

COPY conf/nginx.conf /etc/nginx/nginx.conf

COPY conf/default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
