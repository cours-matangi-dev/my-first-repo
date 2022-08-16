FROM nginx:1.21.6-alpine
RUN rm /etc/nginx/conf.d/default.conf
COPY ./nginx/nginx.conf /etc/nginx/conf.d
RUN adduser -u 1000 -G user -h /home/user -D usern
USER user
CMD ["nginx", "-g", "daemon off;"]
