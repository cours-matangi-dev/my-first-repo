FROM nginx:1.21.6-alpine
RUN rm /etc/nginx/conf.d/default.conf
COPY ./nginx/nginx.conf /etc/nginx/conf.d
RUN adduser -h /app -g user
USER user
CMD ["nginx", "-g", "daemon off;"]
