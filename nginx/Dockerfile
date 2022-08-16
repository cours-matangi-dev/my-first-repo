FROM nginxinc/nginx-unprivileged:1.23
RUN rm /etc/nginx/conf.d/default.conf
COPY ./nginx/nginx.conf /etc/nginx/conf.d
USER nginx
CMD ["nginx", "-g", "daemon off;"]
